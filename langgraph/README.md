# LangGraph

## Development Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/devlabs-learn/agentic-ai.git
   cd agentic-ai
```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
```

4. Setup your Groq API key as an environment variable:
   ```bash
   export GROQ_API_KEY="your_groq_api_key_here"  # On Windows, use `set GROQ_API_KEY=your_groq_api_key_here`
```

## Running the Example
To run the agentic team example, execute the following command:
```bash
python langgraph/agentic_team.py
```