#pip openpyxl
import pandas as pd
dfphenotype = pd.read_excel('1000genome_geno_pheno_data.xlsx')
dfphenotype = dfphenotype.iloc[:, 1:]
col = ["Genotype (forward strand)"]
rs762551 = pd.read_csv('373507-SampleGenotypes-Homo_sapiens_Variation_Sample_rs762551.csv', usecols= col)
rs4988235 = pd.read_csv('373507-SampleGenotypes-Homo_sapiens_Variation_Sample_rs4988235.csv', usecols= col)
rs713598 = pd.read_csv('373507-SampleGenotypes-Homo_sapiens_Variation_Sample_rs713598.csv', usecols= col)
rs1726866 = pd.read_csv('373507-SampleGenotypes-Homo_sapiens_Variation_Sample_rs1726866.csv', usecols= col)
rs10246939 = pd.read_csv('373507-SampleGenotypes-Homo_sapiens_Variation_Sample_rs10246939.csv', usecols= col)
rs17782313 = pd.read_csv('373507-SampleGenotypes-Homo_sapiens_Variation_Sample_rs17782313.csv', usecols= col)
rs1800544 = pd.read_csv('373507-SampleGenotypes-Homo_sapiens_Variation_Sample_rs1800544.csv', usecols= col)
rs5400 = pd.read_csv('373507-SampleGenotypes-Homo_sapiens_Variation_Sample_rs5400.csv', usecols= col)
rs1051168 = pd.read_csv('373507-SampleGenotypes-Homo_sapiens_Variation_Sample_rs1051168.csv', usecols= col)
rs9939609 = pd.read_csv('373507-SampleGenotypes-Homo_sapiens_Variation_Sample_rs9939609.csv', usecols= col)
rs17300539 = pd.read_csv('373507-SampleGenotypes-Homo_sapiens_Variation_Sample_rs17300539.csv', usecols= col)
rs1800206 = pd.read_csv('373507-SampleGenotypes-Homo_sapiens_Variation_Sample_rs1800206.csv', usecols= col)
rs1800588 = pd.read_csv('373507-SampleGenotypes-Homo_sapiens_Variation_Sample_rs1800588.csv', usecols= col)
rs1801282 = pd.read_csv('373507-SampleGenotypes-Homo_sapiens_Variation_Sample_rs1801282.csv', usecols= col)
rs1801133  = pd.read_csv('373507-SampleGenotypes-Homo_sapiens_Variation_Sample_rs1801133.csv', usecols= col)
rs7501331 = pd.read_csv('373507-SampleGenotypes-Homo_sapiens_Variation_Sample_rs7501331.csv', usecols= col)
rs12934922 = pd.read_csv('373507-SampleGenotypes-Homo_sapiens_Variation_Sample_rs12934922.csv', usecols= col)
rs1256335 = pd.read_csv('373507-SampleGenotypes-Homo_sapiens_Variation_Sample_rs1256335.csv', usecols= col)
rs602662 = pd.read_csv('373507-SampleGenotypes-Homo_sapiens_Variation_Sample_rs602662.csv', usecols= col)

rsler = [rs762551, rs4988235, rs713598, rs1726866, rs10246939, rs17782313, rs1800544, rs5400, rs1051168, rs9939609,
         rs17300539, rs1800206, rs1800588, rs1801282, rs1801133, rs7501331, rs12934922, rs1256335, rs602662]
sport = pd.concat(rsler, join='outer', axis=1)
sport.columns = ["rs762551", "rs4988235", "rs713598", "rs1726866", "rs10246939", "rs17782313", "rs1800544",
        "rs5400", "rs1051168", "rs9939609", "rs17300539", "rs1800206", "rs1800588", "rs1801282",
        "rs1801133", "rs7501331", "rs12934922", "rs1256335", "rs602662"]
newdata = pd.concat([sport, dfphenotype], axis=1)
cols = ["rs4680", "rs6265", "rs12722", "rs1042713", "rs1049434", "rs1800012", "rs1800795",
        "rs1815739", "rs2070744", "rs4253778", "rs4644994",  "rs8192678", "rs11549465"]
old = newdata.columns[19:32]
dict = dict(zip(old, cols))
newdata.rename(index=str, columns=dict,  inplace=True)
columnsofnew = newdata.columns[:32]
newdata[columnsofnew] = newdata[columnsofnew].replace({'\|': ''}, regex=True)
newdata.to_excel("GenotypeandPhenotypeData.xlsx")



