# AI-research-Agent


This is an AI-powered assistant built using LangChain and Gemini 1.5. It can take a topic, search the web and Wikipedia, summarize the results, and save the output to a .txt file.


---

🔧 Features

Takes any research topic as input

Uses Wikipedia + Web Search tools to collect information

Summarizes content using Gemini LLM

Outputs a structured response: topic, summary, sources

Saves the result in a text file automatically



---

🛠 Tech Stack

Python

LangChain

Gemini 1.5 (Google Generative AI)

Wikipedia API

DuckDuckGo Search

Pydantic (for output formatting)



---

🚀 How to Run

1. Clone this repo

git clone https://github.com/yourusername/ai-research-agent.git
cd ai-research-agent


2. Set up virtual environment

python -m venv venv
venv\Scripts\activate   # For Windows


3. Install dependencies

pip install -r requirements.txt


4. Add your API key
Create a .env file like this:

GEMINI_API_KEY=your_api_key_here


5. Run the project

python main.py




---

📁 Files

main.py – Runs the AI agent

tools.py – Contains custom tools for search and saving

.env.example – Example for your API key

requirements.txt – Python packages

research_output.txt – Where the result is saved



---

✅ Example Output

Topic: Space Colonization  
Summary: Talks about Mars vs Moon for human settlement...  
Sources: Wikipedia, NASA  
Saved to: research_output.txt


---

📌 Coming Soon

PDF Export

Web Interface (Streamlit)
