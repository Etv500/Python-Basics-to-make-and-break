

#how to import data from csv with pandas

import pandas as pd


#queste due righe servono solo se vuoi stampare tutti i dati per intero, 
#pd.set_option('display.max_columns', None)
#pd.set_option('display.max_rows', None)

#ne mostro 30 intanto
pd.set_option('display.max_columns', 30)
pd.set_option('display.max_rows', 30)



GBPJPY= pd.read_csv("C:\Users\elvis\Desktop\Trading and Algos\GBPJPYdaily19932017.csv", names=["date", "time", "open", "high", "low", "close", "volume"])
#ci ho aggiunto io l'headeings xk non c era, usando names...


#print(GBPJPY["close"])   #printo solo la colonna close
#print(GBPJPY.loc[1])    #printo solo una riga
#print(GBPJPY.loc[1, "close"])   #printo una cella specifica row 1 col  del close
#print(GBPJPY)



#GBPJPY["percvariationsmissing"]=[1,1,1,1,1,1,1,1,1,1,1,1,1] #per aggiungere una colonna ma dovrei scrivire 6198 items


#creo e printo una nuova colonna data da high-low
GBPJPY["high-low"]=GBPJPY["high"]-GBPJPY["low"]

#print(GBPJPY["high"])
#print(GBPJPY["low"])
print(GBPJPY["high-low"])

#print(GBPJPY.groupby('high'))

