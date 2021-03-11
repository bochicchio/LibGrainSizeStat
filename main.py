# function to import excel sheets
def getSheet(path, sheet_name=None):
    df = pd.read_excel(path, sheet_name, header=None)
    return df


def find_string(df, string):
    ref = pd.DataFrame()
    for c in df.columns:
        try:
            filt = pd.DataFrame(df[c].str.startswith(string))
        except AttributeError:
            print("Found a blank column: #", c + 1)
        else:
            ref = pd.concat([ref, filt], axis=1)
    ref = np.where(ref == True)
    ref = list([startRef[0][0], startRef[1][0]])
    return ref


# -----------------------------------------

import numpy as np
import pandas as pd

path = "magic_resave.xlsx"
sheet_name = "July11"
sampleNameString = "SAMP WT"
sizeFractionStartString = "SIZE (MM)"
sizeFractionEndString = "<"
# load sheet
df = getSheet(path, sheet_name)

# Find the index of a string to act as a reference point in
# case of non-standard sheet layout. Default = 'SAMP WT'

sampRef = find_string(df, sampleNameString)

# index of site names (refrenced from string above)
SITENAME = df.iloc[sampRef[0] - 3]
# SITENAME = SITENAME.dropna(1)

# index of site subtitles (refrenced from string above)
SUBNAME = df.iloc[sampRef[0] - 2]
# SUBNAME = SUBNAME.dropna(1)

# find size catagory info
# size fraction start...
startRef = find_string(df, sizeFractionStartString)
startRef[0] = startRef[0] + 1
largestSizeFraction = df.iloc[startRef[0], startRef[1]]
# size fraction end...
endRef = find_string(df, sizeFractionEndString)
smallestSizeFraction = df.iloc[endRef[0], endRef[1]]

if startRef[1][0] == endRef[1][0]:

    binIndex = np.arange(startRef[0][0], endRef[0][0] + 1)
    binIndex = binIndex.tolist()
    BINFRACTION = binIndex
