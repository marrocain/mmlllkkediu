import pandas as pd
import seaborn as sns

root = "./"
outlier_dataframe = pd.read_csv(root+'data.csv')
print (outlier_dataframe.head())
print (outlier_dataframe.info())
sns_plot=sns.pairplot(outlier_dataframe,hue ='Class')
sns_plot.savefig("output.png")

# Nombre d’instances dans le dataframe :
nb_lignes=outlier_dataframe.shape[0]
print(nb_lignes)
# Decompte du nombre d’instance de chaque classe dans le dataframe
series=outlier_dataframe['Class'].value_counts()
print(series)