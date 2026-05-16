from google.adk.runners import Runner
from google.genai import types

from single_agent.agents.html_agent import html_agent


runner = Runner(agent=html_agent)

user_prompt = input("Enter webpage requirement: ")

response = runner.run(
    user_id="pranav",
    session_id="html_session",
    new_message=types.Content(
        role="user",
        parts=[types.Part(text=user_prompt)]
    )
)

print("\n=== AGENT RESPONSE ===\n")
print(response)