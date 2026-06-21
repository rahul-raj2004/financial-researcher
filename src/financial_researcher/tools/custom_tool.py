from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import yfinance as yf


class StockDataToolInput(BaseModel):
    """Input schema for StockDataTool."""
    ticker: str = Field(..., description="The stock ticker symbol, e.g. AAPL for Apple")


class StockDataTool(BaseTool):
    name: str = "Stock Financial Data Lookup"
    description: str = (
        "Fetches real-time stock data for a given ticker symbol, including current price, "
        "market cap, P/E ratio, and 52-week high/low. Use this tool to get accurate, "
        "up-to-date quantitative figures instead of relying on web search results, "
        "which may contain outdated numbers."
    )
    args_schema: Type[BaseModel] = StockDataToolInput

    def _run(self, ticker: str) -> str:
        try:
            stock = yf.Ticker(ticker)
            info = stock.info

            data = {
                "Company Name": info.get("longName", "N/A"),
                "Current Price": info.get("currentPrice", "N/A"),
                "Market Cap": info.get("marketCap", "N/A"),
                "P/E Ratio": info.get("trailingPE", "N/A"),
                "52 Week High": info.get("fiftyTwoWeekHigh", "N/A"),
                "52 Week Low": info.get("fiftyTwoWeekLow", "N/A"),
                "Revenue (TTM)": info.get("totalRevenue", "N/A"),
                "Profit Margin": info.get("profitMargins", "N/A"),
            }

            result = f"Live financial data for {ticker} (retrieved directly from Yahoo Finance):\n"
            for key, value in data.items():
                result += f"- {key}: {value}\n"

            return result

        except Exception as e:
            return f"Error fetching stock data for {ticker}: {str(e)}"