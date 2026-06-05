"""
yahoo_finance_service.py
------------------------
Handles stock and crypto market data retrieval.

Purpose:
- Current price
- Trend
- Daily change
- 7-day historical chart data
- Momentum support metrics
"""

import yfinance as yf


class YahooFinanceService:
    """
    Yahoo Finance intelligence service.
    """

    @staticmethod
    def get_stock_data(ticker: str) -> dict:
        """
        Fetch stock/crypto market data.
        """

        try:
            stock = yf.Ticker(ticker)

            week_history = stock.history(period="7d")

            if week_history.empty or len(week_history) < 2:
                return {
                    "status": "error",
                    "message": f"No market data found for {ticker}."
                }

            current_price = float(
                round(week_history["Close"].iloc[-1], 2)
            )

            previous_price = float(
                round(week_history["Close"].iloc[-2], 2)
            )

            week_start_price = float(
                round(week_history["Close"].iloc[0], 2)
            )

            price_change = float(
                round(current_price - previous_price, 2)
            )

            daily_change_percent = float(
                round(
                    ((current_price - previous_price) / previous_price) * 100,
                    2
                )
            )

            weekly_change_percent = float(
                round(
                    ((current_price - week_start_price) / week_start_price) * 100,
                    2
                )
            )

            trend = "up" if current_price > previous_price else "down"

            historical_prices = []

            for index, row in week_history.iterrows():
                historical_prices.append(
                    {
                        "date": str(index).split(" ")[0],
                        "close": float(round(row["Close"], 2))
                    }
                )

            return {
                "status": "success",
                "ticker": ticker,
                "current_price": current_price,
                "previous_price": previous_price,
                "price_change": price_change,
                "daily_change_percent": daily_change_percent,
                "weekly_change_percent": weekly_change_percent,
                "trend": trend,
                "historical_data": historical_prices
            }

        except Exception as error:
            return {
                "status": "error",
                "message": str(error)
            }