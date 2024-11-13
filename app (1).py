# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LFFA2mfzqlrJ1nUMEZiL11z1h4dOUcMS

# Despliegue

- Cargamos el modelo
- Cargamos los datos futuros
- Preparar los datos futuros
- Aplicamos el modelo para la predicción
"""

#Importamos librerías básicas
import pandas as pd # manipulacion dataframes
import numpy as np  # matrices y vectores
import matplotlib.pyplot as plt #gráfica

#Cargamos el modelo
import pickle
filename = 'modeloFinal_GaviEquipos.pkl'
model, pipe, labelencoder, variables = pickle.load(open(filename, 'rb'))

#Se crea interfaz gráfica con streamlit para captura de los datos

import streamlit as st

st.title('Predicción de presupuesto para invertir videojuegos')

valor_reposicion = st.slider('Valor Reposicion', min_value=0, max_value=7700000, value=0, step=1000)
articulo = st.selectbox('articulo', ['Formaleta', 'Andamios', 'Equipo_multi', 'Herramienta', 'Equipo_Electronico', 'Tableros_Modulares'])
obra = st.selectbox('obra', ['BODEGA METALMEGA', 'AMATISTA LIVING', 'FSCR', 'DEPOSITO JAZA', 'HCH COLOMBIA', 'EBENEZER CONSTRUCCIONES SAS', 'FRANCI ELENA VALENCIA FERNANDEZ', '20 DE JULIO'])

datos = [[articulo, valor_reposicion, obra]]
data = pd.DataFrame(datos, columns=['art_nombre', 'art_vr_reposicion', 'cco_nombre']) #Dataframe con los mismos nombres de variables

# sample_data = {
#     'art_nombre': ['Formaleta'],
#     'art_vr_reposicion': [500000],
#     'cco_nombre': ['BODEGA METALMEGA']
# }

# data = pd.DataFrame(sample_data)

# data

data_preparada = pd.DataFrame(pipe.transform(data), columns=pipe.named_steps['preprocessor'].get_feature_names_out())

Y_fut = model.predict(data_preparada)

data['prediccion'] = labelencoder.inverse_transform(Y_fut)

data