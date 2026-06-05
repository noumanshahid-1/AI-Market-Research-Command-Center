"""
components.py
-------------
Reusable UI components for Streamlit dashboard.

Purpose:
- Modular design
- Cleaner dashboard code
- Consistent rendering
"""

import streamlit as st


def render_header():
    """
    Premium terminal hero header.
    """

    import streamlit as st

    html = '<div style="position:relative;overflow:hidden;padding:2.25rem 2.35rem;border-radius:32px;background:linear-gradient(135deg,rgba(15,23,42,0.96),rgba(30,41,59,0.82),rgba(88,28,135,0.50));border:1px solid rgba(148,163,184,0.18);box-shadow:0 24px 70px rgba(0,0,0,0.40);margin-bottom:1.8rem;"><div style="position:absolute;right:-80px;top:-85px;width:250px;height:250px;background:radial-gradient(circle,rgba(168,85,247,0.48),transparent 65%);"></div><div style="position:absolute;left:-90px;bottom:-90px;width:240px;height:240px;background:radial-gradient(circle,rgba(37,99,235,0.28),transparent 65%);"></div><div style="position:relative;z-index:1;"><div style="display:inline-flex;align-items:center;gap:0.45rem;padding:0.42rem 0.85rem;border-radius:999px;background:rgba(255,255,255,0.09);border:1px solid rgba(255,255,255,0.10);color:#bfdbfe;font-size:0.76rem;font-weight:950;letter-spacing:0.85px;text-transform:uppercase;margin-bottom:0.95rem;"><span style="width:8px;height:8px;border-radius:999px;background:#22c55e;box-shadow:0 0 14px rgba(34,197,94,0.85);display:inline-block;"></span> Agentic AI Market Terminal</div><h1 style="margin:0;color:white;font-size:3.05rem;font-weight:950;letter-spacing:-1.5px;line-height:1.05;">AI Market Research Command Center</h1><div style="margin-top:0.9rem;color:#cbd5e1;font-size:1.08rem;line-height:1.7;max-width:900px;">Multi-agent intelligence for stocks, news, product trends, sentiment, comparison analytics, sector heatmaps, predictive signals, and strategic market decisions.</div><div style="display:flex;flex-wrap:wrap;gap:0.65rem;margin-top:1.25rem;"><span style="padding:0.38rem 0.75rem;border-radius:999px;background:rgba(37,99,235,0.18);color:#bfdbfe;font-size:0.78rem;font-weight:850;">Stocks</span><span style="padding:0.38rem 0.75rem;border-radius:999px;background:rgba(124,58,237,0.18);color:#ddd6fe;font-size:0.78rem;font-weight:850;">News Sentiment</span><span style="padding:0.38rem 0.75rem;border-radius:999px;background:rgba(16,185,129,0.16);color:#a7f3d0;font-size:0.78rem;font-weight:850;">Product Trends</span><span style="padding:0.38rem 0.75rem;border-radius:999px;background:rgba(219,39,119,0.14);color:#fbcfe8;font-size:0.78rem;font-weight:850;">Heatmaps</span></div></div></div>'

    st.markdown(html, unsafe_allow_html=True)

def render_search_bar():
    import streamlit as st

    st.markdown(
        '<div class="command-label">Market Command</div>',
        unsafe_allow_html=True
    )

    return st.text_input(
        "Market Command",
        placeholder="Apple stock and latest AI news | Top AI stocks | AI sector heatmap | Apple vs Microsoft",
        label_visibility="collapsed",
        key="market_command_input"
    )
