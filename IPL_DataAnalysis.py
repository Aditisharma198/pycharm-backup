import pandas as pd
from pandas_profiling import ProfileReport
import matplotlib.pyplot as plt
wdata=pd.read_csv('IPl2020Result.csv')
type(wdata)
#print(wdata)
#print(wdata.head(10))
#print(wdata.tail(10))
#print(wdata.shape)
#print(wdata.iloc[0:5,0:3])
#print(wdata.columns)
#print(wdata.dtypes)
#print(wdata.id.unique())
#print(wdata.id.nunique())
#print(wdata.count())
#print(wdata.value_counts())
#print(wdata.info())
#print(wdata.groupby('result_margin').get_group(8))

#Report = ProfileReport(wdata)
#Report.to_file(output_file='ReportIPL.html')

#plt.plot(result_margin,ls='--',linewidth='5',color='r')
#plt.plot(wdata.ball,wdata.over)


ffam={'family' : 'Serif','color':'red', 'size':15}
'''
plt.title('Most Runs Plot',fontdict=ffam)
plt.xlabel('Innings')
plt.ylabel('Runs')
plt.grid(axis='y',color='r',ls='--')
plt.plot(wdata.Inns,wdata.Runs,marker='s',ms='10',mec='r',mfc='k')
plt.show()'''

'''plt.subplot(1,2,1)
plt.plot(wdata.SR)
plt.title('Strike Rate Plot',fontdict=ffam)
plt.subplot(1,2,2)
plt.plot(wdata.BF)
plt.title('Balls Faced Plot',fontdict=ffam)
plt.suptitle('Most Runs Scored Plot')
plt.show()'''

