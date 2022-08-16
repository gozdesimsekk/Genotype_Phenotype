import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

big_data = pd.read_excel("GenotypeandPhenotypeData.xlsx")

phenotypes = big_data.iloc[:,34:]

AFR = phenotypes.groupby("ancestry")
AFR = AFR.get_group("AFR")

AMR = phenotypes.groupby("ancestry")
AMR = AMR.get_group("AMR")

EUR = phenotypes.groupby("ancestry")
EUR = EUR.get_group("EUR")

EAS = phenotypes.groupby("ancestry")
EAS = EAS.get_group("EAS")

SAS = phenotypes.groupby("ancestry")
SAS = SAS.get_group("SAS")

phenotypes = phenotypes.drop(columns=["ancestry","population","sex"])
phen = ['age', 'bmi', 'fasting_glucose','fasting_insulin', 'hdl', 'height', 'ldl','total_cholesterol',
              'triglycerides', 'waist_hip_ratio']

def graphancestry(df):
    #for df in [AFR, AMR, EAS, EUR, SAS]:
    fig, axs = plt.subplots(2,5)

    axs[0, 0].boxplot(df[phen[0]],vert=False)
    axs[0, 0].set_title(phen[0])
    axs[0, 1].boxplot(df[phen[1]], vert=False)
    axs[0, 1].set_title(phen[1])
    axs[0, 2].boxplot(df[phen[2]], vert=False)
    axs[0, 2].set_title(phen[2])
    axs[0, 3].boxplot(df[phen[3]],vert=False)
    axs[0, 3].set_title(phen[3])
    axs[0, 4].boxplot(df[phen[4]],vert=False)
    axs[0, 4].set_title(phen[4])

    axs[1,0].boxplot(df[phen[5]],vert=False)
    axs[1,0].set_title(phen[5])
    axs[1,1].boxplot(df[phen[6]],vert=False)
    axs[1,1].set_title(phen[6])
    axs[1,2].boxplot(df[phen[7]],vert=False)
    axs[1,2].set_title(phen[7])
    axs[1,3].boxplot(df[phen[8]],vert=False)
    axs[1,3].set_title(phen[8])
    axs[1,4].boxplot(df[phen[9]],vert=False)
    axs[1,4].set_title(phen[9])
    
    plt.show()

#graphancestry(big_data)

def histograms():

    for col in phen:
        sns.histplot(data=big_data, x=col, kde=True)
        plt.show()

#histograms()

def outliers():

    # IQR
    for col in phen:
        df = pd.DataFrame()
        Q1 = np.percentile(big_data[col], 25, method='midpoint')
        Q3 = np.percentile(big_data[col], 75, method='midpoint')
        IQR = Q3 - Q1

        maximum = Q3 + (1.5 * IQR)
        minimum = Q1 - (1.5 * IQR)

        for i in big_data[col]:
            if i < minimum or i > maximum:
                df = pd.concat([df,big_data.loc[big_data[col] == i]], axis=0)

        df = pd.concat([df, big_data[col].describe().to_frame()])
        df.to_csv("outlier/{}_outliers.csv".format(col))


#outliers()
#print(big_data.corr(method="pearson"))
#plt.matshow(phenotypes.corr())

f, ax = plt.subplots(figsize=(10, 10))
corr = phenotypes.corr()
sns.heatmap(corr, mask=np.zeros_like(corr, dtype=np.bool), cmap=sns.diverging_palette(220, 10, as_cmap=True),
            square=True, ax=ax)
plt.show() 
