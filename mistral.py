from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

if __name__ == "__main__":
    summary_template = """
       Tell me poem about pizza in 5 lines
    """
    # Create a PromptTemplate without needing input variables (since none are used).
    summary_prompt_template = PromptTemplate(template=summary_template, input_variables=[])

    llm = ChatOllama(model="mistral")
    chain = summary_prompt_template | llm | StrOutputParser()
    # Pass an empty object as input for prompts with no variables.
    res = chain.invoke({})
    print(res)
