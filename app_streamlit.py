import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu

lesDonneesDesComptes = {
    'usernames': {
        'utilisateur': {
                'name': 'nicolas',
                'password': 'Worn434Raft',
                'email': 'rob.nicolas44@gmail.com',
                'failed_login_attemps': 0, # Sera géré automatiquement
                'logged_in': False, # Sera géré automatiquement
                'role': 'utilisateur'
        },
        'root': {
                'name': 'root',
                'password': 'rootMDP',
                'email': 'admin@gmail.com',
                'failed_login_attemps': 0, # Sera géré automatiquement
                'logged_in': False, # Sera géré automatiquement
                'role': 'administrateur'
        }
    }
}

authenticator = Authenticate(
    lesDonneesDesComptes, # Les données des comptes
    "cookie name", # Le nom du cookie, un str quelconque
    "cookie key", # La clé du cookie, un str quelconque
    30, # Le nombre de jours avant que le cookie expire 
)

authenticator.login()


if st.session_state["authentication_status"]:

    st.title("Bienvenu sur le contenu réservé aux utilisateurs connectés")

    options = ["Accueil", "Photos"]
    selection = st.sidebar.radio("", options)

    if selection == "Accueil":
        st.write("Bienvenue sur la page d'accueil !")
    elif selection == "Photos":
        st.write("Bienvenue sur mon album photo")

        # Le bouton de déconnexion
    st.sidebar.markdown(
        """
        <style>
        .sidebar .sidebar-content {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    authenticator.logout("Déconnexion", "sidebar")


elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')