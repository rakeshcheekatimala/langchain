from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from third_parties.linkedin import scrape_linkedin_profile

if __name__ == "__main__":
    summary_template = """
        given the information {information} about a person from I want you to create:
        1. a short summary
        2. two interesting facts about them
    """
    summary_prompt_template = PromptTemplate(input__variables=["information"], template=summary_template)
    llm = ChatOllama(model="llama3")
    chain = summary_prompt_template | llm
    linkedin_data = scrape_linkedin_profile(
        linkedin_profile_url="https://linkedin.com/in/rakesh-cheekatimala/",mock=True
    )
    res = chain.invoke(input={"information": linkedin_data})
    print(res)
