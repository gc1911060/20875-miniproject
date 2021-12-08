from functools import reduce
import pandas as pd
import numpy as np
import statistics as stats

def mean(lst):
    return reduce(lambda a, b: a + b, lst) / len(lst)


if __name__ == "__main__":
    # labels, data = getData("NYC_Bicycle_Counts_2016_Corrected.csv"

    # get summary statistics of each bridge
    data = pd.read_csv("NYC_Bicycle_Counts_2016_Corrected.csv")
    bridge_names = ["Brooklyn Bridge", "Manhattan Bridge", "Williamsburg Bridge", "Queensboro Bridge"]
    bridges = {}

    for bridge in bridge_names:
        bridges.update({bridge: [x for x in pd.array([int(y.replace(",", "")) for y in data[bridge]])]})

    for bridge in bridge_names:
        mean = stats.mean(bridges[bridge])
        std = np.std(bridges[bridge])
        print(f"{bridge}: {mean}")
        print(f"\tcoefOfVar: {std / mean}")
        print(f"\tstdDev: {std}")
        print(f"\ttotal:  {sum(bridges[bridge])}")
