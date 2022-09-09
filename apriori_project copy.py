#Apriori
import pandas as pd
#from encoding import genotypes, enc_phenotypes, codominant_encoded, additive_encoded
from mlxtend.frequent_patterns import apriori, fpgrowth, association_rules
from encoding import all_data, enc_phenotypes
from mlxtend.preprocessing import TransactionEncoder


te = TransactionEncoder()
te_ary = te.fit(all_data.iloc[:,:].values).transform(all_data.iloc[:,:].values)

print(te.columns_)
te_df = pd.DataFrame(te_ary, columns=te.columns_)
print(te_df.columns)
frq_items = fpgrowth(te_df, min_support=0.4, use_colnames=True)

print(frq_items)
#Collecting the inferred rules in a dataframe
rules = association_rules(df=frq_items, metric="lift", min_threshold=0.5)
rules = rules.sort_values(['confidence', 'lift'], ascending=[False, False])

rules.to_csv("<PATH>/hepsi2.csv",index=False)

#Collecting the inferred rules in a dataframe
rules = association_rules(df=frq_items, metric="lift", min_threshold=0.5)
rules = rules.sort_values(['confidence', 'lift'], ascending=[False, False])

rules.to_csv("<PATH>/rules1.csv",index=False)
#print(rules.head())

# Correcting result to a readable data (1 phenotype to 1 genotype)
results_data = pd.read_csv("<PATH>/hepsi2.csv")

phen_consequents = pd.DataFrame(columns=results_data.columns)
index = 0

for i in range(len(results_data)):
    word = results_data.iloc[i, 1].replace("frozenset({", "")
    word = word.replace(", ", "")
    word = word.replace("})", "")
    val_list = word.split("'")
    for val in val_list:
        if "" in val_list:
            val_list.remove("")

    # print(val_list)
    if len(val_list) == 1:
        consq = val_list[0]
        if consq in enc_phenotypes.values:
            phen_consequents.loc[index] = results_data.loc[i]
            index += 1

phen_consequents.to_csv("<PATH>/resconsq.csv")

phenotypes = ["Child", "Adolescence", "Adult", "Senior", "Underweight", "Healthy", "Overweight", "Obesity",
              "Normal glc", "Impaired fasting glycemia",
              "Diabets mellitus", "Normal chl", "Borderline high chl", "Risky chl", "Normal ldl", "Near normal ldl",
              "Borderline ldl", "Risky ldl",
              "High risk ldl", "Normal hdl", "Risky hdl", "Normal trig", "Borderline high trig", "Risky trig",
              "High risk trig", "Bad", "Good", "F",
              "M"]
# print(type(phen_consequents))
phen_antecedents = phen_consequents
# print(num_list)
del_rows = []
antecedents = []
for i in range(len(phen_consequents)):
    for phen in phenotypes:
        # print(phen_antecedents.iloc[i,0])
        if phen in phen_antecedents.iloc[i, 0]:
            print(i)
            if i not in del_rows:
                del_rows.append(i)

phen_antecedents = phen_antecedents.drop(del_rows)
phen_antecedents.to_csv("<PATH>>/resconsq_exc.csv")

#Finding outlier data
import pandas as pd
df = pd.read_csv("<PATH>/resconsq_exc.csv")
df = df.drop(columns=df.columns[0])
df["Confidence-support"] = (df["confidence"] - df["support"])
last_df = df.sort_values(by= ["Confidence-support"], ascending=True)
last_df.to_csv("<PATH>/final.csv")
