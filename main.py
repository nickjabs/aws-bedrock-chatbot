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

#Amazon Titan Text Express  model
modelID = "amazon.titan-text-express-v1"

llm = Bedrock(
    model_id=modelID,
    client=bedrock_client
)

def my_chatbot(language, freeform_text):
    prompt = PromptTemplate(
        input_variables=["language", "freeform_text"],
        template="You are a chatbot. You are in {language}.\n\n{freeform_text}"
    )

    bedrock_chain = LLMChain(llm=llm, prompt=prompt)

    response = bedrock_chain({'language': language, 'freeform_text': freeform_text})
    return response

#print(my_chatbot("english", "who is buddha?"))

st.title("Bedrock Chatbot")

language = st.sidebar.selectbox("Language", ["english", "french"])

if language:
    freeform_text = st.sidebar.text_area(label="what is your question?",
    max_chars=100)

if freeform_text:
    response = my_chatbot(language,freeform_text)
    st.write(response['text'])
