import streamlit as st
from rag_sql import ask_question

st.set_page_config(page_title="RAG-SQL Customer Chatbot")

st.title("RAG-SQL Customer Chatbot")

question = st.text_input("Ask a question about the customer database:")

if st.button("Ask"):
    if question:
        result, sql_query = ask_question(question)

        st.subheader("Response:")
        st.write(result)

        st.subheader("SQL Query:")
        st.code(sql_query, language="sql")
    else:
        st.warning("Please enter a question before clicking Ask.")
