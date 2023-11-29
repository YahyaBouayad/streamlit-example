import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
from fonction_project import *
import warnings
warnings.filterwarnings('ignore')
#%% Traitement fichier 
info_col = [
    'Age', 
    'Genre', 
    'Education', 
    'Pays',
    'Ethnie',
]

caract_col = [
    'Neuroticisme',
    'Extraversion',
    'Ouverture à l\'expérience',
    'Amicalité',
    'Conscience',
    'Impulsivité',
    'Recherche de sensations'
]

personne_col = info_col + caract_col

drogues_col = [
    'Consommation d\'alcool',
    'Consommation d\'amphétamines',
    'Consommation d\'amyl',
    'Consommation de benzodiazepine',
    'Consommation de café',
    'Consommation de cannabis',
    'Consommation de chocolat',
    'Consommation de cocaïne',
    'Consommation de crack',
    'Consommation d\'ecstasy',
    'Consommation d\'héroïne',
    'Consommation de ketamine',
    'Consommation de drogues légales',
    'Consommation de LSD',
    'Consommation de meth',
    'Consommation de champignons magiques',
    'Consommation de nicotine',
    'Consommation de Semeron',
    'Consommation de VSA'
]

drogues_autorisées = ['Consommation d\'alcool', 'Consommation de café', 'Consommation de chocolat', 'Consommation de nicotine']
drogues_illégales = [i for i in drogues_col if i not in drogues_autorisées]
col = personne_col + drogues_col

data=lecture_data()
pers_data=pre_data(data,col,drogues_col,drogues_illégales)



#%% Debut Page 

# TITRE : 
st.title("Data Analyse for the drug data ")
st.markdown("Project made by \r Yahya \r Hamza \r Joshua ")

if st.checkbox("Show raw data"):
    st.subheader('Drug Raw data used')
    st.write(data)
    st.markdown(
        """
        The data here is made up of 31 columns, the first represents characteristics about the person such as age, education and others. Then there are the psychological characteristics of the person, and finally if he has consumed certain types of drugs ranging from chocolate to cocaine.
We have 1800 individuals, which gives us a good data set to study.

        """
        )
st.markdown("We cleaned the dataset and we were able to assign this representation to each value, for this we used the explanations in the description of the dataset.")
if st.checkbox("Show cleaned data"):
    st.subheader('Cleaned data used')
    st.write(pers_data)
    st.markdown("Ther was no null data, so we had nothing to remove, we just removed the line where someone said that they have used Semeron. Wich is a fake drug used to get raid of the liar")


st.title("Heat map of the data")
st.markdown("We plot this heat map so we can visualise the correlation between data, it can give us idea of graphic we can make.")
st.pyplot(heat_map_data(data))
#################################################################
st.title("... plot for analyse the simple data : ")
st.markdown("Proportion of data for every Personnel information")
####################################################################

selected_column = st.selectbox('Choisissez une colonne pour l\'analyse', info_col)
tab1, tab2 = st.tabs(["Bar exemple", "Pie chart Exemple"])
with tab1:
    fig = plot_proportion_bar(pers_data, selected_column)
    st.pyplot(fig)
with tab2:
    st.plotly_chart(plot_pie_chart(pers_data,selected_column),theme="streamlit", use_container_width=True)
   
    

##############################################################################

st.markdown("Choix affichage complet")
selected_column_a = st.selectbox('Choisissez la première colonne',drogues_col )
selected_column_b = st.selectbox('Choisissez la deuxième colonne',info_col )
# Affichage du graphique à barres en fonction des colonnes sélectionnées
if st.button('Afficher le graphe'):
    fig2 = plot_proportion_bar2(pers_data, selected_column_a, selected_column_b)
    st.pyplot(fig2)

#######################################################################################
st.markdown("User count for different drogues ")
st.pyplot(plot_user_counts_per_drug_combined(data,drogues_col))
st.markdown("And for more detail :")
selected_column_details = st.selectbox('Choisissez la deuxième colonne',drogues_col )
on = st.toggle('Afficher les details:')

if on:
    st.pyplot(plot_user_counts_for_drug(data,selected_column_details))

#######################################################################################
mon_dictionnaire = {
    "Individu": info_col,
    "Caractere": caract_col,
    "Drogues": drogues_col
}

st.markdown("Analyse de la matrice de correlation selon une colonne choisi")
cle_choisie = st.selectbox("Choisissez une clé :", list(mon_dictionnaire.keys()))
st.pyplot(plot_correlation_matrix(data,mon_dictionnaire[cle_choisie]))
################################################################################


#######################################################################################
st.title("Analyse approfondie :")
st.markdown("Analyse des caracteres d'une personne moyenne qui consomme une drogue")
selected_column_drogue = st.selectbox('Choisissez une colonne pour l\'analyse', drogues_col )

col1, col2 = st.columns(2)
# Afficher les graphiques dans les colonnes correspondantes
with col1:
    st.pyplot(radar_chart_consommation_drogue(pers_data,selected_column_drogue,caract_col,True))
with col2:
    st.pyplot(radar_chart_consommation_drogue(pers_data,selected_column_drogue,caract_col,False))

st.markdown("Pour une vue d'ensemble:")
st.plotly_chart(profil_drogue_radar(pers_data,drogues_col,caract_col),theme="streamlit", use_container_width=True)

###########################################################################################################################

st.subheader("Tendance de consomation selon la tranche d'age :sunglasses:")
col1, col2 = st.columns([1, 3])
with col1:
    selected_column_drug = st.selectbox('Choisissez la drogue à etudier ', drogues_col )
with col2:
    st.plotly_chart(plot_drug_use_trends_by_age_pers_data(pers_data,selected_column_drug),theme="streamlit", use_container_width=True)
