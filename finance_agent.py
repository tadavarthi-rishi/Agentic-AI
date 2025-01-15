from dotenv import load_dotenv
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
load_dotenv()

agent = Agent(
    model = Groq(id = "llama-3.3-70b-versatile"),
    tools = [YFinanceTools(stock_price = True, analyst_recommendations = True, stock_fundamentals = True)],
    show_tool_calls = True,
    markdown = True,
    instructions = ["use tables to display data."]
)


agent.print_response("summarize and compare analyst recommendations and fundamentals between Amazon and Google")