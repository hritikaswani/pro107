import csv 
import pandas as pd
import plotly.express as go
df=pd.read_csv ('data2.csv')
mean=df.groupby(['student_id','level'],as_index=False)['attempt'].mean()
graph=go.scatter(mean,x='student_id',y='level',size='attempt',color='attempt')
graph.show()