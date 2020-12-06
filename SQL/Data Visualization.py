#Data Visualization

import pandas as pd 
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

fifa_filepath = "../input/fifa.csv"
fifa_data = pd.read_csv(fifa_filepath, index_col="Date", parse_dates=True)


fifa_data.head()
fifa_data.tail()

plt.figure(figsize=(16,6))
plt.title("Title")
plt.xlabel("Label")
plt.ylabel("Label")
plt.show()

#Line Plot
sns.lineplot(data=fifa_data)

#Bar Chart
sns.barplot(x=flight_data.index, y=flight_data['NK'])

#Heat Map
sns.heatmap(data=flight_data, annot=True)

#Scatter Plot
sns.scatterplot(x=insurance_data['bmi'], y=insurance_data['charges'])

#Adding Regression Line on Scatter Plot
sns.regplot(x=insurance_data['bmi'], y=insurance_data['charges'])

#Color coded scatterplot
sns.scatterplot(x=insurance_data['bmi'], y=insurance_data['charges'], hue=insurance_data['smoker'])

#Add 2 regression line on scatterplot
sns.lmplot(x="bmi", y="charges", hue="smoker", data=insurance_data)

#Categorical Scatter Plot
sns.swarmplot(x=insurance_data['smoker'],
				y=insurance_data['charges'])

#Histograms
sns.distplot(a=iris_data['Petal Length (cm)'], kde=False)

#Density Plots - Kernel Density Plot(KDE)
sns.kdeplot(data=iris_data['Petal Length (cm)'], shade=True)

#2D KDE plot
sns.jointplot(x=iris_data['Petal Length (cm)'], y=iris_data['Sepal Width (cm)'], kind='kde')

#Plot 3 Histograms
sns.distplot(a=iris_set_data['Petal Length (cm)'], label="Iris-setosa", kde=False)
sns.distplot(a=iris_ver_data['Petal Length (cm)'], label="Iris-versicolor", kde=False)
sns.distplot(a=iris_vir_data['Petal Length (cm)'], label="Iris-virginica", kde=False)

plt.title("Histogra of Petal Lengths, by Species")
plt.legend()

#Changing Styles
sns.set_style("dark")