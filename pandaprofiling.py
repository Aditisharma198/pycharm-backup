import pandas as  pd
from pandas_profiling import ProfileReport

wdata=pd.read_csv('netflix_titles.csv')
Report=ProfileReport(wdata)
Report.to_file(output_file='Report.html')