from dotenv import load_dotenv
from phi.agent import Agent
from phi.model.groq import Groq

load_dotenv()

agent = Agent(
    model = Groq(id = "llama-3.3-70b-versatile")
)


agent.print_response("write some info about the india great modern legend virat kohli")