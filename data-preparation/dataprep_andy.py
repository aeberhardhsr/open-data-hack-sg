import pandas as pd

df = pd.read_csv("verkehrszahlung.csv", sep=";", error_bad_lines=False)
#print(df.head(5))
#print(df.columns)

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

# set parameters
year = 2019
category = "Lieferwagen mit Auflieger"
location = "St.Gallen Stadt St.Josefen-Str"

# test query
df = df.groupby(['JAHR', 'NAME_D', 'BEZEICHNUNG'])['TAGESTOTAL'].sum()
print(df.head(50))
#result = df.loc[(df['BEZEICHNUNG'] == location) & (df['JAHR'] == year) & (df['NAME_D'] == category)]['TAGESTOTAL'].sum()
#print(result)