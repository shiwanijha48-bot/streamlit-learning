import streamlit as st

st.title("Chai Taste Poll")
col1 , col2 = st.columns(2)
with col1:
    st.header("mashala chai")
    st.image("https://cdn.shopify.com/s/files/1/0148/1945/9126/articles/Chai_Masala_Tea.jpg?v=1606936195", width = 200)
    vote1 = st.button("vote mashala chai")

with col2:
    st.header("adrak chai")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ336o_vw_8MCwydgz5IkaTc6mmKzfklmSlLf97ExiCEGhMaBN6WV3cN5v5&s=10", width = 200)
    vote2 = st.button("vote adrak chai")

if vote1:
    st.success("thanks for voting masala chai")
if vote2:
    st.success("thanks for voting adrak chai")

name = st.sidebar.text_input("Enter your Name")
tea = st.sidebar.selectbox("choose your chai:", ["mashala", "kesar", "lemon"])

st.write(f"welcome,{name} and your {tea} chai is getting ready")

with st.expander("show chai making instructions"):
    st.write("""
    1. boil water with tea leaves
    2. add milk with spices
    3. serve hot
    """)
st.markdown('# welcome to chai app')
st.markdown('> Blockquote')
