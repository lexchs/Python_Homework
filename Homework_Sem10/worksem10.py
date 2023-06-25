import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

df = pd.DataFrame(columns=list(set(data['whoAmI'])))
for col in data['whoAmI']:
    df.loc[len(df.index)] = [int(col == df.columns[i])
    for i in range(len(df.columns))]
print(df)