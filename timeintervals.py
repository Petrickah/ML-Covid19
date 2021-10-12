import pandas as pd
from tqdm import tqdm

csv = pd.read_csv("covid19_nou.csv", index_col=0)

nrZile=7
newCSV = pd.DataFrame(columns=["Week", "Country", "Open", "High", "Low", "Close"])
gb = csv.groupby(["Country/Region"], sort=True)
for gr in tqdm(gb.groups):
    group = gb.get_group(gr)
    group.reset_index(inplace=True)
    confirmed = group.loc[:,"Confirmed"].diff().fillna(0)
    group.loc[:,"Confirmed"] = confirmed
    for k in range(0, len(group)-nrZile, nrZile):
        week = group.iloc[k:k+nrZile,]
        week.reset_index(inplace=True)
        newCSV = newCSV.append({"Week":k//7, "Country":week["Country/Region"][0], "Open":week.loc[0,"Confirmed"], "Close":week.loc[nrZile-1,"Confirmed"], "High":week["Confirmed"].max(), "Low":week["Confirmed"].min()}, ignore_index=True)
    if len(group)<nrZile: continue
newCSV.set_index("Week", inplace=True)
newCSV.to_csv("covid19_final.csv")