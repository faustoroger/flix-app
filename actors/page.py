import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

actors = [
    {
        "id": 1,
        "name": "Leonardo Di Caprio",
    },
    {
        "id": 2,
        "name": "Chris Rock",
    },
    {
        "id": 3,
        "name": "Sylvester Stallone",
    },
]


def show_actors():
    st.write("Lista de Atores/Atrizes")

    AgGrid(
        data=pd.DataFrame(actors),
        key="genres_grid",
    )

    st.title(body="Cadastrar novo(a) Ator/Atriz")
    name = st.text_input(label="Nome do(a) Ator/Atriz")
    if st.button(label="Cadastrar"):
        st.success(f'Ator/Atriz "{name}" cadastrado(a) com sucesso')
