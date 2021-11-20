import pandas as pd

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
dfg[['Longitude','Laltitude']] = dfg['STANDORT'].str.split(',',1, expand=True)
# drop column
dfg = dfg.drop (dfg.columns[1], axis=1)
#set columns in right order
dfg = dfg[['BEZEICHNUNG', 'Longitude', 'Laltitude', 'RICHTUNG', 'JAHR', 'TAGESTOTAL']]

year = "2019"
count_station_year = "St.Gallen Stadt Bildweiherstr."

result1 = dfg.loc[(dfg['BEZEICHNUNG'] == count_station_year) & (dfg['JAHR'] == year)]['TAGESTOTAL'].sum()


print(result1)


















"""
#df = pd.read_csv("verkehrszahlung.csv", sep=";", error_bad_lines=False)
df = pd.read_csv("verkehrszahlung_gesamt_2018_2020.csv", sep=";", error_bad_lines=False)
#print(df.head(5))
#print(df.columns)

# drop non usable columns


# replace chars in columns
df['STANDORT'] = df['STANDORT'].str.replace('"', '')
#df['NAME_D'] = df['NAME_D'].str.replace('"', '')

# split the standort columnt to extract coordinates
df[['Latitude','Longitude']] = df['STANDORT'].str.split(',',expand=True)

# extract year for slider on website
df['JAHR'] = pd.DatetimeIndex(df['DATUM']).year

# drop non used columns
df = df.drop(['STANDORT', 'DATUM'], 1)

# set parameters
year = 2019
category = "Lieferwagen mit Auflieger"
location = "St.Gallen Stadt St.Josefen-Str"

# test query
df = df.groupby(['JAHR', 'BEZEICHNUNG'])['TAGESTOTAL'].sum()
print(df.head(50))
#result = df.loc[(df['BEZEICHNUNG'] == location) & (df['JAHR'] == year) & (df['NAME_D'] == category)]['TAGESTOTAL'].sum()
#print(result)
"""