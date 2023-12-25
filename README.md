# Project Description

This project implements a chatbot using **AWS Bedrock**, leveraging the `bedrock-runtime` service for natural language processing. The chatbot is powered by the **LangChain** library, enabling interaction with the Bedrock API for language modeling and conversation generation.

![Screenshot](Screenshot%202023-12-25%20154047.png)

## Components

### AWS Services Used:

- **bedrock-runtime:** Utilized for natural language processing and model inference.

### Code Overview

The code comprises several components:

- **LangChain Integration:** Incorporates `LLMChain` from the LangChain library to interact with the Bedrock service.
- **Model ID:** Utilizes the "Amazon Titan Text Express" model (`amazon.titan-text-express-v1`) for chatbot functionality.
- **Streamlit UI:** Implements a user interface with Streamlit, enabling users to interact with the chatbot in different languages.

## How to Run

To run the project:

1. **Clone the repository:** `git clone <repository_URL>`
2. **Set up AWS credentials:** Configure your AWS credentials and required configurations.
3. **Install dependencies:** Run `pip install -r requirements.txt` to install the necessary packages.
4. **Run Streamlit server:** Execute `python3 -m streamlit run main.py` to start the Streamlit server.

---

