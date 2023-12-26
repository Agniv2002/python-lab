import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns

data=pd.read_csv("results.csv")
pass_fail_count={}

for sub in data.columns[1:-3]:
    passcount= len(data[data[sub]>=50])
    failcount=len(data[data[sub]<50])
    pass_fail_count[sub]={'pass':passcount,'fail':failcount}

print(f"{pass_fail_count}")



overallPass=sum(pass_fail_count[sub]['pass'] for sub in pass_fail_count)

overallFail=sum(pass_fail_count[sub]['fail'] for sub in pass_fail_count)
print(f"overall pass is {overallPass} and overall fail is {overallFail}")

plt.figure(figsize=(8, 6))
sns.scatterplot(x='Maths', y='Science', data=data)
plt.title('Scatter Plot of Maths vs Science')
plt.xlabel('Maths')
plt.ylabel('Science')
plt.show()

# Line Chart
plt.figure(figsize=(8, 6))
abc=pd.DataFrame(pass_fail_count).T 
abc.plot(kind="line")
# sns.lineplot(x='Student', y='Maths', data=data)
plt.title('Line Chart of pass and fail Scores')
plt.xlabel('Student')
plt.ylabel('Score')
plt.show()

# Bar Chart
pass_fail_df = pd.DataFrame(pass_fail_count).T
pass_fail_df.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title('Pass/Fail Count for Each Subject')
plt.xlabel('Subject')
plt.ylabel('Count')
plt.legend(title='Result')
plt.show()

# Histogram
data.hist(data.columns[1:-3],figsize=(12, 8))
plt.suptitle('Histograms of Subject Scores', y=0.95)
plt.show()
