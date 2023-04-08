import streamlit as st
import pandas as pd
import pickle
import requests # api

simulary=pickle.load(open("simulary.pklsimulary.pkl","rb"))

st.title("Movie Recomender System")

df=pd.read_csv("new_tmbd.csv")
movie_name=df["title"].values


def simul(movie):
    index = df[df["title"] == movie].index[0]
    distance = simulary[index]
    # for 1st movie 2 movies simularities and 1st movie 3 movie simularities , 1 move 4th....
    list_v = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    re_m=[]
    recommended_movie_posters = []

    for i in list_v:
        movie_id = df.iloc[i[0]].movie_id
        c = i[0]
        re_m.append(df.iloc[c]["title"])
        recommended_movie_posters.append(fetch_poster(movie_id))

    return re_m,recommended_movie_posters



def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=< PASTE UR TOKEN HRER >&language=en-US".format(movie_id)
    #over here the "{}" we put the "format(movie_id)" over there
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path





select = st.selectbox(
    'What would you like to see',
    (movie_name))

if st.button('Recommend'):
    ss,recommended_movie_posters = simul(select)
    lis=[]
    for i in ss:
        lis.append(i)
        #st.write(i)


    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(lis[0])
        st.image(recommended_movie_posters[0])

    with col2:
        st.text(lis[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(lis[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(lis[3])
        st.image(recommended_movie_posters[3])

    with col5:
        st.text(lis[4])
        st.image(recommended_movie_posters[4])
