import streamlit as st
import numpy as np
from geomap import geomap_yearly_overview
import pandas as pd

# data import and calculations
latitude_list = [47.4268991755, 47.4151264537, 47.4133813496, 47.4226367328, 47.4048725228 ]
longitude_list = [ 9.383057054, 9.34173656537, 9.34717463867, 9.34185926089, 9.30853184166 ]
circle_size = 50
circle_color = "#4fffff"

#htmlmap = geomap_yearly_overview(latitude_list, longitude_list, circle_size, circle_color)


## Sidebar
st.sidebar.markdown("## Einstellungen")
st.sidebar.markdown("Jahr auswählen um die spezifische Verkehrsdichte anzuzeigen")
year = st.sidebar.slider('Aufzeichnungs Jahr', min_value=2018, max_value=2020, step=1)
st.sidebar.markdown("___")
st.sidebar.markdown("Fahrzeugkategorie")
veh_category = st.sidebar.selectbox("Kategorie auswählen", options=[
    "Bus, Car",
    "Lastenzug",
    "Lastwagen",
    "Lieferwagen",
    "Lieferwagen mit Anhänger",
    "Lieferwagen mit Auflieger",
    "Motorrad",
    "Personenwagen",
    "Personenwagen mit Anhänger",
    "Sattelzug"
    ])
st.sidebar.markdown("Zählerstation auswählen")
count_station = st.sidebar.selectbox("Standort auswählen", options=[
    "Bildweiherstrasse",
    "Fürstenlandstrasse 57",
    "Lerchenfeld",
    "Singenberg",
    "St. Josefen-Strasse",
    "Teufener Strasse 75"
])

# Main 
st.title("Verkehrszählung St. Gallen")
st.write("Auswertung des gesamten Verkehrsflusses an den jeweiligen Aufzeichnungsorten über drei Jahre hinweg")
st.caption("Jahr {}".format(year))
#st.markdown(htmlmap, unsafe_allow_html=True)
data = pd.DataFrame({
    'counter_locations' : ["Bildweiherstrasse", "Fürstenlandstrasse 57", "Lerchenfeld", "Singenberg", "St. Josefen-Strasse"],
    'lat' : [47.4268991755, 47.4151264537, 47.4133813496, 47.4226367328, 47.4048725228],
    'lon' : [9.383057054, 9.34173656537, 9.34717463867, 9.34185926089, 9.30853184166]
})


st.map(data)


st.title("Verkehrszählung nach Fahrzeugkategorie")
st.write("Auswertung des gesamten Verkehrsflusses kategorisiert nach Fahrzeugtyp")
st.caption("Fahrzeugkategorie: {} | Zählungsstandort: {}".format(veh_category, count_station))

df = pd.read_csv("https://github.com/aeberhardhsr/open-data-hack-sg/blob/main/data-preparation/verkehrszahlung.csv")
df_head = pd.

st.write(df_head)