# Project Description

This project implements a chatbot using **AWS Bedrock**, utilizing the `bedrock-runtime` service for natural language processing. The chatbot leverages the **LangChain** library to interact with the Bedrock API, enabling language modeling and conversation generation.

![Screenshot](Screenshot%202023-12-25%20154047.png)

## Components

### AWS Services Used:

- **bedrock-runtime:** Utilized for natural language processing and model inference.

### Code Overview

The code integrates several components:

- **LangChain Integration:** Incorporates `LLMChain` from the LangChain library to interact with the Bedrock service.
- **Model ID:** Utilizes the "Amazon Titan Text Express" model (`amazon.titan-text-express-v1`) for chatbot functionality.
- **Streamlit UI:** Implements a user interface with Streamlit, enabling users to interact with the chatbot in different languages.

## How to Run

To run the project:

1. **Clone the repository:** `git clone <repository_URL>`
2. **Set up AWS credentials:** Configure your AWS credentials and required configurations.
3. **Install dependencies:** Run `pip install -r requirements.txt` to install the necessary packages.

---

# Code Overview

```python
from langchain.chains import LLMChain
from langchain.llms.bedrock import Bedrock
from langchain.prompts import PromptTemplate
import boto3
import os
from decouple import config
import streamlit as st

# Load environment variables from .env
os.environ["AWS_PROFILE"] = config('AWS_PROFILE')
region_name = config('AWS_REGION')  # Retrieve AWS region from .env

# Bedrock client setup using the region_name variable
bedrock_client = boto3.client(
    service_name="bedrock-runtime",
    region_name=region_name
)


