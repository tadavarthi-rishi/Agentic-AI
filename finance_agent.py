from dotenv import load_dotenv
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
import os
import openai
load_dotenv()
from phi.tools.duckduckgo import DuckDuckGo
openai.api_key = os.getenv("OPENAI_API_KEY")
## web search agent
web_search_agent = Agent(
    name = "Web Search Agent",
    role = "Search the web for information",
    model = Groq(id = "llama-3.3-70b-versatile"),
    tools = [DuckDuckGo()],
    instructions = ["Always include sources"],
    show_tool_calls = True,
    markdown = True,
)
finance_agent = Agent(
    name = "Finance AI Agent",
    model = Groq(id = "llama-3.3-70b-versatile"),
    tools = [YFinanceTools(stock_price = True, analyst_recommendations = True, stock_fundamentals = True, company_news = True)],
    show_tool_calls = True,
    markdown = True,
    instructions = ["use tables to display data."]
)

multi_ai_agent = Agent(
    team = [web_search_agent, finance_agent],
    markdown = True,
    show_tool_calls = True,
    instructions = ["Always include sources", "Use table to display the data"]
)


multi_ai_agent.print_response("Summarize analyst recommendations and share the latest news for NVDA", stream = True)