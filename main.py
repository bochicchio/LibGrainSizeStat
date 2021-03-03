# function to import excel sheets


def getSheet(path, sheet_name=None):
    df = pd.read_excel(path, sheet_name, header=None)
    return df


# function for finding a string inside of a pandas dataframe


def find_string(df, string):
    mask = np.column_stack([df[col].str.contains(string, na=False) for col in df])
    [i, j] = np.where(mask == True)
    return i, j if len(i) <= 1 else print(
        "Error: More than one " + string + " found in " + sheet_name + "!"
    )


# -----------------------------------------

import numpy as np
import pandas as pd
import math

path = "magic.xlsx"
sheet_name = "July11"
string = "SAMP WT"

# load sheet
df = getSheet(path, sheet_name)

# Find the index of a string to act as a reference point in
# case of non-standard sheet layout. Default = 'SAMP WT'
[i, j] = find_string(df, string)

# index of site names (refenced from string above)
siteIndex = list(np.arange(j + 1, df.shape[1]))

# get list of sample site names
siteNames = [df.iloc[i - 2, l] for l in siteIndex]

# get list of sample site second line notes
siteNotes = [df.iloc[i - 1, l] for l in siteIndex]

# get list of SAMP WT
# siteSAMPWT = df.iloc[i, l] for l in siteIndex

siteIndex[0] = 999

for l in siteIndex:
    print(l)

# df.iloc[i, l] for l in siteIndex
# as;sdklf;sdlkfjs;ldfk;sldfk
