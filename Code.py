df_car = pd.read_csv('https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv')


st.title("Analyse du dataset des voitures")

st.write(' ')
st.write(' ')


#Sélécteur de continent dans la variable select
select = st.selectbox('Selectionnez une région', 
             ("Tous","USA","Europe","Japon"))

st.write(' ')
st.write(' ')

st.subheader("""Analyse de corrélation""")


#Adaptation du DF selon la select
if select == "Tous":
  df = df_car
  st.write("""
  
  Sur les colonnes les plus corrélées tout continents confondus on constate que : 
  
  - Le poids, la puissance, la cylindrée et le nombre de cylindres influent fortement sur la consommation d'essence (MPG)
  
  - Une voiture avec plus de puissance (HP) prendra moins de temps à monter à une vitesse de 60 Mph
  
  - Une voiture légere a un nombre de cylindres et une cylindrée faibles et par conséquent une puissance moindre.
  
  """)

if select == "USA" : 
  df = df_car[df_car['continent'] == ' US.']
  st.write("""
  
  Sur les colonnes les plus corrélées aux USA on constate que : 
  
  - Le poids, la puissance, la cylindrée et le nombre de cylindres influent fortement sur la consommation d'essence (MPG)
  
  - Une voiture avec plus de puissance (HP) prendra moins de temps à monter à une vitesse de 60 Mph
  
  """)

if select == "Europe":
  df = df_car[df_car["continent"]==' Europe.']
  st.write("""
  
  Sur les colonnes les plus corrélées en Europe on constate que : 
  
  - Globalement les voitures semblent moins puissantes et lourdes que les véhicules des USA
  
  - 
  
  """)
  
if select == "Japon":
  df = df_car[df_car["continent"]==' Japan.']


# Matrice de corrélation
corr = df.corr()
fig = go.Figure()
fig.add_trace(go.Heatmap(
  z = corr,
  x = corr.columns.values,
  y = corr.columns.values,
  colorscale = px.colors.diverging.RdBu,
  zmid=0
))
fig.update_layout(width=1000, height=900)
st.plotly_chart(fig)
