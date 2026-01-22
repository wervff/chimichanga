# File: calculator.py
import streamlit as st

# ───────────────────────────────────────────────
# Initialize session state (persists across reruns)
# ───────────────────────────────────────────────
if 'expression' not in st.session_state:
    st.session_state.expression = ''

# ───────────────────────────────────────────────
# Helper functions
# ───────────────────────────────────────────────
def add_to_expression(symbol):
    st.session_state.expression += str(symbol)

def clear_expression():
    st.session_state.expression = ''

def evaluate_expression():
    try:
        result = eval(st.session_state.expression)
        st.session_state.expression = str(result)
    except Exception:
        st.session_state.expression = 'Error'

# ───────────────────────────────────────────────
# Layout
# ───────────────────────────────────────────────
st.title("Calculator")

# Display field
st.markdown(
    f"""
    <div style="
        background-color: #2e2e2e;
        color: white;
        font-family: Arial, sans-serif;
        font-size: clamp(1.8rem, 9vw, 3.2rem);
        padding: 16px 12px;
        text-align: right;
        border-radius: 10px;
        min-height: 70px;
        margin-bottom: 12px;
        overflow-wrap: break-word;
        word-break: break-all;
        font-weight: 400;
        letter-spacing: 0.5px;
    ">
        {st.session_state.expression or '0'}
    </div>
    """,
    unsafe_allow_html=True
)

# Better button styling + make + very visible
st.markdown("""
    <style>
        div.stButton > button {
            width: 100%;
            height: 68px;
            font-size: 1.55rem !important;
            font-weight: 500;
            border-radius: 12px;
            margin: 3px 0;
            background-color: #444;
            color: white;
        }
        div.stButton > button:hover {
            background-color: #555;
        }
        div.stButton > button[kind="primary"] {
            background-color: #ff9500;
            color: white;
        }
        /* Force + button to be orange and show big + */
        button[kind="secondary"][data-testid*="btn+"] {
            background-color: #ff9500 !important;
            color: white !important;
            font-size: 2.1rem !important;
            font-weight: 700 !important;
        }
    </style>
""", unsafe_allow_html=True)

# Create columns (5-column layout)
col1, col2, col3, col4, col5 = st.columns(5)

# Row 1: 7 8 9 + (
with col1:
    st.button("7", key="btn7", use_container_width=True, on_click=add_to_expression, args=("7",))
with col2:
    st.button("8", key="btn8", use_container_width=True, on_click=add_to_expression, args=("8",))
with col3:
    st.button("9", key="btn9", use_container_width=True, on_click=add_to_expression, args=("9",))
with col4:
    st.button("+", key="btn+", use_container_width=True, on_click=add_to_expression, args=("+",))
with col5:
    st.button("(", key="btn(", use_container_width=True, on_click=add_to_expression, args=("(",))

# Row 2: 4 5 6 − )
with col1:
    st.button("4", key="btn4", use_container_width=True, on_click=add_to_expression, args=("4",))
with col2:
    st.button("5", key="btn5", use_container_width=True, on_click=add_to_expression, args=("5",))
with col3:
    st.button("6", key="btn6", use_container_width=True, on_click=add_to_expression, args=("6",))
with col4:
    st.button("−", key="btn-", use_container_width=True, on_click=add_to_expression, args=("-",))
with col5:
    st.button(")", key="btn)", use_container_width=True, on_click=add_to_expression, args=(")",))

# Row 3: 1 2 3 × ÷
with col1:
    st.button("1", key="btn1", use_container_width=True, on_click=add_to_expression, args=("1",))
with col2:
    st.button("2", key="btn2", use_container_width=True, on_click=add_to_expression, args=("2",))
with col3:
    st.button("3", key="btn3", use_container_width=True, on_click=add_to_expression, args=("3",))
with col4:
    st.button("×", key="btn*", use_container_width=True, on_click=add_to_expression, args=("*",))
with col5:
    st.button("÷", key="btn/", use_container_width=True, on_click=add_to_expression, args=("/",))

# Row 4: 0 C =
with col1:
    st.button("0", key="btn0", use_container_width=True, on_click=add_to_expression, args=("0",))
with col2:
    st.button("C", key="btnC", use_container_width=True, on_click=clear_expression)
with col3:
    st.button("=", key="btn=", use_container_width=True, on_click=evaluate_expression, type="primary")

st.caption("Simple calculator — made with Streamlit")