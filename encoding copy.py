#Encoding data
import pandas as pd
import numpy as np

dfexcel = pd.read_excel("<PATH>/GenotypeandPhenotypeData.xlsx")
genotypes = dfexcel.iloc[:,1:33]

additive = {"rs762551": {"AA":0, "CA": 1, "AC":1, "CC":2}, "rs4988235": {"AA":0, "GA":1, "AG":1, "GG":2}, "rs713598": {"CC":0, "GC":1, "CG":1, "GG":2},
            "rs1726866": {"AA":0, "GA":1, "AG":1, "GG":2}, "rs10246939": {"CC":0, "TC":1, "CT":1, "TT":2}, "rs17782313": {"CC":0, "TC":1, "CT":1, "TT":2},
            "rs1800544": {"CC":0, "GC":1, "CG":1, "GG":2}, "rs5400": {"AA":0, "GA":1, "AG":1, "GG":2}, "rs1051168": {"GG":0, "TG":1, "GT":1, "TT":2},
            "rs9939609":{"AA":0, "TA": 1, "AT":1, "TT":2}, "rs17300539": {"AA":0, "GA":1, "AG":1, "GG":2}, "rs1800206": {"CC":0, "GC":1, "CG":1, "GG":2},
            "rs1800588": {"CC":0, "TC":1, "CT":1, "TT":2}, "rs1801282": {"CC":0, "GC":1, "CG":1, "GG":2}, "rs1801133": {"AA":0, "GA":1, "AG":1, "GG":2},
            "rs7501331": {"CC":0, "TC":1, "CT":1, "TT":2}, "rs12934922": {"AA":0, "TA": 1, "AT":1, "TT":2}, "rs1256335": {"AA":0, "GA":1, "AG":1, "GG":2},
            "rs602662": {"GG": 0, "AG": 1, "GA": 1, "AA": 2}, "rs4680": {"GG": 0, "AG": 1, "GA": 1, "AA": 2},"rs6265": {"TT": 0, "TC": 1, "CT": 1, "CC": 2},
            "rs12722": {"TT": 0, "TC": 1, "CT": 1, "CC": 2}, "rs1042713": {"GG": 0, "AG": 1, "GA": 1, "AA": 2},"rs1049434": {"TT": 0, "AT": 1, "TA": 1, "AA": 2},
            "rs1800012": {"AA": 0, "AC": 1, "CA": 1, "CC": 2},"rs1800795": {"GG": 0, "GC": 1, "CG": 1, "CC": 2},"rs1815739": {"TT": 0, "TC": 1, "CT": 1, "CC": 2},
            "rs2070744": {"TT": 0, "TC": 1, "CT": 1, "CC": 2},"rs4253778": {"GG": 0, "GC": 1, "CG": 1, "CC": 2},"rs4644994": {"GG": 0, "AG": 1, "GA": 1, "AA": 2},
            "rs8192678": {"TT": 0, "TC": 1, "CT": 1, "CC": 2},"rs11549465": {"TT": 0, "TC": 1, "CT": 1, "CC": 2}}

