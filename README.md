Project Description
This project implements a chatbot using AWS Bedrock, utilizing the bedrock-runtime service for natural language processing. The chatbot leverages the LangChain library to interact with the Bedrock API, enabling language modeling and conversation generation.

![Alt text](<Screenshot 2023-12-25 154047.png>)


Components:
AWS Services Used:

bedrock-runtime: Utilized for natural language processing and model inference.
Code Overview:

LangChain Integration: Incorporates LLMChain from the langchain library to interact with the Bedrock service.
Model ID: Utilizes the "Amazon Titan Text Express" model (amazon.titan-text-express-v1) for chatbot functionality.
Streamlit UI: Implements a user interface with Streamlit, enabling users to interact with the chatbot in different languages.
How to Run:
Clone the repository and set up the necessary AWS credentials and configuration.
Install the required packages by using the requirements.txt file.