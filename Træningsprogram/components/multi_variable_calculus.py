import streamlit as st
from sympy import symbols, diff

def render_page():
    st.header("Multi-Variable Calculus")
    
    function_str = st.text_input("Enter a function f(x, y):", "x**2 + 3*y + 1")
    x, y = symbols('x y')
    function = eval(function_str)
    
    # Partial Derivatives
    if st.button("Compute Partial Derivatives"):
        partial_x = diff(function, x)
        partial_y = diff(function, y)
        st.write(f"∂f/∂x: {partial_x}")
        st.write(f"∂f/∂y: {partial_y}")
    
    # Total Derivative & Bivariate Chain Rule
    dx_dt = st.number_input("dx/dt:", value=1.0)
    dy_dt = st.number_input("dy/dt:", value=1.0)
    total_derivative = diff(function, x) * dx_dt + diff(function, y) * dy_dt
    
    if st.button("Compute Total Derivative"):
        st.write(f"Total Derivative: {total_derivative}")
    
    # Implicit Differentiation
    implicit_eq_str = st.text_input("Enter an implicit equation F(x, y):", "x**2 + y**2 - 1")
    F = eval(implicit_eq_str)
    dy_dx_implicit = -(diff(F, x) / diff(F, y))
    
    if st.button("Compute Implicit Derivative"):
        st.write(f"dy/dx (Implicit): {dy_dx_implicit}")
