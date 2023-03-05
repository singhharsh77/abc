import streamlit as st
import joblit

#load the joblib model
model_nb = joblib.load('spam-ham)

st.tittle('SPAM HAM CLASSIFIER')
ip = st.text_input('Enter your text :')
                       
op = model_nb.predict([ip])
if st.button('PREDICT'):
  st.title(op[0])
