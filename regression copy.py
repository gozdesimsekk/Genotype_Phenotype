#Regression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
from sklearn import preprocessing
import plotly.express as px
from encoding import genotypes, phenotypes, codominant_encoded, additive_encoded, normalizer
import pandas as pd

enc_phenotypes = phenotypes.drop(columns=["fasting_insulin"])
r_square = pd.DataFrame(index=genotypes.columns, columns=enc_phenotypes.columns)
m_square = pd.DataFrame(index=genotypes.columns, columns=enc_phenotypes.columns)
for i in range(len(genotypes.columns)):
    for j in range(len(enc_phenotypes.columns)):
        X = codominant_encoded.iloc[:,i].values
        y = enc_phenotypes.iloc[:,j].values

        encoder = preprocessing.LabelEncoder()
        y_norm = encoder.fit_transform(y)
        X = X.reshape(len(X),1)
        y_norm = y_norm.reshape(len(y_norm),1)

        x_train, x_test, y_train, y_test = train_test_split(X,y_norm, test_size=0.2, random_state=42)

        regressor = LinearRegression()
        regressor.fit(x_train,y_train)

        #regressor1 = Ridge()
        #regressor1.fit(x_train, y_train)
        #y_pred1 = regressor1.predict(x_test)
        #r_square1.iloc[i, j] = r2_score(y_test, y_pred1)

        #regressor2 = LogisticRegression()
        #regressor2.fit(x_train, y_train)
        #y_pred = regressor2.predict(x_test)
        #r_square2.iloc[i, j] = r2_score(y_test, y_pred)

        y_pred = regressor.predict(x_test)

        r_square.iloc[i,j] = r2_score(y_test,y_pred)
        m_square.iloc[i,j] = mean_squared_error(y_test,y_pred)

        #Shows why we are not getting a meaningful regression result
        '''
        plt.scatter(x_train, y_train, color='red')
        plt.plot(x_train, regressor.predict(x_train), color='blue')
        plt.title('Salary vs Experience (Training set)')
        plt.xlabel(genotypes.columns[i])
        plt.ylabel(phenotypes.columns[j])
        plt.show()
'''
#heatmap
print(r_square)
fig = px.imshow(r_square)
fig.show()