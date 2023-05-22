#%%

# Importar las librerías necesarias
import numpy as np
import pandas as pd
import folium
from folium import plugins

# Guardar en la variable 'ruta' la url del dataset 
ruta = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vS4jSNNNr3_z6lhqRlyBIsAbVfozhSr_XAl62TF62bnzu11zlgpI3iuB0XllfUWEH4KsfdHIAYbLqSc/pub?output=csv'

# Cargar el dataset a partir de la ruta establecida
df = pd.read_csv(ruta, sep=',')

# Correcion del formato de coordenadas
df['seguridad.latitud'] = df['seguridad.latitud'].str.replace('.', '').str.replace(' ', '')
df['seguridad.longitud'] = df['seguridad.longitud'].str.replace('.', '').str.replace(' ', '')

df['seguridad.latitud'] = df['seguridad.latitud'].str[0:1] + '.' + df['seguridad.latitud'].str[1:]
df['seguridad.longitud'] = df['seguridad.longitud'].str[0:3] + '.' + df['seguridad.longitud'].str[3:]

df['seguridad.latitud'] = df['seguridad.latitud'].astype(float)
df['seguridad.longitud'] = df['seguridad.longitud'].astype(float)

# Eliminar las filas sin coordenadas
df.dropna(subset=['seguridad.latitud', 'seguridad.longitud'], inplace=True)

# Generar mapa
m = folium.Map(location=[6.25184, -75.56359], tiles="openstreetmap", zoom_start=13)

# Agregar los puntos al mapa
locations = list(zip(df['seguridad.latitud'], df['seguridad.longitud']))
cluster = plugins.MarkerCluster(locations=locations,                     
          popups=df["seguridad.nombre_barrio"].tolist())  
m.add_child(cluster)
m.save('mapa.html')
# %%
