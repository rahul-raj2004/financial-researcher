#!/usr/bin/env python
# src/financial_researcher/main.py
import os
import shutil
from financial_researcher.crew import ResearchCrew

os.makedirs('output', exist_ok=True)

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

        # Rename the generic report.md so it isn't overwritten
        # by the next company's run
        final_path = f"output/{info['ticker']}_report.md"
        shutil.move("output/report.md", final_path)

        print(f"\nReport for {info['company']} saved to: {final_path}")

    print("\n\nAll reports complete!")

if __name__ == "__main__":
    run()