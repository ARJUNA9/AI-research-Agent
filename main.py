from dotenv import load_dotenv
from pydantic import BaseModel
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools import search_tool,wiki_tool,save_tool
load_dotenv()
class ResearchrResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]
api_key = os.getenv("GEMINI_API_KEY")  

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=api_key)  
parser = PydanticOutputParser(pydantic_object=ResearchrResponse)

prompt = ChatPromptTemplate.from_messages([
    ("system", """You are a research assistant that helps generate high-quality research content for the user.
Use tools like Wikipedia and web search whenever needed to gather accurate and relevant information.
At the end of every response, always call the save_txt_to_file tool to save the final structured result.
Wrap the final output in this format and provide no other text: \n{format_instructions}
     """,
     ),
    ("placeholder", "{chat_history}"),
    ("human", "{query}"),
    ("placeholder", "{agent_scratchpad}"),
]
).partial(
    format_instructions= parser.get_format_instructions()
)
tools = [search_tool, wiki_tool, save_tool]
agent = create_tool_calling_agent(
    llm=llm,
    prompt=prompt,
    tools=tools,
)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
query = input("What can i help you research today?")
raw_response = agent_executor.invoke({"query":query})
# print(raw_response)
try:
    output_str = raw_response.get("output", "")
    
    # Remove ```json and surrounding backticks
    if output_str.startswith("```json"):
        output_str = output_str.strip("`").strip()
        output_str = output_str.split('\n', 1)[1]  # Get the JSON string after first line

    structured_response = parser.parse(output_str)
    print(structured_response)  
    from tools import save_to_txt
    save_to_txt(structured_response.model_dump_json(indent=2))

except Exception as e:
    print("Error parsing response:", e, "raw_response:", raw_response)
