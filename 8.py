import pandas as pd

with open("8.txt", "r") as file:
    data = [[j for j in i] for i in file.read().split("\n")]

df = pd.DataFrame(data)

# https://www.activestate.com/resources/quick-reads/how-to-access-a-column-in-a-dataframe-using-pandas/
# https://www.geeksforgeeks.org/creating-pandas-dataframe-using-list-of-lists/

for x in df:
    for y in df.columns:
        print(x, y)