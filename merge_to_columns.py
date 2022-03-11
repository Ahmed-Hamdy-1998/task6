
import pandas as pd
technologies = {
    'Courses':["Spark","PySpark","Python","pandas"],
    'Fee' :[20000,25000,22000,30000],
    'Duration':['30days','40days','35days','50days'],
              }
index_labels=['r1','r2','r3','r4']
df1 = pd.DataFrame(technologies,index=index_labels)

technologies2 = {
    'Courses':["Spark","Java","Python","Go"],
    'Discount':[2000,2300,1200,2000]
              }
index_labels2=['r1','r6','r3','r5']
df2 = pd.DataFrame(technologies2,index=index_labels2)
technologies3 = {
    'Instructor': ["Jerry", "Tom", "Smith", "John"],
    'Courses': ["Spark", "Java", "Python", "Scala"]
}
index_labels3 = ['r1','r6','r3','r7']
df3 = pd.DataFrame(technologies3, index=index_labels3)

print(df1)
print(df2)
print(df3)











