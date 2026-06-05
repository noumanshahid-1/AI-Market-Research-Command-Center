"""
dashboard.py
------------
Main Streamlit dashboard logic.
"""

import streamlit as st

from orchestrator.core import Orchestrator
from utils.storage import (
    load_watchlist,
    save_watchlist,
    load_search_history,
    save_search_history
)

from ui.components import (
    render_header,
    render_search_bar,
    render_summary,
    render_kpi_cards,
    render_market_score,
    render_ai_confidence,
    render_comparison_card,
    render_comparison_chart,
    render_stock_card,
    render_stock_chart,
    render_news_card,
    render_product_card,
    render_product_chart,
    render_screener_dashboard,
    render_screener_chart,
    render_screener_brief,
    render_sentiment_panel,
    render_strategy,
    render_sector_heatmap,
    render_predictive_signals,
    render_multi_asset_dashboard,
    render_multi_asset_chart,
)


def run_analysis(query: str):
    """
    Run orchestrator and persist latest results.
    """

    if not query.strip():
        st.warning("Please enter a valid query.")
        return

    if (
        not st.session_state.search_history
        or st.session_state.search_history[-1] != query
    ):
        st.session_state.search_history.append(query)
        save_search_history(st.session_state.search_history)

    with st.spinner("Running parallel agent intelligence..."):
        system = Orchestrator(query)
        st.session_state.last_results = system.execute()


def run_dashboard():
    """
    Main UI execution flow.
    """

    if "search_history" not in st.session_state:
        st.session_state.search_history = load_search_history()

    if "watchlist" not in st.session_state:
        st.session_state.watchlist = load_watchlist()

    if "last_results" not in st.session_state:
        st.session_state.last_results = None

    if "active_query" not in st.session_state:
        st.session_state.active_query = ""

    render_header()

    with st.sidebar:

        st.markdown(
            """
            <div class="sidebar-title">Command Center</div>
            <div class="sidebar-subtitle">Market memory & quick actions</div>
            """,
            unsafe_allow_html=True
        )

        st.divider()

        st.markdown("### Watchlist")

        manual_ticker = st.text_input(
            "Add ticker",
            placeholder="AAPL, TSLA, BTC-USD",
            key="manual_watchlist_input"
        )

        if st.button("Add to Watchlist", key="manual_add_watchlist"):
            ticker = manual_ticker.strip().upper()

            if ticker:
                if ticker not in st.session_state.watchlist:
                    st.session_state.watchlist.append(ticker)
                    save_watchlist(st.session_state.watchlist)
                    st.success(f"{ticker} added.")
                    st.rerun()
                else:
                    st.info(f"{ticker} already exists.")

        if st.session_state.watchlist:
            for ticker in list(st.session_state.watchlist):

                col1, col2 = st.columns([4, 1])

                with col1:
                    if st.button(
                        f"★ {ticker}",
                        key=f"watch_analyze_{ticker}"
                    ):
                        run_analysis(f"{ticker} stock")
                        st.rerun()

                with col2:
                    if st.button(
                        "×",
                        key=f"watch_remove_{ticker}"
                    ):
                        st.session_state.watchlist.remove(ticker)
                        save_watchlist(st.session_state.watchlist)
                        st.rerun()

            if st.button("Clear Watchlist", key="clear_watchlist"):
                st.session_state.watchlist = []
                save_watchlist(st.session_state.watchlist)
                st.rerun()

        else:
            st.markdown(
                """
                <div class="sidebar-empty">
                    No tracked assets yet.
                </div>
                """,
                unsafe_allow_html=True
            )

        st.divider()

        st.markdown("### Search History")

        if st.session_state.search_history:
            for index, item in enumerate(
                reversed(st.session_state.search_history[-8:])
            ):
                if st.button(
                    item,
                    key=f"history_{index}_{item}"
                ):
                    run_analysis(item)
                    st.rerun()

            if st.button("Clear History", key="clear_history"):
                st.session_state.search_history = []
                save_search_history(st.session_state.search_history)
                st.rerun()

        else:
            st.markdown(
                """
                <div class="sidebar-empty">
                    No searches yet.
                </div>
                """,
                unsafe_allow_html=True
            )

    query = render_search_bar()

    if st.button("Analyze Market", key="main_analyze"):
        run_analysis(query)

    results = st.session_state.last_results

    if not results:
        return

    if results.get("status") != "success":
        st.error(
            results.get(
                "summary",
                "Something went wrong."
            )
        )
        return

    render_summary(results["summary"])

    is_macro_view = bool(
        results.get("screener")
        or results.get("heatmap")
    )
    if not is_macro_view:
        render_kpi_cards(results)
        render_market_score(results)
        render_ai_confidence(results)
        render_predictive_signals(results)

    if results.get("screener"):
        render_screener_dashboard(
            results["screener"]
        )

        render_screener_chart(
            results["screener"]
        )

        render_screener_brief(
            results["screener"]
        )

    if results.get("heatmap"):
        render_sector_heatmap(
            results["heatmap"]
        )

    if results.get("comparison"):
        render_comparison_card(
            results["comparison"]
        )

        render_comparison_chart(
            results["comparison"]
        )

    if results.get("multi_asset"):
        render_multi_asset_dashboard(
            results["multi_asset"]
        )

        render_multi_asset_chart(
            results["multi_asset"]
        )

    if results.get("stock"):

        stock_data = results["stock"]

        render_stock_card(stock_data)

        render_stock_chart(stock_data)

        ticker = stock_data.get("ticker")

        if ticker:
            if st.button(
                f"Add {ticker} to Watchlist",
                key=f"watch_{ticker}"
            ):
                if ticker not in st.session_state.watchlist:
                    st.session_state.watchlist.append(ticker)
                    save_watchlist(st.session_state.watchlist)
                    st.success(f"{ticker} added to watchlist.")
                    st.rerun()
                else:
                    st.info(f"{ticker} already in watchlist.")

    if results.get("news"):
        render_news_card(results["news"])
        render_sentiment_panel(results["news"])

    if results.get("product"):
        render_product_card(results["product"])
        render_product_chart(results["product"])

    if (
        results.get("strategy")
        and not is_macro_view
    ):
        render_strategy(results["strategy"])