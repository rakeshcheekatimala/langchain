# Key Points
- The code uses LangChain's PromptTemplate to create a structured prompt.
- It utilizes the OpenAI Chat model through the ChatOpenAI class.
- The chain is created by piping the prompt template into the LLM model.
- The invoke method is used to run the chain with the provided input.

# Best Practices
- Using environment variables (load_dotenv) for sensitive information.
- Structuring prompts using PromptTemplate for clarity and reusability.
- Initializing the LLM model with appropriate parameters (temperature, model name).
- Using chaining to combine prompt templates with LLM models efficiently.

# Agent

- Identifies & create subtasks for your problem
- Uses tools to perform those subtasks
- Once complete those subtasks return the answer we want.

# Langchain Tools 

- Tools are interfaces that interact with external world to link with Langchain.
- It has a function to execute which is callable.
- It has description which describes what that function should do and what is the output.
- The power of Langchain we can make any function written in python into langchain tool & make
it accessible to LLM.

Based on the description LLM will decide which tool to invoke based on the reasoning engine 

```
 tools_for_agent = [
        Tool(name="Crawl Google for linkedin profile age", func="?", description="useful when you need to get linkedin page url")
    ]
```