def render_summary(summary: str):
    """
    Premium AI market insight summary banner.
    """

    import streamlit as st

    if not summary:
        return

    st.markdown(
        f"""
        <div class="summary-pro-card">
            <div class="summary-accent"></div>
            <div class="summary-content">
                <div class="summary-label">AI Market Insight</div>
                <div class="summary-text">{summary}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


def render_stock_card(stock_data):
    """
    Premium stock intelligence card using native Streamlit layout.
    """

    import streamlit as st

    if not stock_data or stock_data.get("status") != "success":
        return

    ticker = stock_data.get("ticker", "N/A")
    current_price = stock_data.get("current_price", "N/A")
    previous_price = stock_data.get("previous_price", "N/A")
    price_change = float(stock_data.get("price_change", 0))
    trend = stock_data.get("trend", "neutral")

    if trend == "up":
        trend_text = "▲ Uptrend"
        delta_text = f"+${abs(price_change)}"
    elif trend == "down":
        trend_text = "▼ Downtrend"
        delta_text = f"-${abs(price_change)}"
    else:
        trend_text = "Stable"
        delta_text = "$0.00"

    st.subheader("Stock Intelligence")

    with st.container():
        st.markdown(
            f"""
            <div class="stock-intel-card">
                <div class="stock-card-top">
                    <div>
                        <div class="stock-ticker">{ticker}</div>
                        <div class="stock-label">Tracked Asset</div>
                    </div>
                    <div class="stock-trend-pill">{trend_text}</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Current Price", f"${current_price}")

        with col2:
            st.metric("Daily Change", delta_text)

        with col3:
            st.metric("Previous Close", f"${previous_price}")

def render_news_card(news_data):
    """
    Premium ranked news intelligence cards.
    """

    import streamlit as st

    articles = news_data.get("articles", [])

    if not articles:
        return

    st.subheader("Latest News Intelligence")

    for idx, article in enumerate(articles, start=1):

        title = article.get("title", "Untitled")
        description = article.get("description", "No description available.")
        source = article.get("source", "Unknown Source")
        url = article.get("url", "#")

        sentiment = article.get("sentiment", {})
        sentiment_label = sentiment.get("label", "neutral").title()
        sentiment_class = sentiment_label.lower()

        relevance = article.get("relevance", max(100 - ((idx - 1) * 8), 60))

        card_html = f"""
        <div class="news-card">
            <div class="news-topline">
                <span class="news-rank">#{idx} · {relevance}% relevance</span>
                <span class="news-source">{source}</span>
            </div>
            <div class="news-title">{title}</div>
            <div class="news-description">{description}</div>
            <div class="news-footer">
                <span class="article-sentiment {sentiment_class}">{sentiment_label}</span>
                <a href="{url}" target="_blank" class="news-link">Read Full Coverage →</a>
            </div>
        </div>
        """

        st.markdown(card_html, unsafe_allow_html=True)

def render_product_card(product_data):
    """
    Premium product intelligence section.
    """

    import streamlit as st

    if not product_data or product_data.get("status") != "success":
        return

    trend = product_data.get("trend", "stable").title()
    score = round(float(product_data.get("average_interest", 0)), 2)
    products = product_data.get("top_products", [])

    if score >= 80:
        strength_label = "High Demand"
        strength_class = "product-strong"
    elif score >= 60:
        strength_label = "Moderate Demand"
        strength_class = "product-moderate"
    else:
        strength_label = "Emerging Demand"
        strength_class = "product-low"

    st.subheader("Product Intelligence")

    st.markdown(
        f"""
        <div class="product-intel-panel">
            <div>
                <div class="product-panel-label">Category Trend</div>
                <div class="product-panel-value">{trend}</div>
            </div>
            <div>
                <div class="product-panel-label">Demand Strength</div>
                <div class="product-demand-pill {strength_class}">{strength_label}</div>
            </div>
            <div>
                <div class="product-panel-label">Interest Score</div>
                <div class="product-panel-score">{score}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    if products:
        st.markdown("### Top Product Movers")

        cols = st.columns(min(3, len(products)))

        for index, product in enumerate(products):
            product_score = max(score - (index * 7), 10)
            width = min(100, max(10, product_score))

            with cols[index % len(cols)]:
                st.markdown(
                    f"""
                    <div class="product-mover-card">
                        <div class="product-mover-rank">#{index + 1}</div>
                        <div class="product-mover-name">{product}</div>
                        <div class="product-heatbar-bg">
                            <div class="product-heatbar-fill" style="width:{width}%;"></div>
                        </div>
                        <div class="product-mover-score">{round(product_score, 2)} strength</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

def render_sentiment(sentiment_data):
    """
    Render sentiment intelligence.
    """

    import streamlit as st

    if not sentiment_data:
        return

    label = sentiment_data.get(
        "label",
        "neutral"
    ).capitalize()

    score = sentiment_data.get(
        "score",
        0
    )

    st.write(
        f"**Market Sentiment:** {label} ({score})"
    )


def render_strategy(strategy_text):
    """
    Premium strategist insight card with readable executive sections.
    """

    import streamlit as st
    import re

    if not strategy_text:
        return

    clean_text = strategy_text.replace("Executive View:", "").strip()

    ticker_match = re.search(r"\b[A-Z]{2,6}(?:-USD)?\b", strategy_text)
    ticker = ticker_match.group(0) if ticker_match else "Market"

    lower_text = strategy_text.lower()

    if "positive" in lower_text or "strong" in lower_text or "gain" in lower_text:
        outlook = "Positive"
    elif "weakness" in lower_text or "decline" in lower_text or "pressure" in lower_text:
        outlook = "Caution"
    else:
        outlook = "Neutral"

    if "manageable" in lower_text:
        risk = "Manageable"
    elif "bearish" in lower_text or "pressure" in lower_text or "risk" in lower_text:
        risk = "Elevated"
    else:
        risk = "Moderate"

    # Split long strategy into readable points
    sentences = [
        sentence.strip()
        for sentence in clean_text.split(".")
        if sentence.strip()
    ]

    primary_signal = sentences[0] if len(sentences) > 0 else "No primary signal available"
    risk_signal = sentences[-1] if len(sentences) > 1 else "Risk signal not clearly detected"

    highlight_terms = [
        "positive price momentum",
        "short-term weakness",
        "daily gain",
        "daily decline",
        "strong",
        "weakening",
        "bullish",
        "bearish",
        "mixed",
        "price pressure",
        "manageable",
        "risk"
    ]

    def highlight(text):
        for term in highlight_terms:
            text = text.replace(
                term,
                f'<span class="strategy-highlight">{term}</span>'
            )
        return text

    primary_signal = (primary_signal)
    risk_signal = (risk_signal)

    html = f'<div class="strategy-pro-card"><div class="strategy-glow"></div><div class="strategy-header-row"><div class="strategy-orb">AI</div><div class="strategy-header-text"><div class="strategy-title">Executive Market Interpretation</div><div class="strategy-subtitle">Generated by strategist intelligence</div></div></div><div class="strategy-signal-row"><span class="strategy-chip">Asset: {ticker}</span><span class="strategy-chip">Outlook: {outlook}</span><span class="strategy-chip">Risk: {risk}</span></div><div class="strategy-brief-grid"><div class="strategy-mini-panel"><div class="strategy-mini-label">Primary Signal</div><div class="strategy-mini-text">{primary_signal}.</div></div><div class="strategy-mini-panel"><div class="strategy-mini-label">Risk View</div><div class="strategy-mini-text">{risk_signal}.</div></div></div></div>'

    st.markdown(html, unsafe_allow_html=True)
    
def render_stock_chart(stock_data):
    """
    Render premium dark-themed stock chart.
    """

    import streamlit as st
    import pandas as pd
    import plotly.express as px

    historical_data = stock_data.get("historical_data", [])

    if not historical_data:
        return

    df = pd.DataFrame(historical_data)

    ticker = stock_data.get("ticker", "Asset")
    trend = stock_data.get("trend", "neutral")

    line_color = "#22c55e" if trend == "up" else "#ef4444"

    fig = px.line(
        df,
        x="date",
        y="close",
        title=f"{ticker} · 7-Day Price Trend"
    )

    fig.update_traces(
        line=dict(
            color=line_color,
            width=3
        ),
        mode="lines+markers",
        marker=dict(
            size=7,
            color=line_color
        )
    )

    fig.update_layout(
        height=420,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(15,23,42,0.55)",
        font=dict(color="#e2e8f0"),
        title=dict(
            font=dict(size=22, color="white"),
            x=0.02
        ),
        xaxis=dict(
            title="",
            gridcolor="rgba(255,255,255,0.06)",
            zerolinecolor="rgba(255,255,255,0.08)"
        ),
        yaxis=dict(
            title="Close Price",
            gridcolor="rgba(255,255,255,0.06)",
            zerolinecolor="rgba(255,255,255,0.08)"
        ),
        margin=dict(l=20, r=20, t=60, b=20)
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

def render_kpi_cards(results):
    """
    Premium animated KPI command cards.
    """

    import streamlit as st

    stock = results.get("stock")
    news = results.get("news")
    product = results.get("product")

    # -------------------------
    # Stock KPI
    # -------------------------
    stock_price = "—"
    stock_subtext = "No stock data"
    stock_class = "neutral"
    stock_icon = "📈"

    if stock:
        price = stock.get("current_price", "—")
        change = stock.get("price_change", 0)
        trend = stock.get("trend", "neutral")

        stock_price = f"${price}"

        if trend == "up":
            stock_subtext = f"▲ +${abs(change)}"
            stock_class = "positive"
        elif trend == "down":
            stock_subtext = f"▼ -${abs(change)}"
            stock_class = "negative"
        else:
            stock_subtext = "Stable"
            stock_class = "neutral"

    # -------------------------
    # News KPI
    # -------------------------
    news_value = "—"
    news_subtext = "No news signal"
    news_class = "neutral"
    news_icon = "📰"

    if news:
        articles = news.get("articles", [])
        sentiment = news.get("sentiment", {})
        label = sentiment.get("label", "neutral")

        news_value = str(len(articles))
        news_subtext = label.title()

        if label == "bullish":
            news_class = "positive"
        elif label == "bearish":
            news_class = "negative"
        else:
            news_class = "neutral"

    # -------------------------
    # Product KPI
    # -------------------------
    product_value = "—"
    product_subtext = "No trend signal"
    product_class = "neutral"
    product_icon = "🚀"

    if product:
        score = float(product.get("average_interest", 0))
        trend = product.get("trend", "stable")

        product_value = str(round(score, 2))

        if trend == "growing":
            product_subtext = "Growing Demand"
            product_class = "positive"
        elif trend == "declining":
            product_subtext = "Weakening Demand"
            product_class = "negative"
        else:
            product_subtext = "Stable Demand"
            product_class = "neutral"

    metrics = [
        ("Stock Price", stock_price, stock_subtext, stock_icon, stock_class),
        ("News Signal", news_value, news_subtext, news_icon, news_class),
        ("Trend Score", product_value, product_subtext, product_icon, product_class)
    ]

    cols = st.columns(3)

    for col, metric in zip(cols, metrics):
        title, value, subtext, icon, state_class = metric

        with col:
            st.markdown(
                f"""
                <div class="command-kpi-card {state_class}">
                    <div class="kpi-top-row">
                        <span class="command-kpi-icon">{icon}</span>
                        <span class="command-kpi-state">{subtext}</span>
                    </div>
                    <div class="command-kpi-title">{title}</div>
                    <div class="command-kpi-value">{value}</div>
                </div>
                """,
                unsafe_allow_html=True
            )
def render_product_chart(product_data):
    """
    Render premium dark-themed product strength chart.
    """

    import streamlit as st
    import pandas as pd
    import plotly.express as px

    products = product_data.get("top_products", [])

    if not products:
        return

    base_score = float(product_data.get("average_interest", 50))

    values = []

    for index, product in enumerate(products):
        values.append(
            {
                "product": product,
                "score": max(base_score - (index * 7), 15)
            }
        )

    df = pd.DataFrame(values)

    fig = px.bar(
        df,
        x="score",
        y="product",
        orientation="h",
        title="Product Momentum Strength"
    )

    fig.update_traces(
        marker=dict(
            color=df["score"],
            colorscale="Viridis"
        )
    )

    fig.update_layout(
        height=360,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(15,23,42,0.55)",
        font=dict(color="#e2e8f0"),
        title=dict(
            font=dict(size=22, color="white"),
            x=0.02
        ),
        xaxis=dict(
            title="Strength Score",
            gridcolor="rgba(255,255,255,0.06)",
            range=[0, 100]
        ),
        yaxis=dict(
            title="",
            gridcolor="rgba(255,255,255,0.03)"
        ),
        margin=dict(l=20, r=20, t=60, b=20)
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )
def render_watchlist_button(stock_data):
    """
    Add stock to persistent watchlist.
    """

    import streamlit as st

    if not stock_data:
        return

    ticker = stock_data.get(
        "ticker"
    )

    if not ticker:
        return

    button_key = (
        f"watchlist_{ticker}"
    )

    if st.button(
        f"Add {ticker} to Watchlist",
        key=button_key
    ):

        if (
            ticker
            not in st.session_state.watchlist
        ):

            st.session_state.watchlist.append(
                ticker
            )

            st.session_state.watchlist = list(
                dict.fromkeys(
                    st.session_state.watchlist
                )
            )

            st.success(
                f"{ticker} added to watchlist."
            )

        else:
            st.info(
                f"{ticker} already in watchlist."
            )

def calculate_market_score(results):
    """
    Calculate a balanced Market Opportunity Score out of 100.
    """

    score = 60

    stock = results.get("stock")
    news = results.get("news")
    product = results.get("product")

    if stock:
        trend = stock.get("trend", "neutral")
        change = float(stock.get("price_change", 0))

        if trend == "up":
            score += 12
        elif trend == "down":
            if abs(change) <= 1:
                score -= 4
            else:
                score -= 10

    if news:
        sentiment = news.get("sentiment", {}).get("label", "neutral")

        if sentiment == "bullish":
            score += 12
        elif sentiment == "bearish":
            score -= 12
        else:
            score += 2

    if product:
        trend = product.get("trend", "stable")
        interest = float(product.get("average_interest", 0))

        if trend == "growing":
            score += 10
        elif trend == "declining":
            score -= 8

        if interest >= 80:
            score += 8
        elif interest >= 60:
            score += 4
        elif interest < 40:
            score -= 5

    return max(0, min(100, score))

def render_market_score(results):
    """
    Render Market Opportunity Score and sentiment gauge.
    """

    import streamlit as st

    score = calculate_market_score(results)

    news = results.get("news")
    sentiment_label = "Neutral"

    if news:
        sentiment_label = (
            news.get("sentiment", {})
            .get("label", "neutral")
            .title()
        )

    if score >= 75:
        score_class = "score-strong"
        score_label = "Strong Opportunity"
    elif score >= 55:
        score_class = "score-moderate"
        score_label = "Moderate Opportunity"
    else:
        score_class = "score-caution"
        score_label = "Caution Zone"

    sentiment_class = sentiment_label.lower()

    html = f"""
    <div class="market-score-panel">
        <div class="market-score-left">
            <div class="score-label">Market Opportunity Score</div>
            <div class="score-value {score_class}">{score}/100</div>
            <div class="score-subtext">{score_label}</div>
        </div>
        <div class="market-score-right">
            <div class="score-label">News Sentiment</div>
            <div class="sentiment-pill {sentiment_class}">{sentiment_label}</div>
        </div>
    </div>
    """

    st.markdown(html, unsafe_allow_html=True)


def render_sentiment_panel(news_data):
    """
    Premium sentiment intelligence panel.
    """

    import streamlit as st

    if not news_data or news_data.get("status") != "success":
        return

    articles = news_data.get("articles", [])
    overall = news_data.get("sentiment", {})

    overall_label = overall.get("label", "neutral").title()
    overall_score = overall.get("score", 0)

    bullish_count = 0
    bearish_count = 0
    neutral_count = 0

    for article in articles:
        label = article.get("sentiment", {}).get("label", "neutral")

        if label == "bullish":
            bullish_count += 1
        elif label == "bearish":
            bearish_count += 1
        else:
            neutral_count += 1

    total_articles = max(len(articles), 1)

    confidence = round(
        max(bullish_count, bearish_count, neutral_count)
        / total_articles
        * 100
    )

    if overall_label.lower() == "bullish":
        sentiment_class = "sentiment-positive"
    elif overall_label.lower() == "bearish":
        sentiment_class = "sentiment-negative"
    else:
        sentiment_class = "sentiment-neutral"

    html = f'<div class="sentiment-panel"><div class="sentiment-panel-header"><div><div class="sentiment-panel-title">Market Sentiment Intelligence</div><div class="sentiment-panel-subtitle">Aggregated from ranked news signals</div></div><div class="sentiment-overall {sentiment_class}">{overall_label}</div></div><div class="sentiment-grid"><div class="sentiment-stat"><div class="sentiment-stat-value">{bullish_count}</div><div class="sentiment-stat-label">Bullish Signals</div></div><div class="sentiment-stat"><div class="sentiment-stat-value">{neutral_count}</div><div class="sentiment-stat-label">Neutral Signals</div></div><div class="sentiment-stat"><div class="sentiment-stat-value">{bearish_count}</div><div class="sentiment-stat-label">Bearish Signals</div></div><div class="sentiment-stat"><div class="sentiment-stat-value">{confidence}%</div><div class="sentiment-stat-label">Signal Confidence</div></div></div><div class="sentiment-score-line">Sentiment score: {overall_score}</div></div>'

    st.markdown(html, unsafe_allow_html=True)

def calculate_ai_confidence(results):
    """
    Calculate AI confidence based on available signals.
    Adjusted for stock, news, product, and mixed-agent queries.
    """

    stock = results.get("stock")
    news = results.get("news")
    product = results.get("product")
    comparison = results.get("comparison")
    screener = results.get("screener")
    heatmap = results.get("heatmap")

    # Macro views should not rely on this panel normally
    if comparison or screener or heatmap:
        return 70

    confidence = 35

    # STOCK CONFIDENCE
    if stock and stock.get("status") == "success":
        confidence += 25

        daily = abs(float(stock.get("daily_change_percent", 0)))
        weekly = abs(float(stock.get("weekly_change_percent", 0)))

        if daily >= 1:
            confidence += 5

        if weekly >= 3:
            confidence += 8

    # NEWS CONFIDENCE
    if news and news.get("status") == "success":
        articles = news.get("articles", [])
        confidence += min(len(articles) * 4, 18)

        sentiment_score = abs(
            float(
                news.get("sentiment", {}).get("score", 0)
            )
        )

        if sentiment_score >= 0.15:
            confidence += 8
        elif sentiment_score >= 0.05:
            confidence += 4

    # PRODUCT CONFIDENCE
    if product and product.get("status") == "success":
        score = float(
            product.get(
                "average_interest",
                0
            )
        )

        trend = product.get(
            "trend",
            "stable"
        )

        confidence += 20

        if score >= 85:
            confidence += 20
        elif score >= 70:
            confidence += 15
        elif score >= 55:
            confidence += 10

        if trend == "growing":
            confidence += 8
        elif trend == "declining":
            confidence -= 5

        if product.get("top_products"):
            confidence += 5

    return max(0, min(95, confidence))

def render_ai_confidence(results):
    """
    Render AI confidence panel.
    """

    import streamlit as st

    confidence = calculate_ai_confidence(results)

    if confidence >= 80:
        label = "High Confidence"
        css_class = "confidence-high"
    elif confidence >= 60:
        label = "Moderate Confidence"
        css_class = "confidence-medium"
    else:
        label = "Low Confidence"
        css_class = "confidence-low"

    html = f'<div class="ai-confidence-panel"><div><div class="confidence-title">AI Confidence Score</div><div class="confidence-subtitle">Based on signal availability, sentiment strength, and agent agreement</div></div><div class="confidence-score {css_class}">{confidence}%</div><div class="confidence-label {css_class}">{label}</div></div>'

    st.markdown(html, unsafe_allow_html=True)

def render_comparison_card(comparison_data):
    """
    Render premium comparison intelligence.
    """

    import streamlit as st

    if not comparison_data or comparison_data.get("status") != "success":
        return

    assets = comparison_data.get("assets", [])

    valid_assets = [
        asset for asset in assets
        if asset.get("status") == "success"
    ]

    if len(valid_assets) != 2:
        st.warning("Comparison data is incomplete.")
        return

    left = valid_assets[0]
    right = valid_assets[1]

    def trend_class(asset):
        if asset.get("trend") == "up":
            return "comparison-positive"
        if asset.get("trend") == "down":
            return "comparison-negative"
        return "comparison-neutral"

    winner = "Balanced"

    if left.get("trend") == "up" and right.get("trend") == "down":
        winner = left.get("ticker")
    elif right.get("trend") == "up" and left.get("trend") == "down":
        winner = right.get("ticker")
    elif left.get("price_change", 0) > right.get("price_change", 0):
        winner = left.get("ticker")
    elif right.get("price_change", 0) > left.get("price_change", 0):
        winner = right.get("ticker")

    st.subheader("Comparison Intelligence")

    html = f'<div class="comparison-panel"><div class="comparison-header"><div><div class="comparison-title">Asset Comparison</div><div class="comparison-subtitle">Side-by-side market momentum analysis</div></div><div class="comparison-winner">Leader: {winner}</div></div><div class="comparison-grid"><div class="comparison-card"><div class="comparison-ticker">{left.get("ticker")}</div><div class="comparison-price">${left.get("current_price")}</div><div class="comparison-change {trend_class(left)}">{left.get("trend").title()} · ${abs(float(left.get("price_change", 0)))}</div></div><div class="comparison-card"><div class="comparison-ticker">{right.get("ticker")}</div><div class="comparison-price">${right.get("current_price")}</div><div class="comparison-change {trend_class(right)}">{right.get("trend").title()} · ${abs(float(right.get("price_change", 0)))}</div></div></div></div>'

    st.markdown(html, unsafe_allow_html=True)

def render_comparison_chart(comparison_data):
    """
    Render premium overlay comparison chart.
    """

    import streamlit as st
    import pandas as pd
    import plotly.graph_objects as go

    if not comparison_data or comparison_data.get("status") != "success":
        return

    assets = comparison_data.get("assets", [])

    valid_assets = [
        asset for asset in assets
        if asset.get("status") == "success"
        and asset.get("historical_data")
    ]

    if len(valid_assets) != 2:
        return

    fig = go.Figure()

    colors = ["#60a5fa", "#a855f7"]

    for index, asset in enumerate(valid_assets):
        ticker = asset.get("ticker", f"Asset {index + 1}")
        history = asset.get("historical_data", [])

        df = pd.DataFrame(history)

        if df.empty:
            continue

        fig.add_trace(
            go.Scatter(
                x=df["date"],
                y=df["close"],
                mode="lines+markers",
                name=ticker,
                line=dict(
                    width=3,
                    color=colors[index]
                ),
                marker=dict(
                    size=7,
                    color=colors[index]
                )
            )
        )

    fig.update_layout(
        height=430,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(15,23,42,0.55)",
        font=dict(color="#e2e8f0"),

        title=dict(
            text="Comparison Price Trend",
            font=dict(
                size=22,
                color="white"
            ),
            x=0.02
        ),

        xaxis=dict(
            title="",
            gridcolor="rgba(255,255,255,0.06)",
            zerolinecolor="rgba(255,255,255,0.08)"
        ),

        yaxis=dict(
            title="Close Price",
            gridcolor="rgba(255,255,255,0.06)",
            zerolinecolor="rgba(255,255,255,0.08)"
        ),

        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),

        margin=dict(
            l=20,
            r=20,
            t=70,
            b=20
        )
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

def render_screener_dashboard(screener_data):
    """
    Render premium grouped stock screener dashboard.
    """

    import streamlit as st

    if not screener_data or screener_data.get("status") != "success":
        return

    title = screener_data.get("basket_title", "Market Screener")
    assets = screener_data.get("assets", [])

    if not assets:
        st.warning("No screener assets available.")
        return

    st.subheader(title)

    leader = assets[0]

    st.markdown(
        f'<div class="screener-leader-card"><div class="screener-leader-label">Current Basket Leader</div><div class="screener-leader-main">{leader.get("ticker")}</div><div class="screener-leader-sub">Momentum Score: {leader.get("momentum_score", 0)}/100 · Daily: {leader.get("daily_change_percent", 0)}% · Weekly: {leader.get("weekly_change_percent", 0)}%</div></div>',
        unsafe_allow_html=True
    )

    cols = st.columns(min(3, len(assets)))

    for index, asset in enumerate(assets):
        ticker = asset.get("ticker", "N/A")
        price = asset.get("current_price", "N/A")
        trend = asset.get("trend", "neutral")
        change = float(asset.get("price_change", 0))
        daily_percent = asset.get("daily_change_percent", 0)
        weekly_percent = asset.get("weekly_change_percent", 0)
        score = asset.get("momentum_score", 0)

        if trend == "up":
            trend_class = "screener-positive"
            trend_label = "▲ Up"
        elif trend == "down":
            trend_class = "screener-negative"
            trend_label = "▼ Down"
        else:
            trend_class = "screener-neutral"
            trend_label = "Stable"

        with cols[index % len(cols)]:
            st.markdown(
                f'<div class="screener-card"><div class="screener-rank">#{index + 1}</div><div class="screener-ticker">{ticker}</div><div class="screener-price">${price}</div><div class="screener-trend {trend_class}">{trend_label} · ${abs(change)}</div><div class="screener-mini-grid"><div><span>Daily</span><strong>{daily_percent}%</strong></div><div><span>Weekly</span><strong>{weekly_percent}%</strong></div></div><div class="screener-score-bg"><div class="screener-score-fill" style="width:{score}%;"></div></div><div class="screener-score-text">Momentum {score}/100</div></div>',
                unsafe_allow_html=True
            )

def render_sector_heatmap(heatmap_data):
    """
    Render premium sector heatmap using Plotly treemap.
    """

    import streamlit as st
    import pandas as pd
    import plotly.express as px

    if not heatmap_data or heatmap_data.get("status") != "success":
        return

    title = heatmap_data.get("sector_title", "Sector Heatmap")
    assets = heatmap_data.get("assets", [])

    if not assets:
        st.warning("No heatmap assets available.")
        return

    st.subheader(title)

    df = pd.DataFrame(assets)

    # Better labels inside each block
    df["label"] = (
        df["ticker"]
        + "<br>"
        + df["daily_change_percent"].astype(str)
        + "%"
        + "<br>$"
        + df["current_price"].astype(str)
    )

    fig = px.treemap(
        df,
        path=["label"],
        values="weight",
        color="daily_change_percent",
        color_continuous_scale=[
            "#ef4444",
            "#1e293b",
            "#22c55e"
        ],
        color_continuous_midpoint=0,
        hover_data={
            "ticker": True,
            "current_price": True,
            "daily_change_percent": True,
            "weekly_change_percent": True,
            "weight": False,
            "label": False
        }
    )

    fig.update_traces(
        textfont=dict(
            size=18,
            color="white"
        ),
        textposition="middle center",
        marker=dict(
            line=dict(
                color="rgba(255,255,255,0.18)",
                width=2
            )
        ),
        hovertemplate=(
            "<b>%{customdata[0]}</b><br>"
            "Price: $%{customdata[1]}<br>"
            "Daily: %{customdata[2]}%<br>"
            "Weekly: %{customdata[3]}%<extra></extra>"
        )
    )

    fig.update_layout(
        height=620,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(2,6,23,0.85)",
        font=dict(
            color="#e2e8f0",
            size=14
        ),
        title=dict(
            text="Sector Momentum Heatmap",
            font=dict(
                size=24,
                color="white"
            ),
            x=0.02
        ),
        coloraxis_showscale=False,
        margin=dict(
            l=10,
            r=10,
            t=70,
            b=10
        )
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

    positive_assets = [
        asset for asset in assets
        if asset.get("daily_change_percent", 0) > 0
    ]

    strongest_asset = max(
        assets,
        key=lambda asset: asset.get("daily_change_percent", 0)
    )

    weakest_asset = min(
        assets,
        key=lambda asset: asset.get("daily_change_percent", 0)
    )

    st.markdown(
        f'<div class="heatmap-summary-grid"><div class="heatmap-summary-card"><div class="heatmap-summary-title">Sector Signal</div><div class="heatmap-summary-text">{len(positive_assets)} of {len(assets)} tracked assets are positive today.</div></div><div class="heatmap-summary-card"><div class="heatmap-summary-title">Strongest Asset</div><div class="heatmap-summary-text">{strongest_asset.get("ticker")} · {strongest_asset.get("daily_change_percent")}%</div></div><div class="heatmap-summary-card"><div class="heatmap-summary-title">Weakest Asset</div><div class="heatmap-summary-text">{weakest_asset.get("ticker")} · {weakest_asset.get("daily_change_percent")}%</div></div></div>',
        unsafe_allow_html=True
    )

def render_screener_chart(screener_data):
    """
    Render premium momentum chart for screener assets.
    """

    import streamlit as st
    import pandas as pd
    import plotly.express as px

    if not screener_data or screener_data.get("status") != "success":
        return

    assets = screener_data.get("assets", [])

    if not assets:
        return

    df = pd.DataFrame(assets)

    fig = px.bar(
        df,
        x="momentum_score",
        y="ticker",
        orientation="h",
        color="momentum_score",
        color_continuous_scale=[
            "#ef4444",
            "#60a5fa",
            "#22c55e"
        ],
        title="Basket Momentum Ranking",
        text="momentum_score"
    )

    fig.update_traces(
        texttemplate="%{text}/100",
        textposition="outside"
    )

    fig.update_layout(
        height=420,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(15,23,42,0.55)",
        font=dict(color="#e2e8f0"),
        title=dict(
            text="Basket Momentum Ranking",
            font=dict(size=22, color="white"),
            x=0.02
        ),
        xaxis=dict(
            title="Momentum Score",
            range=[0, 100],
            gridcolor="rgba(255,255,255,0.06)"
        ),
        yaxis=dict(
            title="",
            categoryorder="total ascending"
        ),
        coloraxis_showscale=False,
        margin=dict(l=20, r=40, t=70, b=20)
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )
def render_screener_strategy(screener_data):
    """
    Render dedicated screener strategy summary.
    """

    import streamlit as st

    if not screener_data or screener_data.get("status") != "success":
        return

    assets = screener_data.get("assets", [])
    title = screener_data.get("basket_title", "Market Screener")

    if not assets:
        return

    leader = assets[0]

    positive_today = [
        asset for asset in assets
        if float(asset.get("daily_change_percent", 0)) > 0
    ]

    weekly_positive = [
        asset for asset in assets
        if float(asset.get("weekly_change_percent", 0)) > 0
    ]

    weakest = min(
        assets,
        key=lambda asset: asset.get("momentum_score", 0)
    )

    outlook = (
        "Constructive"
        if len(positive_today) >= len(assets) / 2
        else "Selective"
    )

    html = f'<div class="screener-strategy-card"><div class="screener-strategy-top"><div class="strategy-orb">AI</div><div><div class="screener-strategy-title">{title} Strategy Brief</div><div class="screener-strategy-subtitle">Generated from basket momentum intelligence</div></div></div><div class="strategy-signal-row"><span class="strategy-chip">Leader: {leader.get("ticker")}</span><span class="strategy-chip">Outlook: {outlook}</span><span class="strategy-chip">Positive Today: {len(positive_today)}/{len(assets)}</span></div><div class="strategy-brief-grid"><div class="strategy-mini-panel"><div class="strategy-mini-label">Basket Leader</div><div class="strategy-mini-text">{leader.get("ticker")} leads this basket with a momentum score of {leader.get("momentum_score", 0)}/100, daily movement of {leader.get("daily_change_percent", 0)}%, and weekly movement of {leader.get("weekly_change_percent", 0)}%.</div></div><div class="strategy-mini-panel"><div class="strategy-mini-label">Risk View</div><div class="strategy-mini-text">{weakest.get("ticker")} is currently the weakest ranked asset with a momentum score of {weakest.get("momentum_score", 0)}/100. {len(weekly_positive)} of {len(assets)} tracked assets remain positive on a weekly basis.</div></div></div></div>'

    st.markdown(html, unsafe_allow_html=True)
def render_screener_brief(screener_data):
    """
    Dedicated screener strategy brief.
    """

    import streamlit as st

    if not screener_data or screener_data.get("status") != "success":
        return

    assets = screener_data.get("assets", [])
    title = screener_data.get("basket_title", "Market Screener")

    if not assets:
        return

    leader = assets[0]

    positive_today = [
        asset for asset in assets
        if float(asset.get("daily_change_percent", 0)) > 0
    ]

    weekly_positive = [
        asset for asset in assets
        if float(asset.get("weekly_change_percent", 0)) > 0
    ]

    weakest = min(
        assets,
        key=lambda asset: asset.get("momentum_score", 0)
    )

    outlook = (
        "Constructive"
        if len(positive_today) >= len(assets) / 2
        else "Selective"
    )

    html = f'<div class="screener-strategy-card"><div class="screener-strategy-top"><div class="strategy-orb">AI</div><div><div class="screener-strategy-title">{title} Strategy Brief</div><div class="screener-strategy-subtitle">Generated from basket momentum intelligence</div></div></div><div class="strategy-signal-row"><span class="strategy-chip">Leader: {leader.get("ticker")}</span><span class="strategy-chip">Outlook: {outlook}</span><span class="strategy-chip">Positive Today: {len(positive_today)}/{len(assets)}</span></div><div class="strategy-brief-grid"><div class="strategy-mini-panel"><div class="strategy-mini-label">Basket Leader</div><div class="strategy-mini-text">{leader.get("ticker")} leads this basket with a momentum score of {leader.get("momentum_score", 0)}/100, daily movement of {leader.get("daily_change_percent", 0)}%, and weekly movement of {leader.get("weekly_change_percent", 0)}%.</div></div><div class="strategy-mini-panel"><div class="strategy-mini-label">Risk View</div><div class="strategy-mini-text">{weakest.get("ticker")} is currently the weakest ranked asset with a momentum score of {weakest.get("momentum_score", 0)}/100. {len(weekly_positive)} of {len(assets)} tracked assets remain positive on a weekly basis.</div></div></div></div>'

    st.markdown(html, unsafe_allow_html=True)

def render_predictive_signals(results):
    """
    Render predictive market signal panel.
    """

    import streamlit as st

    stock = results.get("stock")
    news = results.get("news")
    product = results.get("product")
    comparison = results.get("comparison")
    screener = results.get("screener")

    # Avoid predictive panel for macro dashboards for now
    if screener or comparison:
        return

    probability = 50
    risk_points = 0
    explanation = []

    if stock and stock.get("status") == "success":
        daily = float(stock.get("daily_change_percent", 0))
        weekly = float(stock.get("weekly_change_percent", 0))

        if daily > 0:
            probability += 10
            explanation.append("positive daily price action")

        if weekly > 0:
            probability += 15
            explanation.append("positive weekly momentum")

        if daily < 0:
            probability -= 8
            risk_points += 1
            explanation.append("negative daily price action")

        if weekly < 0:
            probability -= 12
            risk_points += 1
            explanation.append("negative weekly momentum")

    if news and news.get("status") == "success":
        sentiment = news.get("sentiment", {}).get("label", "neutral")

        if sentiment == "bullish":
            probability += 12
            explanation.append("bullish news sentiment")

        elif sentiment == "bearish":
            probability -= 12
            risk_points += 1
            explanation.append("bearish news sentiment")

    if product and product.get("status") == "success":
        trend = product.get("trend", "stable")
        score = float(product.get("average_interest", 0))

        if trend == "growing":
            probability += 8
            explanation.append("growing product demand")

        if score >= 80:
            probability += 6
            explanation.append("high demand score")

    probability = max(0, min(100, round(probability)))

    if probability >= 70:
        forecast = "Bullish"
        forecast_class = "predictive-positive"
    elif probability >= 50:
        forecast = "Neutral-Positive"
        forecast_class = "predictive-neutral"
    else:
        forecast = "Cautious"
        forecast_class = "predictive-negative"

    if risk_points >= 2:
        risk = "Elevated"
        risk_class = "predictive-negative"
    elif risk_points == 1:
        risk = "Moderate"
        risk_class = "predictive-neutral"
    else:
        risk = "Low"
        risk_class = "predictive-positive"

    explanation_text = (
        ", ".join(explanation[:3])
        if explanation
        else "limited directional signals"
    )

    html = f'<div class="predictive-panel"><div class="predictive-header"><div><div class="predictive-title">Predictive Market Signals</div><div class="predictive-subtitle">Short-term directional estimate from available agent signals</div></div><div class="predictive-probability {forecast_class}">{probability}%</div></div><div class="predictive-grid"><div class="predictive-card"><div class="predictive-label">Bullish Probability</div><div class="predictive-value {forecast_class}">{probability}%</div></div><div class="predictive-card"><div class="predictive-label">Momentum Forecast</div><div class="predictive-value {forecast_class}">{forecast}</div></div><div class="predictive-card"><div class="predictive-label">Short-Term Risk</div><div class="predictive-value {risk_class}">{risk}</div></div></div><div class="predictive-explanation">Signal basis: {explanation_text}.</div></div>'

    st.markdown(html, unsafe_allow_html=True)

def render_multi_asset_dashboard(multi_asset_data):
    """
    Render multiple asset cards from one query.
    """

    import streamlit as st

    if not multi_asset_data or multi_asset_data.get("status") != "success":
        return

    assets = multi_asset_data.get("assets", [])

    if not assets:
        return

    st.subheader("Multi-Asset Intelligence")

    cols = st.columns(
        min(3, len(assets))
    )

    for index, asset in enumerate(assets):
        ticker = asset.get("ticker", "N/A")
        price = asset.get("current_price", "N/A")
        trend = asset.get("trend", "neutral")
        change = float(asset.get("price_change", 0))
        daily_percent = asset.get("daily_change_percent", 0)
        weekly_percent = asset.get("weekly_change_percent", 0)

        if trend == "up":
            trend_class = "comparison-positive"
            trend_label = "▲ Up"
        elif trend == "down":
            trend_class = "comparison-negative"
            trend_label = "▼ Down"
        else:
            trend_class = "comparison-neutral"
            trend_label = "Stable"

        with cols[index % len(cols)]:
            st.markdown(
                f'<div class="screener-card"><div class="screener-rank">Asset #{index + 1}</div><div class="screener-ticker">{ticker}</div><div class="screener-price">${price}</div><div class="screener-trend {trend_class}">{trend_label} · ${abs(change)}</div><div class="screener-mini-grid"><div><span>Daily</span><strong>{daily_percent}%</strong></div><div><span>Weekly</span><strong>{weekly_percent}%</strong></div></div></div>',
                unsafe_allow_html=True
            )


def render_multi_asset_chart(multi_asset_data):
    """
    Render overlay chart for multiple detected assets.
    """

    import streamlit as st
    import pandas as pd
    import plotly.graph_objects as go

    if not multi_asset_data or multi_asset_data.get("status") != "success":
        return

    assets = [
        asset for asset in multi_asset_data.get("assets", [])
        if asset.get("historical_data")
    ]

    if len(assets) < 2:
        return

    fig = go.Figure()

    colors = [
        "#60a5fa",
        "#a855f7",
        "#22c55e",
        "#f97316"
    ]

    for index, asset in enumerate(assets):
        df = pd.DataFrame(
            asset.get("historical_data", [])
        )

        if df.empty:
            continue

        fig.add_trace(
            go.Scatter(
                x=df["date"],
                y=df["close"],
                mode="lines+markers",
                name=asset.get("ticker"),
                line=dict(
                    width=3,
                    color=colors[index % len(colors)]
                ),
                marker=dict(
                    size=7,
                    color=colors[index % len(colors)]
                )
            )
        )

    fig.update_layout(
        height=430,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(15,23,42,0.55)",
        font=dict(color="#e2e8f0"),
        title=dict(
            text="Multi-Asset Price Trend",
            font=dict(size=22, color="white"),
            x=0.02
        ),
        xaxis=dict(
            title="",
            gridcolor="rgba(255,255,255,0.06)"
        ),
        yaxis=dict(
            title="Close Price",
            gridcolor="rgba(255,255,255,0.06)"
        ),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        margin=dict(l=20, r=20, t=70, b=20)
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )