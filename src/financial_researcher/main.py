#!/usr/bin/env python
# src/financial_researcher/main.py
import os
import csv
from financial_researcher.crew import ResearchCrew
from financial_researcher.models import CompanyReport

os.makedirs('output', exist_ok=True)


def format_report_as_markdown(report: CompanyReport) -> str:
    """Convert the validated structured report into a polished markdown document."""
    return f"""# Financial Report: {report.company_name} ({report.ticker})

## Key Metrics
- **Current Price:** ${report.current_price}
- **Market Cap:** ${report.market_cap:,.0f}
- **P/E Ratio:** {report.pe_ratio}
- **52-Week High:** ${report.fifty_two_week_high}
- **52-Week Low:** ${report.fifty_two_week_low}

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


def save_summary_csv(reports: list[CompanyReport]) -> str:
    """Write all collected company reports into a single BI-ready CSV file."""
    csv_path = "output/companies_summary.csv"
    with open(csv_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "Company", "Ticker", "Current Price", "Market Cap",
            "P/E Ratio", "52 Week High", "52 Week Low"
        ])
        for r in reports:
            writer.writerow([
                r.company_name, r.ticker, r.current_price, r.market_cap,
                r.pe_ratio, r.fifty_two_week_high, r.fifty_two_week_low
            ])
    return csv_path


def run():
    """
    Run the research crew for multiple companies, one at a time,
    and produce both individual reports and a combined BI-ready CSV.
    """
    num_companies = int(input("How many companies do you want to research? "))

    companies = []
    for i in range(num_companies):
        print(f"\nCompany {i + 1}:")
        company = input("  Enter the company name (e.g., Apple): ").strip()
        ticker = input("  Enter the stock ticker symbol (e.g., AAPL): ").strip().upper()
        companies.append({'company': company, 'ticker': ticker})

    all_reports = []

    for info in companies:
        print(f"\n\n{'='*60}")
        print(f"Researching {info['company']} ({info['ticker']})...")
        print(f"{'='*60}\n")

        result = ResearchCrew().crew().kickoff(inputs=info)
        report_data = result.pydantic
        all_reports.append(report_data)

        report_markdown = format_report_as_markdown(report_data)
        final_path = f"output/{info['ticker']}_report.md"
        with open(final_path, "w") as f:
            f.write(report_markdown)

        print(f"\nReport for {info['company']} saved to: {final_path}")

    csv_path = save_summary_csv(all_reports)
    print(f"\n\nBI-ready summary CSV saved to: {csv_path}")
    print("\nAll reports complete!")


if __name__ == "__main__":
    run()