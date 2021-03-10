
import pandas as pd
from matplotlib import pyplot as plt


df= pd.read_csv('stud.txt', sep=" ")

df.head()


x=df.loc[:,"course"]
print(x)


dfz=df
c=dfz['course'].value_counts()
print(c)

c.plot(x ='course', y='occurence', kind = 'bar')
plt.show()


c.plot.pie(y='No of students',figsize=(5, 5),autopct='%1.1f%%', startangle=90)
plt.show()



