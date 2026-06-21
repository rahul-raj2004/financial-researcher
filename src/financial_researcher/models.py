# src/financial_researcher/models.py
from pydantic import BaseModel, Field


class CompanyReport(BaseModel):
    """Structured schema for a company financial analysis report."""

    company_name: str = Field(..., description="Name of the company analyzed")
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