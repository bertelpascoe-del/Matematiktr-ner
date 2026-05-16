import streamlit as st

def render_page():
    st.header("Discrete-Time Dynamic Systems (Difference Equations)")
    
    a = st.number_input("Coefficient a:", value=0.5)
    b = st.number_input("Constant b:", value=1.0)
    t = st.number_input("Time t:", value=10.0)
    
    # General Solution
    general_solution = f"Y_t = {b/(1+a)} + C*(-a)^t"
    st.write(f"General Solution: {general_solution}")
    
    # Stability Analysis
    if abs(a) < 1:
        stability = "Stable (Converges)"
    else:
        stability = "Unstable (Diverges)"
    
    st.write(f"Stability: {stability}")
