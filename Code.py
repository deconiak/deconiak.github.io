import streamlit as st

st.header("Système de recommandation de films.")



#Sélécteur de continent dans la variable select
select = st.selectbox('Selectionnez une rubrique', 
             ("Introduction","Sélection des films","KPI et Viz","Recommandations de films"))


def intro():
    return "Coucou"

def selec():
    return "Selec de film bâtard"

def viz():
    return "Chier la bite"

def reco():
    return "TG Camille"



if select == "Introduction" : 
    st.write(intro())

elif select == "Sélection des films" : 
    st.write(selec())

elif select == "KPI et Viz" :
    st.write(viz())

elif select == "Recommandations de films" :
    st.write(reco())
