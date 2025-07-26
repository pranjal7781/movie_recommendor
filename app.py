import streamlit as st 
import pickle
import pandas as pd
import requests

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", 
    unsafe_allow_html=True)

def fetch_poster_by_title(title):
    url = f"https://api.themoviedb.org/3/search/movie?api_key=d013e6cc423395233d30a0299bb88b03&query={title}"
    response = requests.get(url)
    data = response.json()
    if data["results"]:
        poster_path = data["results"][0]["poster_path"]
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
    return "https://via.placeholder.com/300x450?text=No+Image"

movies_dic = pickle.load(open("movie_dict.pkl", "rb"))
movies_list = pd.DataFrame(movies_dic)
similarity = pickle.load(open("similarity.pkl", "rb"))

def recommend(movie):
    movie_index = movies_list[movies_list["title"] == movie].index[0]
    distances = similarity[movie_index]
    moviesList = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:7]
    
    recommended_movies = []
    recommended_posters = []
    for i in moviesList:
        title = movies_list.iloc[i[0]].title
        recommended_movies.append(title)
        recommended_posters.append(fetch_poster_by_title(title))
    return recommended_movies, recommended_posters

# Streamlit UI
st.title('🎬 Movie Recommender System')
selected_movie_name = st.selectbox("Select a movie to get recommendations:", movies_list["title"].values)

if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)
    cols = st.columns(6)
    for i in range(6):
        with cols[i]:
            st.text(names[i])
            st.image(posters[i])
st.balloons()
