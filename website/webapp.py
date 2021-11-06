import streamlit as st
import numpy as np

# data import and calculations


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

st.title("Verkehrszählung nach Fahrzeugkategorie")
st.write("Auswertung des gesamten Verkehrsflusses kategorisiert nach Fahrzeugtyp")
st.caption("Fahrzeugkategorie: {} | Zählungsstandort: {}".format(veh_category, count_station))