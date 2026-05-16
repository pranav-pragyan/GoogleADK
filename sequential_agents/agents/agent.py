from google.adk.agents import SequentialAgent
from agents.information_gathering_agent.agent import information_gathering_agent
from agents.website_prompt_engineer_agent.agent import website_prompt_engineer_agent
from agents.website_generation_agent.agent import website_generation_agent
from utils.load_instruction import load_instruction


root_agent = SequentialAgent(
    name="Website_Creation_Agent",
    description=load_instruction(__file__, instruction_file="root_agent_description.txt"),
    sub_agents=[information_gathering_agent, website_prompt_engineer_agent, website_generation_agent]
)