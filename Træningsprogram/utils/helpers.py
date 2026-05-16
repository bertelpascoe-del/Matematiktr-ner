def safe_eval(expr):
    try:
        return eval(expr)
    except Exception as e:
        st.error(f"Error evaluating expression: {e}")
        return None
