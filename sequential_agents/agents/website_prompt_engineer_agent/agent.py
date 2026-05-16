from google.adk.agents import Agent
from utils.load_instruction import load_instruction
from agents.website_generation_agent.agent import website_generation_agent

instruction = load_instruction(__file__)

website_prompt_engineer_agent = Agent(
    name="website_prompt_engineer_agent",
    model="gemini-flash-latest",
    instruction=instruction,
    output_key="website_specification"
)