import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=537533250b86a80fe3e199d111e4c90e&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].id

        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters


movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))
st.title('Movie Recommender System')

selected_movie_name = st.selectbox('Enter Movie Name Here ', movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    c1, c2, c3, c4, c5 = st.columns(5)

    with c1:
        st.text(names[0])
        st.image(posters[0])
    with c2:
        st.text(names[1])
        st.image(posters[1])
    with c3:
        st.text(names[2])
        st.image(posters[2])
    with c4:
        st.text(names[3])
        st.image(posters[3])
    with c5:
        st.text(names[4])
        st.image(posters[4])
