import streamlit as st
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler
from IPython.display import display



pd.set_option('max_columns', None)
pd.set_option('max_rows', None)

movie_df = pd.read_csv("C:\\Users\\Decon\\movie_df.csv")



st.header("Système de recommandation de films.")



st.cache(suppress_st_warning=True)
#Sélécteur de continent dans la variable select
select = st.selectbox('Selectionnez une rubrique', 
             ("Introduction","Sélection des films","KPI et Viz","Recommandations de films"))


def intro():
    return "Coucou"

def selec():
    return "Selec de film bâtard"

def viz():
    return "Chier la bite"


#def reco():
    
 #   film_choisi = st.selectbox('Choisisez un film', films)
  #  mask_movies = movie_df['titleFR'] == film_choisi
    #data = movie_df[mask_movies]
    #return mask_movies




if select == "Introduction" : 
    st.write(intro())

elif select == "Sélection des films" : 
    st.write(selec())

elif select == "KPI et Viz" :
    st.write(viz())

elif select == "Recommandations de films" :

    films = movie_df['titleFR'].unique()
    film_choisi = st.selectbox('Choisisez un film', films)
    mask_movies = movie_df['titleFR'] == film_choisi
