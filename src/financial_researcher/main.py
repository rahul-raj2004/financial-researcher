#!/usr/bin/env python
# src/financial_researcher/main.py
import os
from financial_researcher.crew import ResearchCrew
from financial_researcher.models import CompanyReport

os.makedirs('output', exist_ok=True)


def format_report_as_markdown(report: CompanyReport) -> str:
    """Convert the validated structured report into a polished markdown document."""
    return f"""# Financial Report: {report.company_name}

## Executive Summary
{report.executive_summary}

## Current Status & Financial Health
{report.current_status}

## Historical Performance
{report.historical_performance}

## Challenges & Opportunities
{report.challenges_and_opportunities}

## Recent News & Events
{report.recent_news}

## Future Outlook
{report.future_outlook}

---

**Disclaimer:** {report.disclaimer}
"""


def run():
    """
    Run the research crew for multiple companies, one at a time.
    """
    num_companies = int(input("How many companies do you want to research? "))

    companies = []
    for i in range(num_companies):
        print(f"\nCompany {i + 1}:")
        company = input("  Enter the company name (e.g., Apple): ").strip()
        ticker = input("  Enter the stock ticker symbol (e.g., AAPL): ").strip().upper()
        companies.append({'company': company, 'ticker': ticker})

    for info in companies:
        print(f"\n\n{'='*60}")
        print(f"Researching {info['company']} ({info['ticker']})...")
        print(f"{'='*60}\n")

        result = ResearchCrew().crew().kickoff(inputs=info)

        # result.pydantic is a validated CompanyReport — disclaimer is GUARANTEED present
        report_markdown = format_report_as_markdown(result.pydantic)

        final_path = f"output/{info['ticker']}_report.md"
        with open(final_path, "w") as f:
            f.write(report_markdown)

        print(f"\nReport for {info['company']} saved to: {final_path}")

    print("\n\nAll reports complete!")


if __name__ == "__main__":
    run()