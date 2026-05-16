import streamlit as st
from sympy import symbols, integrate

def render_page():
    st.header("Integral Calculus & Distribution Metrics")
    
    function_str = st.text_input("Enter a function f(x):", "x**2 + 3*x + 1")
    x = symbols('x')
    function = eval(function_str)
    
    # Indefinite Integral
    if st.button("Compute Indefinite Integral"):
        indefinite_integral = integrate(function, x)
        st.write(f"Indefinite Integral: {indefinite_integral}")
    
    # Definite Integral
    lower_limit = st.number_input("Lower Limit:", value=0.0)
    upper_limit = st.number_input("Upper Limit:", value=1.0)
    
    if st.button("Compute Definite Integral"):
        definite_integral = integrate(function, (x, lower_limit, upper_limit))
        st.write(f"Definite Integral: {definite_integral}")
