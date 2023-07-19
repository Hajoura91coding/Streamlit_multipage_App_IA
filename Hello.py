import streamlit as st

st.set_page_config(
                   page_title="Hello",
                   page_icon="👋",

                   )

st.title("Hello chers utilisateurs! 👋")
st.write(" Bienvenue dans ce mini-book qui répertorient plusieurs cas de modèles du machine learning")
st.sidebar.success("Selectionne la page qui t'interesse au-dessus:")
st.markdown(
"""
Je vous présente quelques exemples de modèles de machine learnings :
- La classification d'images
- La traduction d'une langue en langue française
et pleins d'autres qui arrivent ...
"""
)
