import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

from genres.service import GenreService


def show_genres():
    genre_service = GenreService()
    genres = genre_service.get_genres()

    if genres:
        st.write("Lista de Gêneros:")
        genres_df = pd.json_normalize(genres)
        AgGrid(
            data=genres_df,
            key="genres_grid",
        )
    else:
        st.warning(body="Nenhum gênero encontrado.")

    st.title(body="Cadastrar novo Gênero")
    name = st.text_input(label="Nome do Gênero")
    if st.button(label="Cadastrar"):
        new_genre = genre_service.create_genre(
            name=name,
        )
        if new_genre:
            st.rerun()
        else:
            st.error(body="Erro ao cadastrar o gênero. Verifique os campos.")
