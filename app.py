import streamlit as st
import pickle
import pandas as pd
movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies_df=pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl','rb'))

def recommend(movie):
    movie_index=movies_df[movies_df['title']==movie].index[0]
    distances=similarity[movie_index]
    movie_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    for i in movie_list:
        recommended_movies.append(movies_df.iloc[i[0]].title)
    return recommended_movies


st.title('Movie Recommender')

selected_movie_name= st.selectbox(
    "How would you like to be contacted?",
    (movies_df['title'].values)
)
if st.button("Recommend"):
    recommendation=recommend(selected_movie_name)
    for i in recommendation:
        st.write(i)
