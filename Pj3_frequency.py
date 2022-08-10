import pandas as pd
import matplotlib.pyplot as plt

continents = ["AFR","AMR","EAS","EUR","SAS"]
rslerlist = ["rs762551", "rs4988235", "rs713598",   "rs1726866", "rs10246939", "rs17782313", "rs1800544", "rs5400", "rs1051168", "rs9939609",
         "rs17300539", "rs1800206", "rs1800588", "rs1801282", "rs1801133", "rs7501331", "rs12934922", "rs1256335", "rs602662"]
AFR = pd.DataFrame()
AMR = pd.DataFrame()
EAS = pd.DataFrame()
EUR = pd.DataFrame()
SAS = pd.DataFrame()
#Dataframes filled with according data
for i in rslerlist:
    for j in continents:
        a = pd.read_csv("output/{}/{}.csv".format(i,j),names=rslerlist)
        a = a.iloc[1:,1]
        if j == "AFR":
            AFR = pd.concat([AFR,a],axis=1)
        elif j == "AMR":
            AMR = pd.concat([AMR, a], axis=1)
        elif j == "EAS":
            EAS = pd.concat([EAS, a], axis=1)
        elif j == "EUR":
            EUR = pd.concat([EUR, a], axis=1)
        elif j == "SAS":
            SAS = pd.concat([SAS, a], axis=1)
AFR.columns = rslerlist
AMR.columns = rslerlist
EAS.columns = rslerlist
EUR.columns = rslerlist
SAS.columns = rslerlist
def converter(df):
    heterovals = [["A|C","C|A"],["A|T","T|A"],["A|G","G|A"],["C|T","T|C"],["G|C","C|G"],["T|G","G|T"]]
    for i in range(len(df)):
        for j in range(len(rslerlist)):
            for k,l in heterovals:
                if k == df.iloc[i,j]:
                    df.iloc[i,j] = l
    return df
AFR, AMR, EAS, EUR, SAS = converter(AFR), converter(AMR), converter(EAS), converter(EUR), converter(SAS)

total_number = []
for df in [AFR, AMR, EAS, EUR, SAS]:
    total_number.append(df.count(axis=1))

AFR_tot = len(total_number[0])
AMR_tot = len(total_number[1])
EAS_tot = len(total_number[2])
EUR_tot = len(total_number[3])
SAS_tot = len(total_number[4])

AFR_values = []
AMR_values = []
EAS_values = []
EUR_values = []
SAS_values = []

for i in rslerlist:
    AFR_values.append(AFR[i].value_counts().to_dict())
    AMR_values.append(AMR[i].value_counts().to_dict())
    EAS_values.append(EAS[i].value_counts().to_dict())
    EUR_values.append(EUR[i].value_counts().to_dict())
    SAS_values.append(SAS[i].value_counts().to_dict())

values_list = [AFR_values, AMR_values, EAS_values, EUR_values, SAS_values]


def adict(dict1,dict2):
    for i in dict1.keys():
        for j in dict2.keys():
            if i == j:
                dict1[i] = dict1[i] + dict2[j]

    for j in dict2.keys():
        if j not in dict1.keys():
            a = {j : dict2[j]}
            dict1.update(a)
    return dict1

def freq_calc(df_values, tot):

    df_values_frequency = []
    df_values_allel_frequency = []

    for b in df_values:
        df_values_frequency_rs = {}
        df_values_allel_rs1 = {}
        df_values_allel_rs2 = {}
        for j in ["A", "C", "T", "G"]:
            for k in ["A", "C", "T", "G"]:

                if "{}|{}".format(j, k) in b.keys():

                    df_values_frequency_rs.update({"{}|{}".format(j, k): ((b["{}|{}".format(j, k)] / tot) * 100)})
                    if j == k:
                        df_values_allel_rs1.update({ j: ((b["{}|{}".format(j, k)] * 2) / tot) *50})
                    elif j != k:
                        df_values_allel_rs2.update({j: (b["{}|{}".format(j, k)] / tot) *50})
                        df_values_allel_rs2.update({k: (b["{}|{}".format(j, k)] / tot) *50})
        df_values_allel_rs = adict(df_values_allel_rs1, df_values_allel_rs2)
        df_values_allel_frequency.append(df_values_allel_rs)
        df_values_frequency.append(df_values_frequency_rs)

    return df_values_frequency, df_values_allel_frequency

#genotype and allele frequency
AFR_frequency, AFR_allel_frequency = freq_calc(AFR_values, AFR_tot)
AMR_frequency, AMR_allel_frequency = freq_calc(AMR_values, AMR_tot)
EAS_frequency, EAS_allel_frequency = freq_calc(EAS_values, EAS_tot)
EUR_frequency, EUR_allel_frequency = freq_calc(EUR_values, EUR_tot)
SAS_frequency, SAS_allel_frequency = freq_calc(SAS_values, SAS_tot)
#visualization
def plotfreq(dffreq):
    ee = dict(zip(rslerlist, dffreq))
    bb = pd.DataFrame(ee).T
    pp = bb.columns
    unsymbol = []
    symbol = '|'
    for element in pp:
        temp = ""
        for ch in element:
            if ch not in symbol:
                temp += ch
        unsymbol.append(temp)
    bb.columns = unsymbol
    ax = bb.plot(kind='barh', stacked=True)
    plt.xlabel("% Frequency")
    '''for p in ax.patches:
        h, w, x, y = p.get_height(), p.get_width(), p.get_x(), p.get_y()
        text = f'{w :0.2f} %'
        ax.annotate(text=text, xy=(x + w / 2, y + h / 2), ha='left',
                       va='center_baseline', color='black', size=8)'''
    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height * 0.1,
                        box.width, box.height * 0.9])
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15),
                 fancybox=True, shadow=True, ncol=5)

    plt.show()

'''#Genotip görselleri'''
#AMRplotG = plotfreq(AMR_frequency)
#EASplotG = plotfreq(EAS_frequency)
#EURplotG = plotfreq(EUR_frequency)
#SASplotG = plotfreq(SAS_frequency)
'''#Alel görselleri'''
#AFRplotA = plotfreq(AFR_allel_frequency)
#AMRplotA = plotfreq(AMR_allel_frequency)
#EASplotA = plotfreq(EAS_allel_frequency)
#EURplotA = plotfreq(EUR_allel_frequency)
#SASplotA = plotfreq(SAS_allel_frequency)