codominant = {"rs762551": {"AA":0, "CA": 1, "AC":1, "CC":0}, "rs4988235": {"AA":0, "GA":1, "AG":1, "GG":0}, "rs713598": {"CC":0, "GC":1, "CG":1, "GG":0},
            "rs1726866": {"AA":0, "GA":1, "AG":1, "GG":0}, "rs10246939": {"CC":0, "TC":1, "CT":1, "TT":0}, "rs17782313": {"CC":0, "TC":1, "CT":1, "TT":0},
            "rs1800544": {"CC":0, "GC":1, "CG":1, "GG":0}, "rs5400": {"AA":0, "GA":1, "AG":1, "GG":0}, "rs1051168": {"GG":0, "TG":1, "GT":1, "TT":0},
            "rs9939609":{"AA":0, "TA": 1, "AT":1, "TT":0}, "rs17300539": {"AA":0, "GA":1, "AG":1, "GG":0}, "rs1800206": {"CC":0, "GC":1, "CG":1, "GG":0},
            "rs1800588": {"CC":0, "TC":1, "CT":1, "TT":0}, "rs1801282": {"CC":0, "GC":1, "CG":1, "GG":0}, "rs1801133": {"AA":0, "GA":1, "AG":1, "GG":0},
            "rs7501331": {"CC":0, "TC":1, "CT":1, "TT":0}, "rs12934922": {"AA":0, "TA": 1, "AT":1, "TT":0}, "rs1256335": {"AA":0, "GA":1, "AG":1, "GG":0},
            "rs602662": {"GG": 0, "AG": 1, "GA": 1, "AA": 0}, "rs4680": {"GG": 0, "AG": 1, "GA": 1, "AA": 0},"rs6265": {"TT": 0, "TC": 1, "CT": 1, "CC": 0},
            "rs12722": {"TT": 0, "TC": 1, "CT": 1, "CC": 0}, "rs1042713": {"GG": 0, "AG": 1, "GA": 1, "AA": 0},"rs1049434": {"TT": 0, "AT": 1, "TA": 1, "AA": 0},
            "rs1800012": {"AA": 0, "AC": 1, "CA": 1, "CC": 0},"rs1800795": {"GG": 0, "GC": 1, "CG": 1, "CC": 0},"rs1815739": {"TT": 0, "TC": 1, "CT": 1, "CC": 0},
            "rs2070744": {"TT": 0, "TC": 1, "CT": 1, "CC": 0},"rs4253778": {"GG": 0, "GC": 1, "CG": 1, "CC": 0},"rs4644994": {"GG": 0, "AG": 1, "GA": 1, "AA": 0},
            "rs8192678": {"TT": 0, "TC": 1, "CT": 1, "CC": 0},"rs11549465": {"TT": 0, "TC": 1, "CT": 1, "CC": 0}}

recessive = {"rs762551": {"AA":0, "CA": 0, "AC":0, "CC":1}, "rs4988235": {"AA":0, "GA":0, "AG":0, "GG":1}, "rs713598": {"CC":0, "GC":0, "CG":0, "GG":1},
            "rs1726866": {"AA":0, "GA":0, "AG":0, "GG":1}, "rs10246939": {"CC":0, "TC":0, "CT":0, "TT":1}, "rs17782313": {"CC":0, "TC":0, "CT":0, "TT":1},
            "rs1800544": {"CC":0, "GC":0, "CG":0, "GG":1}, "rs5400": {"AA":0, "GA":0, "AG":0, "GG":1}, "rs1051168": {"GG":0, "TG":0, "GT":0, "TT":1},
            "rs9939609":{"AA":0, "TA": 0, "AT":0, "TT":1}, "rs17300539": {"AA":0, "GA":0, "AG":0, "GG":1}, "rs1800206": {"CC":0, "GC":0, "CG":0, "GG":1},
            "rs1800588": {"CC":0, "TC":0, "CT":0, "TT":1}, "rs1801282": {"CC":0, "GC":0, "CG":0, "GG":1}, "rs1801133": {"AA":0, "GA":0, "AG":0, "GG":1},
            "rs7501331": {"CC":0, "TC":0, "CT":0, "TT":1}, "rs12934922": {"AA":0, "TA": 0, "AT":0, "TT":1}, "rs1256335": {"AA":0, "GA":0, "AG":0, "GG":1},
             "rs602662": {"GG":0, "AG":0, "GA":0 , "AA":1}, "rs4680": {"GG":0, "AG":0, "GA":0 , "AA":1}, "rs6265": {"TT":0, "TC":0, "CT":0, "CC":1},
            "rs12722": {"TT":0, "TC":0, "CT":0, "CC":1}, "rs1042713": {"GG":0, "AG":0, "GA":0 , "AA":1},
            "rs1049434": {"TT":0, "AT":0, "TA":0, "AA":1}, "rs1800012": {"AA":0, "AC":0, "CA":0, "CC":1}, "rs1800795": {"GG":0, "GC":0, "CG":0, "CC":1},
            "rs1815739": {"TT":0, "TC":0, "CT":0, "CC":1}, "rs2070744": {"TT":0, "TC":0, "CT":0, "CC":1}, "rs4253778": {"GG":0, "GC":0, "CG":0, "CC":1},
            "rs4644994": {"GG":0, "AG":0, "GA":0 , "AA":1}, "rs8192678": {"TT":0, "TC":0, "CT":0, "CC":1}, "rs11549465": {"TT":0, "TC":0, "CT":0, "CC":1}}

