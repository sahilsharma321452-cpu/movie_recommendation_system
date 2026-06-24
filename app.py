import streamlit as st
import pickle as pkl
import pandas as pd
import re
import requests

def fetch_poster(movie_title):
    clean_title = re.sub(r'\(\d{4}\)', '', movie_title).strip()

    url = f"http://www.omdbapi.com/?t={clean_title}&apikey=b215095d"

    response = requests.get(url)
    data = response.json()

    if data.get("Response") == "True":
        return data.get("Poster")

    print("Not found:", clean_title)
    return None
def recommend(movie_name):

   
    movie_name = movie_name.strip().lower()

    
    idx = movies[
        movies['title'].str.strip().str.lower() == movie_name
    ].index

    
    if len(idx) == 0:
        idx = movies[
            movies['title'].str.strip().str.lower().str.contains(
                movie_name,
                na=False
            )
        ].index

    if len(idx) == 0:
        return ["Movie not found!"]

    idx = idx[0]

    distances, indices = model.kneighbors(
        tfidf_matrix[idx],
        n_neighbors=6
    )

    recommended_movies = []
    recommended_movies_posters=[]
    movie_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    for i in range(1, len(indices[0])):
        
        #fetch poster
        movie_idx = indices[0][i]
        movie_title = movies.iloc[movie_idx]['title']

        recommended_movies.append(movie_title)
        recommended_movies_posters.append(fetch_poster(movie_title))
        
        

    return recommended_movies,recommended_movies_posters
    



movies_dict =pkl.load(open('movies_dict.pkl','rb'))
model=pkl.load(open('model.pkl','rb'))
tfidf_matrix=pkl.load(open('tfidf.pkl','rb'))
movies=pd.DataFrame(movies_dict)
st.title("Movie Recommendation System")

select_movie_name=st.selectbox(
    'how would you  like to be contacted?',
    movies['title'].values
)
if st.button('Recommend'):
    names,posters=recommend(select_movie_name)
    cols = st.columns(5)

    for i in range(min(5, len(names))):
        with cols[i]:
            st.write(names[i])

            if posters[i] and posters[i] != "N/A":
                st.image(posters[i], use_container_width=True)
            else:
                st.write("No poster found")    