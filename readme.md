# Automated Resume to Job Description Matching System:

## Overview

This is an AI system to match resumes with job descriptions, aiding HR in
recruitment processes by highlighting the most suitable candidates and automatically sending rejection mails to candidates who are not matching with the job requirements. 

Bulit using Python, Langchian, Anthropic Claude API, Pinecone, SMTP library, Steamlit.

## Installation & create environment

Clone the project

```bash
  git clone https://github.com/Bhanukoushik/Nebula_HR_HELP.git
```

Go to the project directory

```bash
  cd Nebula_HR_HELP
```

Create the enviroment

```bash
  conda create --name env_name_of_your_choice python=3.10
  conda activate env_name_of_your_choice

```

Install dependencies

```bash
  pip install -r requirements.txt
```

Insert API keys in the .env file
```bash
  insert your key as following
  HUGGINGFACEHUB_API_TOKEN=""
  PINECONE_API_KEY=""
```

Start the server

```bash
  streamlit run app.py
```

## Features

+ **Job Description Matching:** It compares the content of uploaded resumes with a provided job description to identify candidates whose qualifications closely match the job requirements (Hugging face for Embeddings, Pinecone for Vector Storage, Cosine/dot product Similarity for matching).

+ **Automated Summary Generation:** For selected candidates, the tool generates a summary of their qualifications and experience to aid HR professionals in making informed decisions (Anthropic Claude Opus model and Langchain).

+ **Automated Email Notification:** The tool automatically sends rejection emails to candidates whose resumes do not match the job description, providing them with feedback on their application status (SMTP library).


### Usage

First create accounts in Anthropic Claude, Pinecone, Huggging Face.

Then take API keys from them which are free for certain limits. 

When you hit `streamlit run app.py` it will open a streamlit user interface.

First provide your Anthropic Claude API key at side panel of UI.

Then enter your Job Description, Numbers of resumes you want to filter out of all the resumes you will upload and the Upload the resumes in PDF type(can upload multiple resumes.)

Then hit the filter resume button.

You will be getting the list of Candidate profiles with Summaries and Matching score in the order and our tool will be automatically sending rejection emails to candidates who are not matching with job requirements.

### Test Results
**1. Entering Inputs**
![WhatsApp Image 2024-03-19 at 10 27 52](https://github.com/Bhanukoushik/Nebula_HR_HELP/assets/92176220/c1c30eda-b6fe-4cd9-b740-9129c411ab85)

![WhatsApp Image 2024-03-19 at 10 29 17](https://github.com/Bhanukoushik/Nebula_HR_HELP/assets/92176220/6d5741cb-500a-468a-ad04-c7ef12695b4f)


**2. Comparing Two Candidates**
![WhatsApp Image 2024-03-18 at 03 28 51](https://github.com/Bhanukoushik/Nebula_HR_HELP/assets/92176220/9aef2759-c95d-472e-96d0-7cedfe717dd5)

**3. Matching Score and Summary of a Candidate**
![WhatsApp Image 2024-03-18 at 14 04 02](https://github.com/Bhanukoushik/Nebula_HR_HELP/assets/92176220/10eaedd2-4040-41c6-8e8f-36ec4dc85352)

**4.Rejection Mail Notification in Terminal**
![WhatsApp Image 2024-03-18 at 15 37 19](https://github.com/Bhanukoushik/Nebula_HR_HELP/assets/92176220/c34487bb-8bd6-4615-9d93-6034cbb528ed)

**5. Rejection Mail Notification Sent to Candidate Email Automatically**
![WhatsApp Image 2024-03-18 at 16 44 49](https://github.com/Bhanukoushik/Nebula_HR_HELP/assets/92176220/19f72467-f58b-4e75-8a00-67b865286db3)

