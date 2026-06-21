
 Financial Researcher - AI-Powered Multi-Agent Financial Analysis

An AI agent system that automates company financial research and report writing, built with [CrewAI](https://www.crewai.com/). Give it a company name and stock ticker, and two specialized AI agents - a researcher and an analyst - collaborate to produce a polished, structured financial report in minutes instead of the 30-60+ minutes this would typically take a human analyst.

## The Problem

Researching a company's financial health typically means manually cross-referencing multiple sources: news articles, investor relations pages, and live stock data - then synthesizing all of it into a coherent report. This is repetitive, time-consuming, and easy to do inconsistently across different companies or analysts.

## The Solution

This project simulates a small research team using AI agents with distinct roles:

- **Researcher Agent** - gathers qualitative information via web search and pulls **live, real-time quantitative data** (stock price, market cap, P/E ratio, 52-week range) directly from Yahoo Finance using a custom tool
- **Analyst Agent** - synthesizes the researcher's findings into a polished, professional report with an executive summary, key insights, and a market outlook

The two agents pass context between each other automatically, the same way a junior researcher would hand off findings to a senior analyst for write-up.

## How It Works (Architecture)
User Input (company + ticker)

│

▼

┌─────────────────────┐

│  Researcher Agent    │── uses ──▶ Web Search Tool (Serper)

│  (research_task)     │── uses ──▶ Live Stock Data Tool (yfinance)

└─────────┬────────────┘

│ (findings passed as context)

▼

┌─────────────────────┐

│  Analyst Agent        │

│  (analysis_task)      │

└─────────┬────────────┘

▼

output/{TICKER}_report.md

Built on **CrewAI's sequential process** - the researcher's output flows directly into the analyst's prompt via task context, with no manual handoff required.

## Tech Stack

- **[CrewAI](https://www.crewai.com/)** - multi-agent orchestration framework
- **OpenAI GPT-4o-mini** - LLM powering both agents
- **SerperDevTool** - web search (Google Search API)
- **yfinance** - custom tool for live, real-time financial data (no API key required)
- **Pydantic** - structured tool input validation
- **uv** — Python dependency and environment management

## Project Structure
financial_researcher/

├── src/financial_researcher/

│   ├── config/

│   │   ├── agents.yaml      # Agent role/goal/backstory definitions

│   │   └── tasks.yaml       # Task descriptions and dependencies

│   ├── tools/

│   │   └── custom_tool.py   # Custom live stock data tool (yfinance)

│   ├── crew.py               # Agent/task/crew wiring

│   └── main.py               # Entry point — handles user input and execution

├── output/                   # Generated reports (per company)

├── pyproject.toml

└── README.md

## Setup & Installation

**Prerequisites:** Python 3.10–3.13, [uv](https://docs.astral.sh/uv/)

```bash
# Clone the repo
git clone https://github.com/<your-username>/financial_researcher.git
cd financial_researcher

# Install dependencies
crewai install
```

Create a `.env` file in the project root with your API keys:
OPENAI_API_KEY=your_openai_key_here

SERPER_API_KEY=your_serper_key_here

- Get an OpenAI key at [platform.openai.com](https://platform.openai.com)
- Get a free Serper key (2,500 free searches) at [serper.dev](https://serper.dev)

## Usage

```bash
crewai run
```

You'll be prompted to enter how many companies to research, followed by each company's name and ticker symbol:
How many companies do you want to research? 2
Company 1:

Enter the company name (e.g., Apple): Apple

Enter the stock ticker symbol (e.g., AAPL): AAPL
Company 2:

Enter the company name (e.g., Apple): Tesla

Enter the stock ticker symbol (e.g., AAPL): TSLA

Reports are saved to `output/{TICKER}_report.md`.

## Sample Output

See [`output/sample_report.md`](output/sample_report.md) for a full example report on Apple Inc.

## Known Limitations & Future Improvements

This project is functional end-to-end, but I'm actively aware of (and improving) a few things:

- **Ticker symbols must be entered manually** - there's currently no automatic company-name-to-ticker resolution. A future version could add a lookup tool for this.
- **Source date consistency** - since the researcher pulls from both live web search and live financial data, occasionally older cached search results can surface alongside current data. Planned fix: enforce recency filtering on search results.
- **Compliance language enforcement** - the analyst is currently *instructed* (not strictly enforced) to include a disclaimer that the report shouldn't be used for trading decisions. A planned improvement is moving to a structured Pydantic output schema with a required disclaimer field, rather than relying purely on prompt instruction-following.
- **Sequential execution** - companies are currently researched one at a time. For larger batches, this could be parallelized using CrewAI's async task execution.

## What This Project Demonstrates

- Multi-agent system design and orchestration (role-based agent collaboration, not a single monolithic LLM call)
- Custom tool development with typed Pydantic schemas and defensive error handling
- Prompt engineering - structured task decomposition for consistent, complete outputs
- Practical debugging of Python packaging/environment issues in a real dev workflow
- Awareness of LLM reliability limitations and a concrete plan to address them
