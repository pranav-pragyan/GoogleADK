# Setup and Running Instructions for GoogleADK Projects

These instructions apply to all four projects in this repository: `single_agent`, `sequential_agents`, `parallel_agent`, and `loop_agents`.

## Prerequisites
- Python 3.10 or higher
- [GoogleADK](https://github.com/google/adk) installed (follow official instructions)
- (Recommended) Use a virtual environment

## Setup Steps

1. **Clone the repository:**
   ```sh
   git clone <your-repo-url>
   cd <repo-folder>
   ```

2. **Create and activate a virtual environment:**
   ```sh
   python3 -m venv .env
   source .env/bin/activate
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Install GoogleADK (if not already installed):**
   ```sh
   pip install google-adk
   ```

## Running Each Project

### single_agent
1. Change directory:
   ```sh
   cd single_agent
   ```
2. Start the ADK web server:
   ```sh
   adk web .
   ```
3. Open your browser and go to [http://127.0.0.1:8000](http://127.0.0.1:8000)

### sequential_agents
- Work in progress. Instructions will be added once implemented.

### parallel_agent
- Work in progress. Instructions will be added once implemented.

### loop_agents
- Work in progress. Instructions will be added once implemented.

## Notes
- Output files (such as generated HTML) will be saved in the `output` directory inside the corresponding project folder (e.g., `single_agent/output`).
- For any issues, ensure your Python environment is activated and all dependencies are installed.
