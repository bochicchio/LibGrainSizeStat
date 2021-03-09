#%%
# function to import excel sheets


def getSheet(path, sheet_name=None):
    df = pd.read_excel(path, sheet_name, header=None)
    return df


# function for finding a string inside of a pandas dataframe


def findString(df, string):

    filt = df == string
    [i, j] = np.where(filt == True)

    return i, j if i.size > 0 else print(
        "Error: More than one " + string + " found in " + sheet_name + "!"
    )


# -----------------------------------------
#%%
import numpy as np
import pandas as pd


path = "magic_resave.xlsx"
sheet_name = "July11"
string = "SAMP WT"

# load sheet
df = getSheet(path, sheet_name)

# Find the index of a string to act as a reference point in
# case of non-standard sheet layout. Default = 'SAMP WT'
[i, j] = findString(df, string)


# index of site names (refenced from string above)
siteNames = df.iloc[i - 2]
siteNames = siteNames.dropna(1)

# index of site subtitles (refenced from string above)
subName = df.iloc[i - 1]
subName = subName.dropna(1)