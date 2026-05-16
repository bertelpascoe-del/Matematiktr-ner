import streamlit as st
from sympy import symbols, diff, solve

def render_page():
    st.header("Unconstrained & Constrained Optimization")
    
    function_str = st.text_input("Enter a function f(x, y):", "x**2 + 3*y + 1")
    x, y = symbols('x y')
    function = eval(function_str)
    
    # Unconstrained Optimization
    partial_x = diff(function, x)
    partial_y = diff(function, y)
    
    if st.button("Find Critical Points"):
        critical_points = solve((partial_x, partial_y), (x, y))
        st.write(f"Critical Points: {critical_points}")
    
    # Constrained Optimization (Lagrange Multipliers)
    constraint_str = st.text_input("Enter a constraint g(x, y) = c:", "x + y - 1")
    c_value = st.number_input("Constraint Value (c):", value=1.0)
    lambda_ = symbols('lambda')
    
    lagrange_function = function - lambda_ * (eval(constraint_str) - c_value)
    partial_lambda = diff(lagrange_function, lambda_)
    
    if st.button("Compute Lagrange Multipliers"):
        solutions = solve((partial_x, partial_y, partial_lambda), (x, y, lambda_))
        st.write(f"Solutions: {solutions}")
