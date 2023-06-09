# -*- coding: utf-8 -*-
"""Data_StoryTelling+Alexander Sothmann.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_OB1lI8oJ76I0NPvJCUOO0l57jiQqvLc
"""

import streamlit as st
import pandas as pd
import numpy as np

'''
#### **TITULO:** Evaluación de implemetanción de sistema CRM para la atención a la ciudadania. 

#### **INDICE** 
1. [Introducción](#id1)
2. [Contexto pandemia Covid-19](#id2)
3. [Problematica e impacto](#id3)
4. [Propuesta de mejora](#id4)


![Funciones de la Coordinación de Documentación e Información al Ciudadano](https://i.ibb.co/bLdNyQW/entrega-page-0002.jpg)




'''


DATA_URL = ('https://raw.githubusercontent.com/dataista93/Proyecto-Coderhouse/main/DATOS/df_casos_final.csv')

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data

data_load_state = st.text('Loading data...')
data = load_data(1000000)
data_load_state.text("")

if st.checkbox('Visualizar datos'):
    st.subheader('Tabla')
    st.write(data)