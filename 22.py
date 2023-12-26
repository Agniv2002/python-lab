import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
data=pd.read_csv("tips.csv")
print(f"{data.head(10)}")

#scatter plot
sns.scatterplot(data=data,x="total_bill",y="tip")
plt.title("Scatter plot")
plt.show()


#line Chart
sns.lineplot(data=data,x="day",y="tip",ci=None)
plt.title("line chart")
plt.show()


#bar chart
plt.figure(figsize=(10, 6)) 
sns.barplot(data=data,x="day",y="tip",ci=None)
plt.title("bar Chart")
plt.show()

#histogram 
plt.hist(data["total_bill"],bins=20)
plt.show()
