from google.adk.agents import Agent
from tools.file_tools import save_html
from utils.load_instruction import load_instruction

instruction = load_instruction(__file__)

website_generation_agent = Agent(
    name="website_generation_agent",
    model="gemini-flash-latest",
    instruction=instruction,
    tools=[save_html],
    output_key="generated_website_path",
    disallow_transfer_to_parent=True
)