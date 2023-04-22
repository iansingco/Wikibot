import os
import langchain
from langchain.llms import OpenAI
from langchain.agents import load_tools, initialize_agent, AgentType, Tool, AgentExecutor, ConversationalChatAgent, ZeroShotAgent
from langchain.memory import ConversationBufferMemory
from langchain import LLMChain

#setup - Enter your OpenAI API KEY here
os.environ["OPENAI_API_KEY"] = ""
llm = OpenAI(temperature=0.7, model_name="text-davinci-003", openai_api_key = os.getenv("OPENAI_API_KEY"))
tools = load_tools(["wikipedia", "llm-math"], llm=llm)


prefix = """Have a conversation with a human, answering the following questions as best you can, and be friendly and conversational.
Do not use too many tokens, but do not keep it so short either.
If you sincerely do not know the answer or are not sure, say so, but try your best. You have access to the following tools:"""
suffix = """Begin!"

{chat_history}
Question: {input}
{agent_scratchpad}"""

prompt = ZeroShotAgent.create_prompt(
    tools, 
    prefix=prefix, 
    suffix=suffix, 
    input_variables=["input", "chat_history", "agent_scratchpad"]
)
memory = ConversationBufferMemory(memory_key="chat_history")

llm_chain = LLMChain(llm=llm, prompt=prompt)
agent = ZeroShotAgent(llm_chain=llm_chain, tools=tools, verbose=True)
agent_chain = AgentExecutor.from_agent_and_tools(agent=agent, tools=tools, verbose=True, memory=memory)



def agent(message):
    result = agent_chain.run(message)
    return str(result)



