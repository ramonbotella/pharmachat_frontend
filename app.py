import streamlit as st
import requests

# Streamlit App Title
st.title("PharmaChat Frontend")

# Input fields for medicament and question
medicament = st.text_input("Enter the name of the medicament:")
question = st.text_input("Enter your question:")

# Submit button to query the API
if st.button("Submit"):
    # Check if both inputs are provided
    if not medicament or not question:
        st.error("Please enter both the medicament and the question.")
    else:
        # Make the POST request to the PharmaChat API
        try:
            response = requests.post(
                "http://pharmachat:8000/query",
                json={"medicament": medicament, "question": question},
            )
            # Handle the API response
            if response.status_code == 200:
                result = response.json()
                st.success("Response from PharmaChat:")
                st.write(result.get("response", "No response received."))
            elif response.status_code == 404:
                st.error(f"Error: {response.json().get('detail')}")
            else:
                st.error(f"Error: Unexpected status code {response.status_code}")
        except Exception as e:
            st.error(f"Failed to connect to PharmaChat API: {e}")
