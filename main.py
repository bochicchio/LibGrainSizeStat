# function to import excel sheets
# skdmsl


def getSheet(path, sheet_name=None):
    df = pd.read_excel(path, sheet_name, header=None)
    return df


# function for finding a string inside of a pandas dataframe


def find_string(df, string):

    filt = df == string
    [i, j] = np.where(filt == True)

    return i, j if i.size > 0 else print(
        "Error: More than one " + string + " found in " + sheet_name + "!"
    )


# -----------------------------------------

import numpy as np
import pandas as pd


path = "magic_resave.xlsx"
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