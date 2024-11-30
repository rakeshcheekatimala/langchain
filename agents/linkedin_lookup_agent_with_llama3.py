from dotenv import load_dotenv

load_dotenv()
import subprocess
from langchain_openai import ChatOpenAI
from langchain.prompts.prompt import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import (
    create_react_agent,
    AgentExecutor,
)
from langchain import hub
from tools.tools import get_profile_url_tavily
from langchain.llms.base import BaseLLM
from typing import List, Optional
from langchain.schema import Generation, LLMResult
# Custom LLM class to interact with Ollama
class OllamaLLM(BaseLLM):
    def _generate(self, prompts: List[str], stop: Optional[List[str]] = None) -> LLMResult:
        """Generates responses using the Ollama CLI."""
        responses = []
        for prompt in prompts:
            result = subprocess.run(
                ["ollama", "run", "llama3"],
                input=prompt.encode("utf-8"),
                stdout=subprocess.PIPE
            )
            output = result.stdout.decode("utf-8").strip()
            responses.append(Generation(text=output))
        return LLMResult(generations=[responses])

    @property
    def _identifying_params(self):
        return {}

    @property
    def _llm_type(self):
        return "ollama"


def lookup(name: str) -> str:
    llm = OllamaLLM()
    template = """given the full name {name_of_person} I want you to get it me a link to their Linkedin profile page.
                              Your answer should contain only a URL"""
    prompt_template = PromptTemplate(template=template, input_variables=["name_of_person"])

    tools_for_agent = [
        Tool(name="Crawl Google for linkedin profile age", func=get_profile_url_tavily,
             description="useful when you need to get linkedin page url")
    ]

    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    # Agent executor is the runtime of the engine
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)

    result = agent_executor.invoke(input={"input": prompt_template.format_prompt(name_of_person=name)})
    linked_profile_url = result["output"]
    return linked_profile_url


if __name__ == "__main__":
    print("Inside Agent with LLAMA3")
    print(lookup(name="Rakesh Cheekatimala"))
