# function to import excel sheets
def getSheet(path, sheet_name=None):
    df = pd.read_excel(path, sheet_name, header=None)

    return df


# function for finding a string inside of a pandas dataframe
def findString(df, string, startWith=False):

    if startWith == False:
        filt = df == string
        [i, j] = np.where(filt == True)

    if startWith == True:
        i = list([])
        j = list([])
        for col in df.columns:
            try:
                temp = df[col].str.startswith(string)
            except AttributeError:
                print("Found a blank column: #", col)
            else:
                ii = list(np.where(temp == True))
                if np.sum(ii) > 0:
                    i.append(ii)

    i = list(i)
    return i, j if np.size(i) == 1 else print(
        "Error: More than one "
        + string
        + " found in "
        + sheet_name
        + " or not found at all."
    )


# -----------------------------------------

import numpy as np
import pandas as pd

path = "magic_resave.xlsx"
sheet_name = "July11"
sampleNameString = "SAMP WT"
sizeFractionString = "SIZE (MM)"

# load sheet
df = getSheet(path, sheet_name)

# Find the index of a string to act as a reference point in
# case of non-standard sheet layout. Default = 'SAMP WT'
[i, j] = findString(df, sampleNameString)


# index of site names (refrenced from string above)
SITENAME = df.iloc[i - 2]
SITENAME = SITENAME.dropna(1)

# index of site subtitles (refrenced from string above)
SUBNAME = df.iloc[i - 1]
SUBNAME = SUBNAME.dropna(1)

# find size catagory info
[i, j] = findString(df, sizeFractionString)

largestSizeFraction = i + 1

SIZEFRACTION = df.iloc[:, j]
SIZEFRACTION = SIZEFRACTION.dropna(0)

SIZEFRACTION = SIZEFRACTION.squeeze()
smallestSizeFraction = SIZECATAGORY.str.startswith("<")
