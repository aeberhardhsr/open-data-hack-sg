from re import X
import pandas as pd
import numpy as np
from IPython.display import display
import io
#import requests



#df = pd.read_csv("verkehrszahlung.csv", sep=";", error_bad_lines=False).fillna(0)


dfg = pd.read_csv("verkehrszahlung_gesamt_2018_2020.csv", sep=";", error_bad_lines=False).fillna(0) 

dfg = dfg.drop (dfg.columns[[0,4,5,6,8,9,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,32]], axis=1)
dfg.insert(4, "JAHR", value=None)
dfg.insert(2, "Longitude", value=None)
dfg['JAHR'] = dfg['DATUM'].str.slice(0,4)
dfg = dfg.drop (dfg.columns[[3]], axis=1)
dfg[['Longitude','Laltitude']] = dfg['STANDORT'].str.split(',',1, expand=True)
dfg = dfg.drop (dfg.columns[1], axis=1)
dfg = dfg[['BEZEICHNUNG', 'Longitude', 'Laltitude', 'RICHTUNG', 'JAHR', 'TAGESTOTAL']]

#display[(dfg['JAHR'] == 2020) & (dfg['BEZEICHNUNG'] == 'St.Gallen Stadt Gaiserwaldstr.')]

#def Total(year, region):
    #s = dfg[(dfg['JAHR'] == year) & (dfg['BEZEICHNUNG'] == region)]
   # dfg = dfg.groupby(['JAHR'] == year) & (dfg['BEZEICHNUNG'] == region)['TAGESTOTAL'].sum()
   # sum = s['TAGESTOTAL'].sum()
    #display (sum)

#dfg = dfg.groupby(['JAHR', 'BEZEICHNUNG'])['TAGESTOTAL'].sum()
#dfg = dfg.groupby(['JAHR', 'BEZEICHNUNG'])['TAGESTOTAL'].sum()

year = 2018
region = "St.Gallen Stadt Gaiserwaldstr."


#dfg = dfg.groupby(['JAHR'] == year & ['BEZEICHNUNG'] == region)['TAGESTOTAL'].sum()

result = dfg.loc[(dfg['JAHR'] == year) & (dfg['BEZEICHNUNG'] == region)]['TAGESTOTAL'].sum()

#result = df.loc[(df['BEZEICHNUNG'] == count_station) & (df['JAHR'] == int(year_radio)) & (df['NAME_D'] == veh_category)]['TAGESTOTAL'].sum()

display(result.head())


#Total(2018, "St.Gallen Stadt Gaiserwaldstr.")


#def ganz(Jahr, Bezeichnung):
 #   J = dfg.loc[dfg['JAHR']==Jahr][dfg['BEZEICHNUNG']=="Lastwagen"]
  #  s = J['TAGESTOTAL'].sum()
   # display(s)


#ganz(2020, "St.Gallen Stadt Gaiserwaldstr.")
#df = df.drop (df.columns[[3,4,5,6,8,9,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37]], axis=1)


#def Total(year, region):
#    dfg.loc[(df['JAHR'] == year) & (df['BEZEICHNUNG'] == region), 'TAGESTOTAL'].sum()


#df.loc[df['ORT-ID']==10944][df['NAME_D']=="Bus, Car"]
#TotJosefenbc = Josefenbc['TAGESTOTAL'].sum()
#Josefenlz = df.loc[(df['ORT-ID'] == 10944) & (df['NAME_D'] == "Lastenzug"), 'TAGESTOTAL'].sum()
#TotJosefenlz = Josefenlz['TAGESTOTAL'].sum()
#Josefenlkw = df.loc[df['ORT-ID']==10944][df['NAME_D']=="Lastwagen"]
#TotJosefenlkw = Josefenlkw['TAGESTOTAL'].sum()
#Josefenlw = df.loc[df['ORT-ID']==10944][df['NAME_D']=="Lieferwagen"]
#TotJosefenlw = Josefenlw['TAGESTOTAL'].sum()
#Josefenlwan = df.loc[df['ORT-ID']==10944][df['NAME_D']=="Lieferwagen mit Anhänger"]
#TotJosefenlwan = Josefenlwan['TAGESTOTAL'].sum()
#Josefenlwau = df.loc[df['ORT-ID']==10944][df['NAME_D']=="Lieferwagen mit Auflieger"]
#TotJosefenbc = Josefenlwau['TAGESTOTAL'].sum()
#Josefenmot = df.loc[df['ORT-ID']==10944][df['NAME_D']=="Motorrad"]
#TotJosfenmot = Josefenmot['TAGESTOTAL'].sum()
#Josefenpw = df.loc[df['ORT-ID']==10944][df['NAME_D']=="Personenwagen"]
#TotJosefenpw = Josefenpw['TAGESTOTAL'].sum()
#Josefenpwa = df.loc[df['ORT-ID']==10944][df['NAME_D']=="Personenwagen mit Anhänger"]
#TotJosefenpwa = Josefenpwa['TAGESTOTAL'].sum()
#Josefensat = df.loc[df['ORT-ID']==10944][df['NAME_D']=="Sattelzug"]
#TotJosefensat = Josefensat['TAGESTOTAL'].sum()



#Anzahl pro Jahr 
#AnzahlBCJosefen = Josefenbc['TAGESTOTAL'].sum()
#Josefenlz = df.loc[df['ORT-ID']==10944], ['NAME_D']=="Lastenzug"
#Josefenlkw = df.loc[df['ORT-ID']==10944], ['NAME_D']=="Lastwagen"
#Josefenlw = df.loc[df['ORT-ID']==10944], ['NAME_D']=="Lieferwagen"
#Josefenlwan = df.loc[df['ORT-ID']==10944], ['NAME_D']=="Lieferwagen mit Anhänger"
#Josefenlwau = df.loc[df['ORT-ID']==10944], ['NAME_D']=="Lieferwagen mit Auflieger"
#Josefenmot = df.loc[df['ORT-ID']==10944], ['NAME_D']=="Motorrad"
#Josefenpw = df.loc[df['ORT-ID']==10944], ['NAME_D']=="Personenwagen"
#Josefenpwa = df.loc[df['ORT-ID']==10944], ['NAME_D']=="Personenwagen mit Anhänger"
#Josefensat = df.loc[df['ORT-ID']==10944], ['NAME_D']=="Sattelzug"









#Fürsten = df.loc[df['ORT-ID']==10908]
#Bild = df.loc[df['ORT-ID']==11077]
#Teufen = df.loc[df['ORT-ID']==11287]

#JosBC = df.loc[df['NAME_D']=="Bus, Car"]

#display(JosBC)

#AnzJosefen = Josefen['TAGESTOTAL'].sum()
#AnzSingen = Singen['TAGESTOTAL'].sum()
#AnzLerchen = Lerchen['TAGESTOTAL'].sum()
#AnzFürsten = Fürsten['TAGESTOTAL'].sum()
#nzBild = Bild['TAGESTOTAL'].sum()
#AnzTeufen = Teufen['TAGESTOTAL'].sum()

#display(Josefen.head(5))


#Josefens = df.loc[df['ORT-ID']==10944], ['NAME_D']=="Bus, Car"
