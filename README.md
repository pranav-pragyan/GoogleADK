# GoogleADK Projects

This repository contains four projects built with the Google Agent Development Kit (GoogleADK):

## single_agent
A project featuring a single HTML generator agent using GoogleADK. This agent:
- Acts as an expert frontend developer.
- Generates complete, modern, and responsive HTML pages based on user prompts.
- Includes inline CSS for styling.
- Saves generated HTML files to the project output directory.
- Strictly refuses to generate HTML for prompts unrelated to webpage creation, replying with a clear refusal message.

The agent is defined in `single_agent/agents/html_agent.py` and exposed via `single_agent/agents/agent.py` as `root_agent` for ADK compatibility. The project demonstrates prompt engineering, tool integration, and output handling with GoogleADK.

## sequential_agents
Work in progress.

## parallel_agent
Work in progress.

## loop_agents
Work in progress.
