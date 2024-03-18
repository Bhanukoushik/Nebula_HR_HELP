import streamlit as st 
from dotenv import load_dotenv
from uuid import uuid4
from utils import *
import time
import smtplib
from email.mime.text import MIMEText

def send_rejection_email(doc):
    resume_text = doc.page_content
    candidate_email = extract_email(resume_text)
    if not candidate_email:
        print(f"No email found for {doc[0].metadata['name']}")
        return

    candidate_name = doc.metadata['name'].split(".")[0]
    print ("candidateemail: " + candidate_email)
    # Email settings
    sender_email = "koushikavuthucs3018@gmail.com"
    receiver_email = candidate_email
    subject = "Application Status Update"
    body = f"Dear {candidate_name},\n\nThank you for your interest and for applying for the position. Unfortunately, we have decided to move forward with other candidates whose qualifications more closely match our requirements at this time.\n\nWe appreciate your time and effort in the application process, and we wish you the best in your future endeavors.\n\nBest regards, HR"

    # Create email message
    message = MIMEText(body)
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email

    # Send email
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.login("koushikavuthucs3018@gmail.com", "password")
        smtp.send_message(message)
        print(f"Rejection email sent to {candidate_email}")

#session_state
if 'unique_key' not in st.session_state:
  st.session_state['unique_key']=''


def main():
  st.set_page_config(page_title='HR HELP')
  st.title('👨‍🎓Automated Resume to Job Description Matching System:🕵️‍♀️')
  st.subheader('An AI system to match resumes with job descriptions, aiding HR in recruitment processes by highlighting the most suitable candidates.')

  #loading the keys 
  load_dotenv()
  
  # api_key = st.text_input("Please enter your Anthropic API key", type="password")
  with st.sidebar:
    st.write("Please enter your Anthropic API Key here")
    api_key = st.text_input("API Key", type="password")

    # Check if API key is provided
  if not api_key:
    st.error("Please enter your Anthropic API key in the sidebar.")
    return


  job_desc=st.text_area("Enter or Paste your 'JOB DESCRIPTION' below")
  num_count=st.text_input('Enter the number of resumes to filter out ')
  files=st.file_uploader('Please upload resumes here, Only pdf files allowed',type=['pdf'],accept_multiple_files=True)

  button=st.button(f'Filter out the top {num_count} profiles')


  if button:
    with st.spinner('Wait for it........'):
      st.session_state['unique_key']=uuid4().hex
      docs=create_docs(files,st.session_state['unique_key'])
      st.write('creating the docs......')

      #get embeddings
      st.write('getting embeddings from Hugging face hub......')
      embeddings=get_embeddings()
  
      st.write('storing the docs/embeddings into Pinecone Vector DB......')
      store_to_pinecone(docs,embeddings)
      
      time.sleep(20)

      #retrieval of docs
      st.write('retrieve relevant docs/embeddings from Pinecone Vector DB......')
      relevant_docs=get_docs_from_pinecone(job_desc,num_count,embeddings,st.session_state['unique_key'])
      st.write(relevant_docs)

      st.write(f'A detailed summary profiles of top {num_count} candidates with their score is coming your way shortly')
    
    
      selected_doc_ids = [doc[0].metadata['id'] for doc in relevant_docs]

      for doc in relevant_docs:
        summary=get_summary(doc, api_key)
        st.divider()
        st.write(f"Resume Name: {doc[0].metadata['name']}")
        st.write(f'Score:{doc[1]}')
        with st.expander('Show Summary'):
          st.write('Summary:')
          st.write(f'{summary}')
      st.write("Above are the Candidates matching our requirements")
      # if doc[0].metadata['id'] not in selected_doc_ids:
      #   send_rejection_email(doc)
        
      # Send rejection emails to candidates who were not selected
      for doc in docs:
        doc_id = doc.metadata['id']
        if doc_id not in selected_doc_ids:
          send_rejection_email(doc)
      st.write("Rejection Mails sent to the candidates who are not matching with our requirements.")

    st.success('Filtering completed. Thank You')



if __name__=='__main__':
  main()
