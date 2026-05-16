from google.adk.agents import Agent
from utils.load_instruction import load_instruction
from agents.website_prompt_engineer_agent.agent import website_prompt_engineer_agent

instruction = load_instruction(__file__)

information_gathering_agent = Agent(
    name="information_gathering_agent",
    model="gemini-flash-latest",
    instruction=instruction,
    output_key="user_requirement"
)