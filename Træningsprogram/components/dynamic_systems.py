import streamlit as st

def render_page():
    st.header("Continuous-Time Dynamic Systems (Differential Equations)")
    
    a = st.number_input("Coefficient a:", value=1.0)
    b = st.number_input("Constant b:", value=1.0)
    y0 = st.number_input("Initial Condition y(0):", value=0.0)
    t = st.number_input("Time t:", value=1.0)
    
    # General Solution
    general_solution = f"y(t) = {b/a} + C*e^(-{a}*t)"
    st.write(f"General Solution: {general_solution}")
    
    # Specific Solution
    C = y0 - b/a
    specific_solution = f"y(t) = {b/a} + {C}*e^(-{a}*t)"
    st.write(f"Specific Solution: {specific_solution}")
    
    # Stability Analysis
    if a > 0:
        stability = "Stable (Converges to steady state)"
    else:
        stability = "Unstable (Diverges)"
    
    st.write(f"Stability: {stability}")
