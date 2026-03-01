import streamlit as st
import requests
import json

st.set_page_config(page_title="SHL Assessment Recommender", page_icon="📋", layout="wide")

st.title("🎯 SHL Assessment Recommendation System")
st.markdown("Get personalized assessment recommendations based on your job requirements")

# API URL input
api_url = st.sidebar.text_input(
    "API URL",
    value="YOUR_NGROK_URL_HERE",
    help="Enter your API endpoint URL"
)

# Query input
query = st.text_area(
    "Enter Job Description or Query",
    height=150,
    placeholder="Example: I am hiring for Java developers who can also collaborate effectively with my business teams."
)

if st.button("Get Recommendations", type="primary"):
    if not query:
        st.warning("Please enter a query")
    else:
        with st.spinner("Analyzing query and fetching recommendations..."):
            try:
                response = requests.post(
                    f"{api_url}/recommend",
                    json={"query": query},
                    headers={"Content-Type": "application/json"},
                    timeout=30
                )
                
                if response.status_code == 200:
                    data = response.json()
                    recommendations = data.get("recommended_assessments", [])
                    
                    st.success(f"Found {len(recommendations)} recommendations!")
                    
                    for i, rec in enumerate(recommendations, 1):
                        with st.expander(f"#{i}: {rec['name']}", expanded=(i<=3)):
                            col1, col2 = st.columns([2, 1])
                            
                            with col1:
                                st.markdown(f"**Description:** {rec.get('description', 'N/A')}")
                                st.markdown(f"**Test Types:** {', '.join(rec.get('test_type', []))}")
                                st.markdown(f"**[View Assessment]({rec['url']})**")
                            
                            with col2:
                                st.metric("Duration", f"{rec.get('duration', 'N/A')} min")
                                st.text(f"Adaptive: {rec.get('adaptive_support', 'N/A')}")
                                st.text(f"Remote: {rec.get('remote_support', 'N/A')}")
                else:
                    st.error(f"Error: {response.status_code} - {response.text}")
                    
            except Exception as e:
                st.error(f"Error connecting to API: {str(e)}")

# Sidebar info
st.sidebar.markdown("---")
st.sidebar.markdown("### About")
st.sidebar.info(
    "This system uses RAG and LLMs to recommend "
    "relevant SHL assessments based on job requirements."
)
