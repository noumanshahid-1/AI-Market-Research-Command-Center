"""
main.py
-------
Application entry point.

Purpose:
- Launch Streamlit dashboard
- Apply custom CSS
"""

import streamlit as st
from ui.dashboard import run_dashboard


def load_css():
    """
    Load external CSS file.
    """
    try:
        with open("ui/styles.css") as css_file:
            st.markdown(
                f"<style>{css_file.read()}</style>",
                unsafe_allow_html=True
            )
    except FileNotFoundError:
        pass


def main():
    """
    Main app launcher.
    """
    st.set_page_config(
        page_title="AI Market Research Command Center",
        layout="wide"
    )

    load_css()
    run_dashboard()


if __name__ == "__main__":
    main()