import streamlit as st
import numpy as np
import pandas as pd



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

    dfg = pd.read_csv("verkehrszahlung_gesamt_2018_2020.csv", sep=";", error_bad_lines=False).fillna(0) 
    dfg = dfg.drop (dfg.columns[[4,5,6,8,9,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33]], axis=1)
    dfg.insert(4, "JAHR", value=None)
    dfg['JAHR'] = dfg['DATUM'].str.slice(0, 3)

df = df.drop (df.columns[[3,4,5,6,8,9,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37]], axis=1)
})


st.map(data)


st.title("Verkehrszählung nach Fahrzeugkategorie")
st.write("Auswertung des gesamten Verkehrsflusses kategorisiert nach Fahrzeugtyp")
st.caption("Fahrzeugkategorie: {} | Zählungsstandort: {}".format(veh_category, count_station))


