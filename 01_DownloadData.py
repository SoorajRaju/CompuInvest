from pandas.io.data import DataReader
from datetime import datetime
import matplotlib.pyplot as plt
from googlefinance import getQuotes
import json
import numpy as np

StartDate = datetime(2016, 1, 1, 0, 00)
EndDate = datetime(2016, 5, 1, 0, 00)
BSE = DataReader("^BSESN",  'yahoo', StartDate, EndDate)
SBI = DataReader("SBIN.BO", 'yahoo', StartDate, EndDate)
LT = DataReader("LT.BO", 'yahoo', StartDate, EndDate)

print BSE.describe()

#print ibm
plt.figure(1)
plt.subplot(311)
plt.plot(BSE['Adj Close'],'r--')
plt.subplot(312)         
plt.plot(SBI['Adj Close'],'g--')
plt.subplot(313)         
plt.plot(LT['Adj Close'],'b--')

RiskSbi = np.mean(SBI['Adj Close'])/np.std(SBI['Adj Close'])
print RiskSbi
RiskLt = np.mean(LT['Adj Close'])/np.std(LT['Adj Close'])
print RiskLt