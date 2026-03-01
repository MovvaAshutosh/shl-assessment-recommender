🎯 SHL Assessment Recommendation System

An intelligent web application that recommends relevant SHL assessments based on job descriptions using Retrieval-Augmented Generation (RAG) and Large Language Models (LLMs).

📌 Project Overview

The SHL Assessment Recommendation System helps recruiters and hiring managers select appropriate SHL assessments based on job requirements. Instead of manually searching through assessment catalogs, users can simply input a job description and receive structured recommendations.

The system analyzes the query, retrieves relevant assessment data, and returns detailed recommendations including:

Assessment Name

Description

Test Types

Duration

Adaptive Support

Remote Support

Direct URL

This solution improves hiring efficiency and supports data-driven talent evaluation.

🏗️ Architecture

Frontend → Streamlit Web App
Backend → API Endpoint
Processing → RAG + LLM-based recommendation logic

Workflow:

User enters job description.

Streamlit sends request to backend API.

Backend processes query using RAG.

Recommended assessments are returned.

Results displayed in structured UI.

💻 Tech Stack

Python

Streamlit

Requests (API integration)

RAG (Retrieval-Augmented Generation)

LLMs

JSON-based API communication

📂 Project Structure
shl-assessment-recommender/
│
├── streamlit_app.py
├── SHL_Assessment_Recommendation_System.ipynb
├── requirements.txt
├── README.md
└── .gitignore
⚙️ Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/yourusername/shl-assessment-recommender.git
cd shl-assessment-recommender
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Run the Application
streamlit run streamlit_app.py
🔌 API Configuration

In the Streamlit sidebar, enter your backend API URL:

http://your-api-url/recommend

If using ngrok:

https://your-ngrok-url.ngrok.io
🚀 Features

Intelligent assessment recommendation

Clean and interactive Streamlit UI

API-based modular architecture

Structured recommendation output

Expandable results display

Error handling for API failures

📊 Use Case

This project is ideal for:

HR Technology platforms

Recruitment automation systems

Talent assessment platforms

AI-powered hiring assistants

🧠 Future Improvements

Authentication system

Deployment on cloud (AWS / Render / Streamlit Cloud)

Database integration

Admin dashboard

Logging & analytics

Model performance evaluation metrics

📜 License

This project is for educational and demonstration purposes.
