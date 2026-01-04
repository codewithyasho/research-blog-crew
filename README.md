# Research and Blog Crew

An AI-powered multi-agent system built with [CrewAI](https://crewai.com) that automatically generates comprehensive research reports and engaging blog posts on any given topic.


## Overview

This project implements a sequential AI workflow using CrewAI framework, where specialized AI agents collaborate to research a topic and create content. The system consists of two intelligent agents working together:

1. **Report Generator**: Conducts in-depth research and creates comprehensive reports
2. **Blog Writer**: Transforms research into engaging, reader-friendly blog posts

## Features

- 🤖 Multi-agent AI system with specialized roles
- 📊 Automated research report generation (~1000 words)
- ✍️ Creative blog post writing (~800 words)
- 🔄 Sequential task execution workflow
- 📁 Organized output file management
- ⚙️ YAML-based configuration for easy customization
- 🦙 Supports local LLM via Ollama (DeepSeek v3.1)

## Python Version

**⚠️ IMPORTANT: This project requires Python 3.11.9**

```bash
python --version
# Should output: Python 3.11.9
```

This specific version is required for compatibility with CrewAI and all project dependencies.

## Project Structure

```
research_and_blog_crew/
│
├── main.py                      # Entry point for running the crew
├── README.md                    # Project documentation
├── requirements.txt             # Project dependencies
│
├── src/
│   ├── __init__.py             # Package initializer
│   ├── crew.py                 # Main crew definition with agents and tasks
│   │
│   ├── config/
│   │   ├── agents.yaml         # Agent configurations (roles, goals, backstories)
│   │   └── tasks.yaml          # Task definitions and expected outputs
│   │
│   └── __pycache__/            # Python cache files
│
└── outputs/                     # Generated outputs directory
    ├── research_report.md      # Generated research report
    └── blog_post.md            # Generated blog post
```

## Installation

### Prerequisites

- **Python 3.11.9** (strictly required)
- pip package manager
- Ollama (for local LLM) or OpenAI API access

### Step 1: Clone or Download the Project

```bash
cd research_and_blog_crew
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# Create virtual environment
py -3.11 -m venv .venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install crewai crewai-tools litellm streamlit python-dotenv fastapi
```

### Step 4: Set Up Environment Variables

Create a `.env` file in the project root:

```bash
# For OpenAI (if not using local LLM)
OPENAI_API_KEY=your_openai_api_key_here

# For Ollama (if using local LLM)
OLLAMA_BASE_URL=http://localhost:11434
```

### Step 5: Set Up Ollama (Optional - for local LLM)

If using Ollama with DeepSeek:

```bash
# Install Ollama from https://ollama.ai/

# Pull the DeepSeek model
ollama pull deepseek-v3.1:671b-cloud

# Start Ollama service
ollama serve
```

## Configuration

### Agents Configuration

Edit `src/config/agents.yaml` to customize agent behaviors:

- **report_generator**: Expert at creating detailed research reports
- **blog_writer**: Creative writer for engaging blog content

Each agent has:
- `name`: Display name
- `role`: Agent's role with topic placeholder
- `goal`: Primary objective
- `backstory`: Context and expertise
- `llm`: LLM model to use
- `base_url`: LLM endpoint

### Tasks Configuration

Edit `src/config/tasks.yaml` to modify task requirements:

- **report_task**: Generates comprehensive research report
- **blog_writing_task**: Creates engaging blog post from research

### Changing the Topic

Modify the input in `main.py`:

```python
inputs = {
    "topic": "Your Topic Here",  # Change this to any topic
}
```

## Usage

### Run the Crew

Execute the main script:

```bash
python main.py
```

### What Happens:

1. **Report Generation**: The report generator agent researches the topic and creates a detailed report
2. **Blog Writing**: The blog writer agent takes the research and crafts an engaging blog post
3. **Output**: Both outputs are saved in the `outputs/` directory

### Expected Output

```
outputs/
├── research_report.md    # ~1000 word research report
└── blog_post.md          # ~800 word blog post
```

## Agents

### 1. Report Generator
- **Role**: Expert report generator on specified topic
- **Goal**: Creating detailed reports with comprehensive coverage
- **Skills**: Data organization, research synthesis, structured presentation

### 2. Blog Writer
- **Role**: Creative blog writer on specified topic
- **Goal**: Writing engaging and accessible blog posts
- **Skills**: Storytelling, content simplification, reader engagement

## Tasks

### 1. Report Task
- **Agent**: report_generator
- **Output**: Comprehensive 1000-word research report
- **File**: `outputs/research_report.md`

### 2. Blog Writing Task
- **Agent**: blog_writer
- **Output**: Engaging 800-word blog post
- **File**: `outputs/blog_post.md`

## Output

All generated content is automatically saved to the `outputs/` directory:

- **research_report.md**: Detailed, factual research report
- **blog_post.md**: Engaging, reader-friendly blog post

## Technologies Used

- **[CrewAI](https://crewai.com)** - Multi-agent orchestration framework
- **Python 3.11.9** - Programming language
- **Ollama/DeepSeek** - Local LLM (or OpenAI API)
- **python-dotenv** - Environment variable management
- **YAML** - Configuration files

## Support

### CrewAI Resources
- [Documentation](https://docs.crewai.com)
- [GitHub Repository](https://github.com/joaomdmoura/crewai)
- [Discord Community](https://discord.com/invite/X4JWnZnxPb)
- [Interactive Docs](https://chatg.pt/DWjSBZn)

### Common Issues

**Issue**: Import errors or module not found
**Solution**: Ensure Python 3.11.9 is installed and all dependencies are installed via `pip install -r requirements.txt`

**Issue**: LLM connection errors
**Solution**: Check Ollama is running (`ollama serve`) or verify OpenAI API key in `.env` file

**Issue**: No output generated
**Solution**: Check console for errors, verify agent configurations in YAML files

---

Built with ❤️ using CrewAI | Python 3.11.9
