import streamlit as st
import numpy as np
import pandas as pd

 
## Sidebar
st.sidebar.markdown("## Einstellungen")
st.sidebar.markdown("Jahr auswählen um die spezifische Verkehrsdichte anzuzeigen")
year = st.sidebar.radio("Jahr auswählen", ("2018", "2019", "2020"))
st.sidebar.markdown("Zählerstation auswählen")
count_station_year = st.sidebar.selectbox("Standort auswählen", options=[
    "St.Gallen Stadt Biderstr.",     
    "St.Gallen Stadt Bildweiherstr.",     
    "St.Gallen Stadt Biserhofstr. 7",     
    "St.Gallen Stadt Bruggen",     
    "St.Gallen Stadt Burgstr. 59",     
    "St.Gallen Stadt Dufour/Winkelr",      
    "St.Gallen Stadt Dufourstr. 4",      
    "St.Gallen Stadt Favrestr. 5",      
    "St.Gallen Stadt Flurhofstr. 68",      
    "St.Gallen Stadt Fürstenlstr. 57",     
    "St.Gallen Stadt Gaiserwaldstr.",    
    "St.Gallen Stadt Gallusst./Webergasse",    
    "St.Gallen Stadt Geltenwilenstr",    
    "St.Gallen Stadt Gerhaldenstr.21",    
    "St.Gallen Stadt Grossackers. 1",    
    "St.Gallen Stadt Guisanstr. 40",    
    "St.Gallen Stadt Heiligkreuz",    
    "St.Gallen Stadt Herisauer/Schranke",    
    "St.Gallen Stadt Herisauerst.58",    
    "St.Gallen Stadt Industriest.13",    
    "St.Gallen Stadt Kirche Neudorf",    
    "St.Gallen Stadt Kn.Neudorf neu",    
    "St.Gallen Stadt Kolumb/Heiligk",    
    "St.Gallen Stadt Kolumba/Heimat",    
    "St.Gallen Stadt Lerchenfeld",    
    "St.Gallen Stadt Lerchenfeldstr",    
    "St.Gallen Stadt Lerchental",    
    "St.Gallen Stadt Letzistr.",    
    "St.Gallen Stadt Lukasstr. 30",    
    "St.Gallen Stadt Moosbruggst. 2",    
    "St.Gallen Stadt Mühlegg",    
    "St.Gallen Stadt Müller-Fried.2",    
    "St.Gallen Stadt Ob/Teufen. neu",    
    "St.Gallen Stadt Oberstr. 75",    
    "St.Gallen Stadt Oberstr/Ahorns",    
    "St.Gallen Stadt Post Langgasse",    
    "St.Gallen Stadt Rötelibrücke",    
    "St.Gallen Stadt Schwarzer Bäre",    
    "St.Gallen Stadt Singenberg",    
    "St.Gallen Stadt Sonnenh./Peter",    
    "St.Gallen Stadt Speicherstr 54",    
    "St.Gallen Stadt Splügen/Bachst",    
    "St.Gallen Stadt St.Fiden(neu)",    
    "St.Gallen Stadt St.Jakob-Str.5",    
    "St.Gallen Stadt St.Josefen-Str",    
    "St.Gallen Stadt St.Leonhard Br",    
    "St.Gallen Stadt Steinach/Sonne",    
    "t.Gallen Stadt Turnerstr. 30",  
    "t.Gallen Stadt Wildeggstr 44"  
], key=1)
st.sidebar.markdown("___")


year_radio = st.sidebar.radio("Jahr auswählen", ("2019", "2020"))
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
    "St.Gallen Stadt Bildweiherstr.",
    "St.Gallen Stadt Lerchenfeld",          
    "St.Gallen Stadt Singenberg",           
    "St.Gallen Stadt St.Josefen-Str",       
    "St.Gallen Stadt Teufener Str.75"
])


### begin data preparation for first map ###

