import pandas as pd
import random as rd


lex = pd.read_csv("http://www.lexique.org/databases/Lexique382/Lexique382.tsv", sep='\t')
lex.head()

subset = lex.loc[(lex.nblettres >= 6) & (lex.nblettres <=10)]

# separe les noms et les verbes dans deux dataframes:
noms = subset.loc[subset.cgram == 'NOM']
verbs = subset.loc[subset.cgram == 'VER']

# sectionne sur la bases de la fréquence lexicale
noms_hi = noms.loc[noms.freqlivres > 50.0]
noms_low = noms.loc[(noms.freqlivres < 20.0) & (noms.freqlivres > 10.0)]

verbs_hi = verbs.loc[verbs.freqlivres > 50.0]
verbs_low = verbs.loc[(verbs.freqlivres < 20.0) & (verbs.freqlivres > 10.0)]
# choisi des items tirés au hasard dans chacun des 4 sous-ensembles:
N = 1

def get_word() -> str:    
    prob = rd.randint(0,100)
    
    if 0 <= prob <= 15: 
        if rd.randint(0,1) :
            word = noms_low.sample(N).ortho.to_string(index=False)
        word = verbs_low.sample(N).ortho.to_string(index=False)
    else :
        if rd.randint(0,1) :
            word = noms_hi.sample(N).ortho.to_string(index=False)
        word = verbs_hi.sample(N).ortho.to_string(index=False)
    return word