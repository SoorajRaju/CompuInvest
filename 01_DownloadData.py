from pandas.io.data import DataReader
from datetime import datetime
import matplotlib.pyplot as plt
from googlefinance import getQuotes
import json

BSE = DataReader("^BSESN",  'yahoo', datetime(2016,3,1), datetime(2016,4,20))
SBI = DataReader("SBIN.BO", 'yahoo', datetime(2016,3,1), datetime(2016,4,20))
#print ibm
plt.figure(1)
plt.subplot(211)
plt.plot(BSE['Adj Close'],'r--')
plt.subplot(212)         
plt.plot(SBI['Adj Close'],'g--')