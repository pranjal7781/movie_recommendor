# 🎬 Movie Recommender System

A content-based movie recommendation web app built using **Python**, **Streamlit**, and **scikit-learn**. This app recommends similar movies based on the selected title and displays their posters using the TMDb API.

---

## 📌 Features

- 🔍 Select a movie and get 5 similar movie recommendations  
- 🖼️ Fetch movie posters dynamically using TMDb API  
- 🧠 Uses **cosine similarity** on movie tags for recommendation  
- 💡 Built with **Streamlit** for an interactive web UI  

---
## 🛠️ Technologies Used
Python
Pandas, NumPy
Scikit-learn
Streamlit
TMDb API

## 🧪 How It Works

1. Movie titles and tag features are preprocessed and saved into .pkl files.

2. When a user selects a movie from the dropdown, the app:
   -Finds similar movies using cosine similarity
   -Fetches posters for the top 5 matches via TMDb API

## 🔐 TMDb API Key
To fetch movie posters, you need a free TMDb API key.
Replace your_api_key_here in the code with your own API key:

api_key = "your_api_key_here"


## 🚀 Demo

Run the app locally:
```bash

streamlit run app.py
