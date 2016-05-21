from pandas.io.data import DataReader
from datetime import datetime
import matplotlib.pyplot as plt
from googlefinance import getQuotes
import json
import numpy as np
import matplotlib.ticker as plticker

StartDate = datetime(2016, 1, 2, 0, 00)
EndDate = datetime.now()

def Plotfig(Stock,Param):
    n = 6
    fig = plt.figure()
    ax = plt.plot(Stock.index,Stock[Param])
    plt.xticks(rotation=30)
    ticks = ax.xaxis.get_ticklocs()
    ticklabels = [l.get_text() for l in ax.xaxis.get_ticklabels()]
    ax.xaxis.set_ticks(ticks[::n])
    ax.xaxis.set_ticklabels(ticklabels[::n])
    ax.figure.show()
    
print "Total number of days - %s" %str(EndDate-StartDate)

BSE = DataReader("^BSESN",  'yahoo', StartDate, EndDate)
print "Number of Business days - %s days" %np.count_nonzero(BSE.Open)
SBIBO = DataReader("SBIN.BO", 'yahoo', StartDate, EndDate)
SBINS = DataReader("SBIN.NS", 'yahoo', StartDate, EndDate)
LT = DataReader("LT.BO", 'yahoo', StartDate, EndDate)
TIS = DataReader("TATASTEEL.BO", 'yahoo', StartDate, EndDate)
ONGC = DataReader("ONGC.BO", 'yahoo', StartDate, EndDate)
#print BSE.describe()

#print ibm
plt.figure(1)
#plt.subplots(2,2)
ax = plt.subplot(511)
ax.set_title("BSE")
ax.plot(BSE.index,BSE['Adj Close'],'r-')

ax = plt.subplot(512)
plt.title(figure_title, y=1.08)
#ax.set_title("SBI",fontsize=12,location='left')
plt.plot(SBIBO.index,SBIBO['Adj Close'],'g-')

ax = plt.subplot(513)
ax.set_title("L&T")       
plt.plot(LT.index,LT['Adj Close'],'b-')

ax = plt.subplot(514)
ax.set_title("Tata Steel")        
plt.plot(TIS.index,TIS['Adj Close'],'b-')

ax = plt.subplot(515)
ax.set_title("ONGC")        
plt.plot(ONGC.index,ONGC['Adj Close'],'b-')

RiskBSE = np.mean(BSE['Adj Close'])/np.std(BSE['Adj Close'])
print "BSE - %s" %RiskBSE
RiskSbi = np.mean(SBIBO['Adj Close'])/np.std(SBIBO['Adj Close'])/RiskBSE*100
print "SBI - %s" %RiskSbi
RiskLt = np.mean(LT['Adj Close'])/np.std(LT['Adj Close'])/RiskBSE*100
print "L&T - %s" %RiskLt
RiskTIS = np.mean(TIS['Adj Close'])/np.std(TIS['Adj Close'])/RiskBSE*100
print "Tata Steel - %s" %RiskTIS
RiskONGC = np.mean(ONGC['Adj Close'])/np.std(ONGC['Adj Close'])/RiskBSE*100
print "ONGC - %s" %RiskONGC

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot(ONGC['Adj Close'],'b--')
ax1.set_ylabel('ONGC', color='b')
for tl in ax1.get_yticklabels():
    tl.set_color('b')

ax2 = ax1.twinx()
ax2.plot(BSE['Adj Close'], 'r--')
ax2.set_ylabel('BSE', color='r')
for tl in ax2.get_yticklabels():
    tl.set_color('r')
Plotfig(BSE,'Adj Close')

