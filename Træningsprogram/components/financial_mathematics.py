import streamlit as st

def render_page():
    st.header("Financial Mathematics (Annuity Applications)")
    
    PV = st.number_input("Principal Volume (PV):", value=10000.0)
    r = st.number_input("Periodic Interest Rate (r) [as decimal]:", value=0.05)
    n = st.number_input("Total Payment Intervals (n):", value=60.0)
    
    # Annuity Loan Amortization
    a = (r * PV) / (1 - (1 + r)**-n)
    st.write(f"Fixed Periodic Payment: {a}")
    
    # Outstanding Debt Valuation
    t = st.number_input("Number of Payment Periods Passed (t):", value=10.0)
    restgæld = PV * ((1 + r)**t - 1) / ((1 + r)**n - 1)
    st.write(f"Outstanding Debt After {t} periods: {restgæld}")
