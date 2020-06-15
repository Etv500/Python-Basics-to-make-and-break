# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 15:00:52 2017

@author: elvis
"""




#import matplotlib.pyplot
#year=[1999,2000,2001,2002]
#gdp=[52000, 55000, 56000, 57000]
#matplotlib.pyplot.plot(year, gdp)


import matplotlib.pyplot as plt
year=[1999,2000,2001,2002]
gdp=[52000, 55000, 56000, 57000]
plt.plot(gdp, year)


#sotto vedi lo scatter e l histogram, se li lascio attivi mi mischia i grafici 
#non so come dividerli va be non serve ora

y=[1999,2000,2001,2002]
g=[52000, 55000, 56000, 57000]
plt.scatter(y, g)  #etc. uguale per tutti i tipi di grafico


values=[1,2,3,8,6,4,7,8,9,5,4]
plt.hist(values, bins=3)  #bins sono i segmenti considerati in asse x




