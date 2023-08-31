import streamlit as st
import os
st.set_page_config(
                    page_title="Machine translation",
                    page_icon='🆎',
                    )

import deepl



# Replicate Credentials
with st.sidebar:
    st.title('Machine translation🆎')
    st.write("Traduisez en toute confiance ! :p ")
    if 'DEEPL_API_TOKEN' in st.secrets:
        st.success('La clé est déjà validé!', icon='✅')
        deepl_api = st.secrets['DEEPL_API_TOKEN']
    else:
        deepl_api = st.text_input('Entre l\'API REST Deepl:', type='password')
        if not (deepl_api.startswith('r8_') and len(deepl_api)==40):
            st.warning('Please enter your credentials!', icon='⚠️')
        else:
            st.success('Veuillez entrer le prompt!', icon='👉')

os.environ['DEEPL_API_TOKEN'] = deepl_api

def auto_translate():

    key = st.text_input("Entre ta clé deepl :")
    if key :
     translator = deepl.Translator(key)

     texte = st.text_input("Ecrire le texte que vous voulez traduire en français :")
     if texte :
         result = translator.translate_text(texte, target_lang="FR")
         st.write(result.text)



if __name__ == "__main__":
    auto_translate();