dfg = pd.read_csv("verkehrszahlung_gesamt_2018_2020.csv", sep=";", error_bad_lines=False).fillna(0) 
# drop non usable columns
dfg = dfg.drop (dfg.columns[[0,4,5,6,8,9,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,32]], axis=1)
#insert new columns JAHR und Längengrad
dfg.insert(4, "JAHR", value=None)
dfg.insert(2, "Longitude", value=None)
#extract year from DATUM
dfg['JAHR'] = dfg['DATUM'].str.slice(0,4)
#drop column DATUM
dfg = dfg.drop (dfg.columns[[3]], axis=1)
# split the standort columnt to extract coordinates
dfg[['Latitude','Longitude']] = dfg['STANDORT'].str.split(',',1, expand=True)
# drop column
dfg = dfg.drop (dfg.columns[1], axis=1)
#set columns in right order
dfg = dfg[['BEZEICHNUNG', 'Longitude', 'Latitude', 'RICHTUNG', 'JAHR', 'TAGESTOTAL']]

result1 = dfg.loc[(dfg['JAHR'] == year) & (dfg['BEZEICHNUNG'] == count_station_year)]['TAGESTOTAL'].sum()
### end data preparation for first map ###



### begin data preparation for second map ###

df = pd.read_csv("verkehrszahlung.csv", sep=";", error_bad_lines=False)
# drop non usable columns
df = df.drop([
    'WOCHENTAG',
    'ARBEITSTAG',
    'KENNZAHL',
    'RICHTUNG',
    'ORT-RICHTUNG ID',
    'KLASSE',
    'SWISS10GROUP',
    'SWISS7GROUP',
    'SWISS6GROUP',
    '1', '2', '3', '4',
    '5', '6', '7', '8',
    '9', '10', '11', '12',
    '13', '14', '15', '16',
    '17', '18', '19', '20',
    '21', '22', '23', '24'], 1)

# replace chars in columns
df['STANDORT'] = df['STANDORT'].str.replace('"', '')
df['NAME_D'] = df['NAME_D'].str.replace('"', '')

# split the standort columnt to extract coordinates
df[['Latitude','Longitude']] = df['STANDORT'].str.split(',',expand=True)

# extract year for slider on website
df['JAHR'] = pd.DatetimeIndex(df['DATUM']).year

# drop non used columns
df = df.drop(['STANDORT', 'DATUM'], 1)

result2 = df.loc[(df['BEZEICHNUNG'] == count_station) & (df['JAHR'] == int(year_radio)) & (df['NAME_D'] == veh_category)]['TAGESTOTAL'].sum()

### end of data preparation ###

# Main 
st.title("Verkehrszählung St. Gallen")
st.write("Auswertung des gesamten Verkehrsflusses an den jeweiligen Aufzeichnungsorten über drei Jahre hinweg")

resultlat = dfg.loc[(dfg['BEZEICHNUNG'] == count_station_year)]['Latitude'].head(1)
resultlon = dfg.loc[(dfg['BEZEICHNUNG'] == count_station_year)]['Longitude'].head(1)
st.write(resultlat, resultlon)
# first map

data = pd.DataFrame({
    'counter_locations' : [count_station_year],
    'lat' : [float(resultlat)],
    'lon' : [float(resultlon)]})


st.map(data)
#resultlongitude = df.loc von result2 annähern

col1, col2 = st.columns(2)
col1.metric("Jahr", year)
col2.metric("Fahrzeugzähler", int(result1), "5%")
st.metric("Standort", count_station_year)
st.markdown("___")

st.title("Verkehrszählung nach Fahrzeugkategorie")
st.write("Auswertung des gesamten Verkehrsflusses kategorisiert nach Fahrzeugtyp")

# second map
data2 = pd.DataFrame({
    'counter_locations' : ["Bildweiherstrasse", "Fürstenlandstrasse 57", "Lerchenfeld", "Singenberg", "St. Josefen-Strasse"],
    'lat' : [47.4268991755, 47.4151264537, 47.4133813496, 47.4226367328, 47.4048725228],
    'lon' : [9.383057054, 9.34173656537, 9.34717463867, 9.34185926089, 9.30853184166]})

st.map(data2)

col1, col2 = st.columns(2)
col1.metric("Fahrzeugzähler", int(result2), "5%")
col2.metric("Jahr", year_radio)
st.metric("Kategorie", veh_category)
st.metric("Standort", count_station)