dominant = {"rs762551": {"AA":0, "CA": 1, "AC":1, "CC":1}, "rs4988235": {"AA":0, "GA":1, "AG":1, "GG":1}, "rs713598": {"CC":0, "GC":1, "CG":1, "GG":1},
            "rs1726866": {"AA":0, "GA":1, "AG":1, "GG":1}, "rs10246939": {"CC":0, "TC":1, "CT":1, "TT":1}, "rs17782313": {"CC":0, "TC":1, "CT":1, "TT":1},
            "rs1800544": {"CC":0, "GC":1, "CG":1, "GG":1}, "rs5400": {"AA":0, "GA":1, "AG":1, "GG":1}, "rs1051168": {"GG":0, "TG":1, "GT":1, "TT":1},
            "rs9939609":{"AA":0, "TA": 1, "AT":1, "TT":1}, "rs17300539": {"AA":0, "GA":1, "AG":1, "GG":1}, "rs1800206": {"CC":0, "GC":1, "CG":1, "GG":1},
            "rs1800588": {"CC":0, "TC":1, "CT":1, "TT":1}, "rs1801282": {"CC":0, "GC":1, "CG":1, "GG":1}, "rs1801133": {"AA":0, "GA":1, "AG":1, "GG":1},
            "rs7501331": {"CC":0, "TC":1, "CT":1, "TT":1}, "rs12934922": {"AA":0, "TA": 1, "AT":1, "TT":1}, "rs1256335": {"AA":0, "GA":1, "AG":1, "GG":1},
             "rs602662": {"GG":0, "AG":1, "GA":1 , "AA":1}, "rs4680": {"GG":0, "AG":1, "GA":1 , "AA":1}, "rs6265": {"TT":0, "TC":1, "CT":1, "CC":1},
            "rs12722": {"TT":0, "TC":1, "CT":1, "CC":1}, "rs1042713": {"GG":0, "AG":1, "GA":1 , "AA":1},"rs1049434": {"TT":0, "AT":1, "TA":1, "AA":1},
            "rs1800012": {"AA":0, "AC":1, "CA":1, "CC":1}, "rs1800795": {"GG":0, "GC":1, "CG":1, "CC":1}, "rs1815739": {"TT":0, "TC":1, "CT":1, "CC":1},
            "rs2070744": {"TT":0, "TC":1, "CT":1, "CC":1}, "rs4253778": {"GG":0, "GC":1, "CG":1, "CC":1}, "rs4644994": {"GG":0, "AG":1, "GA":1 , "AA":1},
            "rs8192678": {"TT":0, "TC":1, "CT":1, "CC":1}, "rs11549465": {"TT":0, "TC":1, "CT":1, "CC":1}}

