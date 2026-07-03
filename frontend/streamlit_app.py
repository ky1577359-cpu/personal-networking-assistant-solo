import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

st.title("Personalized Networking Assistant")

description = st.text_area("Event Description")
interests = st.text_input("Interests (comma separated)")

if st.button("Generate Conversation Starters"):
    response = requests.post(
        f"{BASE_URL}/generate",
        json={
            "description": description,
            "interests": [i.strip() for i in interests.split(",")]
        }
    )

    if response.status_code == 200:
        data = response.json()

        st.subheader("Topics")
        st.write(data["topics"])

        st.subheader("Conversation Starters")
        for item in data["suggestions"]:
            st.write("- " + item)

st.divider()

query = st.text_input("Fact Check")

if st.button("Check Fact"):
    response = requests.post(
        f"{BASE_URL}/fact-check",
        json={"query": query}
    )

    if response.status_code == 200:
        st.success(response.json()["summary"])