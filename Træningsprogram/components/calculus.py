import streamlit as st
from sympy import symbols, diff, limit, solve, ln, exp

def render_page():
    st.header("Single-Variable Calculus & Function Analysis")
    
    function_str = st.text_input("Enter a function f(x):", "x**2 + 3*x + 1")
    x = symbols('x')
    function = eval(function_str)
    
    # Differentiation
    if st.button("Compute Derivative"):
        derivative = diff(function, x)
        st.write(f"Derivative: {derivative}")
    
    # Limits
    limit_type = st.selectbox("Limit Type", ["x -> ∞", "x -> 0"])
    if limit_type == "x -> ∞":
        lim_value = limit(function, x, float('inf'))
    else:
        lim_value = limit(function, x, 0)
    
    if st.button("Compute Limit"):
        st.write(f"Limit: {lim_value}")
    
    # Monotonicity & Extrema
    derivative_expr = diff(function, x)
    critical_points = solve(derivative_expr, x)
    
    if st.button("Find Critical Points and Extrema"):
        st.write(f"Critical Points: {critical_points}")
    
    # Economic Elasticity
    elasticity_expr = (x / function) * derivative_expr
    if st.button("Compute Elasticity"):
        st.write(f"Elasticity: {elasticity_expr}")