dict1 = {"rs762551": {"AA":"rs762551AA", "CA":"rs762551CA", "AC":"rs762551CA", "CC":"rs762551CC"},
         "rs4988235": {"AA":"rs4988235AA", "GA":"rs4988235GA", "AG":"rs4988235GA", "GG":"rs4988235GG"},
         "rs713598": {"CC":"rs713598CC", "GC":"rs713598GC", "CG":"rs713598GC", "GG":"rs713598GG"},
         "rs1726866": {"AA":"rs1726866AA", "GA":"rs1726866GA", "AG":"rs1726866GA", "GG":"rs1726866GG"},
         "rs10246939": {"CC":"rs10246939CC", "TC":"rs10246939TC", "CT":"rs10246939TC", "TT":"rs10246939TT"},
         "rs17782313": {"CC":"rs17782313CC", "TC":"rs17782313TC", "CT":"rs17782313TC", "TT":"rs17782313TT"},
         "rs1800544": {"CC":"rs1800544CC", "GC":"rs1800544GC", "CG":"rs1800544GC", "GG":"rs1800544GG"},
         "rs5400": {"AA":"rs5400AA", "GA":"rs5400GA", "AG":"rs5400GA", "GG":"rs5400GG"},
         "rs1051168": {"GG":"rs1051168GG", "TG":"rs1051168TG", "GT":"rs1051168TG", "TT":"rs1051168TT"},
         "rs9939609":{"AA":"rs9939609AA", "TA": "rs9939609TA", "AT":"rs9939609TA", "TT":"rs9939609TT"},
         "rs17300539": {"AA":"rs17300539AA", "GA":"rs17300539GA", "AG":"rs17300539GA", "GG":"rs17300539GG"},
         "rs1800206": {"CC":"rs1800206CC", "GC":"rs1800206GC", "CG":"rs1800206GC", "GG":"rs1800206GG"},
         "rs1800588": {"CC":"rs1800588CC", "TC":"rs1800588TC", "CT":"rs1800588TC", "TT":"rs1800588TT"},
         "rs1801282": {"CC":"rs1801282CC", "GC":"rs1801282GC", "CG":"rs1801282GC", "GG":"rs1801282GG"},
         "rs1801133": {"AA":"rs1801133AA", "GA":"rs1801133GA", "AG":"rs1801133GA", "GG":"rs1801133GG"},
         "rs7501331": {"CC":"rs7501331CC", "TC":"rs7501331TC", "CT":"rs7501331TC", "TT":"rs7501331TT"},
         "rs12934922": {"AA":"rs12934922AA", "TA": "rs12934922TA", "AT":"rs12934922TA", "TT":"rs12934922TT"},
         "rs1256335": {"AA":"rs1256335AA", "GA":"rs1256335GA", "AG":"rs1256335GA", "GG":"rs1256335GG"},
         "rs602662": {"GG": "rs602662GG", "AG": "rs602662AG", "GA": "rs602662AG", "AA": "rs602662AA"},
         "rs4680": {"GG": "rs4680GG", "AG": "rs4680AG", "GA": "rs4680GA", "AA": "rs4680AA"},
         "rs6265": {"TT": "rs6265TT", "TC": "rs6265TC", "CT": "rs6265TC", "CC": "rs6265CC"},
         "rs12722": {"TT": "rs12722TT", "TC": "rs12722TC", "CT": "rs12722TC", "CC": "rs12722CC"},
         "rs1042713": {"GG": "rs1042713GG", "AG": "rs1042713AG", "GA": "rs1042713AG", "AA": "rs1042713AA"},
         "rs1049434": {"TT": "rs1049434TT", "AT": "rs1049434AT", "TA": "rs1049434AT", "AA": "rs1049434AA"},
         "rs1800012": {"AA": "rs1800012AA", "AC": "rs1800012AC", "CA": "rs1800012AC", "CC": "rs1800012CC"},
         "rs1800795": {"GG": "rs1800795GG", "GC": "rs1800795GC", "CG": "rs1800795GC", "CC": "rs1800795CC"},
         "rs1815739": {"TT": "rs1815739TT", "TC": "rs1815739TC", "CT": "rs1815739TC", "CC": "rs1815739CC"},
         "rs2070744": {"TT": "rs2070744TT", "TC": "rs2070744TC", "CT": "rs2070744CT", "CC": "rs2070744CC"},
         "rs4253778": {"GG": "rs4253778GG", "GC": "rs4253778GC", "CG": "rs4253778GC", "CC": "rs4253778CC"},
         "rs4644994": {"GG": "rs4644994GG", "AG": "rs4644994AG", "GA": "rs4644994AG", "AA": "rs4644994AA"},
         "rs8192678": {"TT": "rs8192678TT", "TC": "rs8192678TC", "CT": "rs8192678TC", "CC": "rs8192678CC"},
         "rs11549465": {"TT": "rs11549465TT", "TC": "rs11549465TC", "CT": "rs11549465TC", "CC": "rs11549465CC"}}

def age_enc(age):
    if age < 12:
        age = "Child"
    elif 12 <= age < 18:
        age = "Adolescence"
    elif 18 <= age < 59:
        age = "Adult"
    elif 59 <= age:
        age = "Senior"

    return age

def bmi_enc(bmi):
    if bmi < 18.5:
        bmi = "Underweight"
    elif 18.5 <= bmi < 25:
        bmi = "Healthy"
    elif 25 <= bmi < 30:
        bmi = "Overweight"
    elif 30 <= bmi:
        bmi = "Obesity"

    return bmi

