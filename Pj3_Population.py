import pandas as pd
import os
rs762551 = pd.read_csv('373507-SampleGenotypes-Homo_sapiens_Variation_Sample_rs762551.csv')
rs4988235 = pd.read_csv('373507-SampleGenotypes-Homo_sapiens_Variation_Sample_rs4988235.csv')
rs713598 = pd.read_csv('373507-SampleGenotypes-Homo_sapiens_Variation_Sample_rs713598.csv')
rs1726866 = pd.read_csv('373507-SampleGenotypes-Homo_sapiens_Variation_Sample_rs1726866.csv')
rs10246939 = pd.read_csv('373507-SampleGenotypes-Homo_sapiens_Variation_Sample_rs10246939.csv')
rs17782313 = pd.read_csv('373507-SampleGenotypes-Homo_sapiens_Variation_Sample_rs17782313.csv')
rs1800544 = pd.read_csv('373507-SampleGenotypes-Homo_sapiens_Variation_Sample_rs1800544.csv')
rs5400 = pd.read_csv('373507-SampleGenotypes-Homo_sapiens_Variation_Sample_rs5400.csv')
rs1051168 = pd.read_csv('373507-SampleGenotypes-Homo_sapiens_Variation_Sample_rs1051168.csv')
rs9939609 = pd.read_csv('373507-SampleGenotypes-Homo_sapiens_Variation_Sample_rs9939609.csv')
rs17300539 = pd.read_csv('373507-SampleGenotypes-Homo_sapiens_Variation_Sample_rs17300539.csv')
rs1800206 = pd.read_csv('373507-SampleGenotypes-Homo_sapiens_Variation_Sample_rs1800206.csv')
rs1800588 = pd.read_csv('373507-SampleGenotypes-Homo_sapiens_Variation_Sample_rs1800588.csv')
rs1801282 = pd.read_csv('373507-SampleGenotypes-Homo_sapiens_Variation_Sample_rs1801282.csv')
rs1801133  = pd.read_csv('373507-SampleGenotypes-Homo_sapiens_Variation_Sample_rs1801133.csv')
rs7501331 = pd.read_csv('373507-SampleGenotypes-Homo_sapiens_Variation_Sample_rs7501331.csv')
rs12934922 = pd.read_csv('373507-SampleGenotypes-Homo_sapiens_Variation_Sample_rs12934922.csv')
rs1256335 = pd.read_csv('373507-SampleGenotypes-Homo_sapiens_Variation_Sample_rs1256335.csv')
rs602662 = pd.read_csv('373507-SampleGenotypes-Homo_sapiens_Variation_Sample_rs602662.csv')
rs1 = {str(rs762551): "rs762551",str(rs4988235) :"rs4988235", str(rs713598) :"rs713598", str(rs1726866) :"rs1726866",
        str(rs10246939) :"rs10246939", str(rs17782313) :"rs17782313", str(rs1800544) :"rs1800544",
       str(rs5400) :"rs5400", str(rs1051168) :"rs1051168", str(rs9939609) :"rs9939609", str(rs17300539) :"rs17300539",
       str(rs1800206): "rs1800206",str(rs1800588) :"rs1800588", str(rs1801282) :"rs1801282",  str(rs1801133) :"rs1801133",
       str(rs7501331) :"rs7501331",str(rs12934922) :"rs12934922", str(rs1256335) :"rs1256335", str(rs602662) :"rs602662"}

rsler = [rs762551, rs4988235, rs713598, rs1726866, rs10246939, rs17782313, rs1800544, rs5400, rs1051168, rs9939609,
         rs17300539, rs1800206, rs1800588, rs1801282, rs1801133, rs7501331, rs12934922, rs1256335, rs602662]
foldisim = ["rs762551", "rs4988235", "rs713598", "rs1726866", "rs10246939", "rs17782313", "rs1800544", "rs5400", "rs1051168",
            "rs9939609", "rs17300539", "rs1800206", "rs1800588", "rs1801282", "rs1801133", "rs7501331",
            "rs12934922", "rs1256335", "rs602662"]
#19 rsi etnik gruplarına göre ayrı klasörlere kaydedildi.
def ethnicchang(df):
    for index,value in enumerate(population):
        for j in ["AFR", "AMR", "EAS", "EUR", "SAS"]:
            if j in value:
                population[index] = j
    df['Population(s)'] = population

for i in rsler:
    for j in foldisim:
        if os.path.isdir(f"output/{j}") == False:
            os.mkdir(f"output/{j}")
for i in rsler:
    population = list(i['Population(s)'])
    ethnicchang(i)
    data_grp = i.groupby('Population(s)')
#gerekli olmayan sütunları kaldırarak kaydetmek için
    for c in ["AFR", "AMR", "EAS", "EUR", "SAS"]:
        df1 = data_grp.get_group(c)
        df1.iloc[:, 1:3].to_csv("output/{}/{}.csv".format(rs1[str(i)], c))

