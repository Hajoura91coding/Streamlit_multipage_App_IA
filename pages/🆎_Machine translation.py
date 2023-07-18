import streamlit as st

st.set_page_config(
                    page_title="Machine translation",
                    page_icon='🆎',
                    )

import deepl

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
