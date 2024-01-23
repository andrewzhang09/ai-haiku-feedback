from flask import render_template

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from ..constants import OPENAI_API_KEY

def initialize_llm_chain():
    llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY)
    prompt = ChatPromptTemplate.from_messages([
        ('system', 'You are a helpful assistant designed to rate haikus and generate haikus')
    ])
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    return chain

# TODO: validate that user input is a haiku, if not then input different thing to OpenAI
# TODO: save input to SQLite database
def form_handler(user_input):
    chain = initialize_llm_chain()
    response = chain.invoke({'input': user_input})
    return render_template('result.html', user_input=user_input, response=response)