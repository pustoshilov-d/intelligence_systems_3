import pandas as pd

data = pd.read_csv('train.csv')

print(data)
print(data.describe())


print('male: ', len(data[data['Sex'] == 'male']), ', female: ', len(data[data['Sex'] == 'female']))
print('Survived: ', round(data['Survived'].mean()*100,2))
print('1st class: ', round(len(data[data['Pclass'] == 1])/len(data)*100,2))
print('Age: ', round(data['Age'].mean()), round(data['Age'].median()))
print('Pearson corr: ', data[['SibSp','Parch']].corr(method='pearson'))


data[['FirstName', 'OtherName']] = data['Name'].str.replace('[^a-zA-Z ]', '').str.split(' ', 1, expand = True)

ans = data[data['Sex'] == 'female'].groupby(['FirstName'])['FirstName'].agg(['count']).sort_values(by='count', ascending=False).iloc[0]
print('Popular female name: ',data[data['Sex'] == 'female'].groupby(['FirstName'])['FirstName'].agg(['count']).sort_values(by='count', ascending=False).iloc[0])