def fas_glu_enc(fast_glu):
    if fast_glu < 6.1:
        fast_glu = "Normal glc"
    elif 6.1 <= fast_glu < 7:
        fast_glu = "Impaired fasting glycemia"
    elif 7 <= fast_glu :
        fast_glu = "Diabets mellitus"

    return fast_glu

def tot_chol_enc(cholesterol):
    if cholesterol < 200:
        cholesterol = "Normal chl"
    elif 200 <= cholesterol < 239:
        cholesterol = "Borderline high chl"
    elif 239 <= cholesterol:
        cholesterol = "Risky chl"

    return cholesterol


def low_dl_enc(ldl):
    if ldl < 100:
        ldl = "Normal ldl"
    elif 100 <= ldl < 129:
        ldl = "Near normal ldl"
    elif 129 <= ldl < 159:
        ldl = "Borderline ldl"
    elif 159 <= ldl < 189:
        ldl = "Risky ldl"
    elif 189 <= ldl:
        ldl = "High risk ldl"

    return ldl

def high_dl_enc(hdl):
    if hdl >= 40:
        hdl = "Normal hdl"
    elif 40 > hdl :
        hdl = "Risky hdl"
    return hdl

def triglyceride_enc(trig):
    if trig < 150:
        trig = "Normal trig"
    elif 150 <= trig < 199:
        trig = "Borderline high trig"
    elif 199 <= trig < 499:
        trig = "Risky trig"
    elif 499 <= trig :
        trig = "High risk trig"

    return trig

def waist_hip_enc(gender,ratio):
    if gender == "F":
        if ratio > 0.85:
            ratio = "Bad"
        else:
            ratio = "Good"
    elif gender == "M":
        if ratio > 0.9:
            ratio = "Bad"
        else:
            ratio = "Good"

    return ratio

additive_encoded =genotypes.replace(additive)
codominant_encoded = genotypes.replace(codominant)

phenotypes = dfexcel.iloc[:,34:]
phenotypes = phenotypes.drop(columns=["ancestry","population"])

enc_phenotypes = dfexcel.iloc[:,34:]
enc_phenotypes = enc_phenotypes.drop(columns=["ancestry","population","fasting_insulin"])


for i in range(len(enc_phenotypes.columns)):
    if i == 0:
        for row in range(len(enc_phenotypes)):
            enc_phenotypes.iloc[row,i] = age_enc(enc_phenotypes.iloc[row,i])
    elif i == 1:
        for row in range(len(enc_phenotypes)):
            enc_phenotypes.iloc[row,i] = bmi_enc(enc_phenotypes.iloc[row,i])
    elif i == 2:
        for row in range(len(enc_phenotypes)):
            enc_phenotypes.iloc[row,i] = fas_glu_enc(enc_phenotypes.iloc[row,i])
    elif i == 3:
        for row in range(len(enc_phenotypes)):
            enc_phenotypes.iloc[row,i] = high_dl_enc(enc_phenotypes.iloc[row,i])
    elif i == 5:
        for row in range(len(enc_phenotypes)):
            enc_phenotypes.iloc[row,i] = low_dl_enc(enc_phenotypes.iloc[row,i])
    elif i == 7:
        for row in range(len(enc_phenotypes)):
            enc_phenotypes.iloc[row,i] = tot_chol_enc(enc_phenotypes.iloc[row,i])
    elif i == 8:
        for row in range(len(enc_phenotypes)):
            enc_phenotypes.iloc[row,i] = triglyceride_enc(enc_phenotypes.iloc[row,i])
    elif i == 9:
        for row in range(len(enc_phenotypes)):
            enc_phenotypes.iloc[row,i] = waist_hip_enc(enc_phenotypes.iloc[row,6],enc_phenotypes.iloc[row,i])

#print(enc_phenotypes)
def normalizer(array):
    norm = np.empty(array.shape)
    for elm in array:
        #print(i)
        normalized = (elm - np.amin(array)) / (np.amax(array) - np.amin(array))
        norm[np.where(array==elm),0] = normalized
        #norm = np.append(normalized, axis=0)
    return norm


arl_encoded = genotypes.replace(dict1)

all_data = pd.concat([arl_encoded,enc_phenotypes.iloc[:,:]], axis=1)
all_data = all_data.drop(columns=["height"])

