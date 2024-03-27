import streamlit as st

st.title("App Title")
st.markdown("## Markdown Header")
st.header("Streamlit Header")
st.subheader("Streamlit SubHeader")
st.caption("Streamlit caption")
st.code("pip install pip3")
st.latex(r'''
 a + a r ^1 + a r ^2 + a r ^3''')

st.image("kid.jpg")
st.audio("Audio.mp3")
st.video("video.mp4")

st.checkbox('yes')
st.button('Click')
st.radio('Pick your gender',['Male', 'Female'])
st.selectbox('Pick your gender',['Male', 'Female'])
st.multiselect('Choose a planet',['Jupiter', 'Mars', 'Neptune'])
st.select_slider('Pick a mark',['Bad', 'Good', 'Excellent'])
st.slider('Pick a number', 0,50)

