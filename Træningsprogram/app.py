import streamlit as st
from components import calculus, optimization, integral_calculus, dynamic_systems, financial_mathematics

st.title("Advanced Math Training Program Generator")

# Sidebar for navigation
with st.sidebar:
    st.header("Navigation")
    page = st.selectbox(
        "Select a Topic",
        [
            "Single-Variable Calculus & Function Analysis",
            "Multi-Variable Calculus",
            "Unconstrained & Constrained Optimization",
            "Integral Calculus & Distribution Metrics",
            "Continuous-Time Dynamic Systems (Differential Equations)",
            "Discrete-Time Dynamic Systems (Difference Equations)",
            "Financial Mathematics (Annuity Applications)"
        ]
    )

# Render the selected page
if page == "Single-Variable Calculus & Function Analysis":
    calculus.render_page()
elif page == "Multi-Variable Calculus":
    multi_variable_calculus.render_page()
elif page == "Unconstrained & Constrained Optimization":
    optimization.render_page()
elif page == "Integral Calculus & Distribution Metrics":
    integral_calculus.render_page()
elif page == "Continuous-Time Dynamic Systems (Differential Equations)":
    dynamic_systems.render_page()
elif page == "Discrete-Time Dynamic Systems (Difference Equations)":
    discrete_time_dynamic_systems.render_page()
elif page == "Financial Mathematics (Annuity Applications)":
    financial_mathematics.render_page()

