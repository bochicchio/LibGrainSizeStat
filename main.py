# function to import excel sheets
def get_sheet(path, sheetName=None):
    df = pd.read_excel(path, sheetName, header=None)
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
    ref = list([ref[0][0], ref[1][0]])
    return ref

def extract_row(df, ref, direction)
    if direction == 'row':
        df.iloc[ref[0]][ref[1]:df.shape[0]]
    
    if direction == 'col':
        df[ref[0]][ref[1]]

# -----------------------------------------

import numpy as np
import pandas as pd

path = "magic_resave.xlsx"
sheetName = "July11"
sampleNameString = "TS 1"
sampleDirection = 0
sizeFractionStartString = "SIZE (MM)"
sizeFractionEndString = "<"
# load sheet
df = get_sheet(path, sheet_name)

# Find the first sample site name 

sampRef = find_string(df, sampleNameString, sampleDirection)

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
