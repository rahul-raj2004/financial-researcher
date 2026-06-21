# src/financial_researcher/models.py
from pydantic import BaseModel, Field


class CompanyReport(BaseModel):
    """Structured schema for a company financial analysis report."""

    company_name: str = Field(..., description="Name of the company analyzed")
    ticker: str = Field(..., description="Stock ticker symbol of the company")
    current_price: float = Field(..., description="Current stock price in USD")
    market_cap: float = Field(..., description="Market capitalization in USD")
    pe_ratio: float = Field(..., description="Price-to-earnings (P/E) ratio")
    fifty_two_week_high: float = Field(..., description="52-week high stock price")
    fifty_two_week_low: float = Field(..., description="52-week low stock price")
    executive_summary: str = Field(..., description="A concise executive summary of the report")
    current_status: str = Field(
        ..., description="Current company status and financial health, including key metrics"
    )
    historical_performance: str = Field(..., description="Summary of historical company performance")
    challenges_and_opportunities: str = Field(
        ..., description="Major challenges and opportunities facing the company"
    )
    recent_news: str = Field(..., description="Recent news and events relevant to the company")
    future_outlook: str = Field(..., description="Future outlook and potential developments")
    disclaimer: str = Field(
        ...,
        min_length=20,
        description=(
            "A mandatory disclaimer stating that this report is for informational "
            "purposes only and should not be used as the basis for trading or "
            "investment decisions."
        )
    )