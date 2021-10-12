import pandas as pd
import numpy as np
from plotly import graph_objects as go
from tqdm import tqdm

tara = "Romania"
csv = pd.read_csv("./covid19.csv")
csv.drop(columns=["Last Update", "Deaths", "Recovered", "SNo"], inplace=True)

newCSV = pd.DataFrame(columns=["ObservationDate", "Country/Region", "Confirmed"])
gb = csv.groupby(["ObservationDate"], sort=False)
for gr in tqdm(gb.groups):
    group = gb.get_group(gr)
    country_gr = group.groupby(["Country/Region"], sort=False)
    for gr in country_gr.groups:
        group = country_gr.get_group(gr).reset_index()
        newCSV = newCSV.append({"ObservationDate": group["ObservationDate"][0], "Country/Region": group["Country/Region"][0], "Confirmed": group["Confirmed"].sum()}, ignore_index=True)
    # break
newCSV.set_index(keys=["ObservationDate"], inplace=True)
newCSV.to_csv("covid19_nou.csv")