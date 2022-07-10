#%%
import numpy as np
import pandas as pd
import util
#from classes import data
#from dataclasses import dataclass

# load file and sheet
path = "magic_resave.xlsx"
sheetName = "July11"
df = util.get_sheet(path, sheetName)  #load sheet into df


# find site names
string = "SIZE (MM)"
referencePoint = util.find_string(df, string)
line = util.extract_line(df, referencePoint, xOffset = 1, yOffset = -3, direction = 'x')
siteList = line

# find size fractions
string = "SIZE (MM)"
referencePoint = util.find_string(df, string)
line = util.extract_line(df, referencePoint, xOffset = 0, yOffset = 1, direction = 'y', stop = '<')
sizeFractions = line

# find grain size fraction weights
string = "SIZE (MM)"
referencePoint = util.find_string(df, string)
line = util.extract_line(df, referencePoint, xOffset = 1, yOffset = 1, direction = 'x', width = sizeFractions.shape[0])
results = line

# find site type/notes
string = "SIZE (MM)"
referencePoint = util.find_string(df, string)
line = util.extract_line(df, referencePoint, xOffset = 1, yOffset = -2, direction = 'x')
subName = line

# find sample weights
string = "SAMP WT"
referencePoint = util.find_string(df, string)
line = util.extract_line(df, referencePoint, xOffset = 1, yOffset = 0, direction = 'x')
sampleWeight = line


#%%
data = pd.DataFrame(siteList.values, columns=['site'])
data['subCat'] = subName
data['sampWt'] = sampleWeight

for i in data.index:
    data.loc[i,'sizeFraction'] = sizeFractions.values
    data.loc[i,'results'] = [results[:i].values]






#%%



# load sheet

# Find the first sample site name 


# # index of site names (referencePointrenced from string above)
# SITENAME = df.iloc[sampreferencePoint[0] - 3]
# # SITENAME = SITENAME.dropna(1)

# # index of site subtitles (referencePointrenced from string above)
# SUBNAME = df.iloc[sampreferencePoint[0] - 2]
# # SUBNAME = SUBNAME.dropna(1)

# # find size catagory info
# # size fraction start...
# startreferencePoint = find_string(df, sizeFractionStartString)
# startreferencePoint[0] = startreferencePoint[0] + 1
# largestSizeFraction = df.iloc[startreferencePoint[0], startreferencePoint[1]]
# # size fraction end...
# endreferencePoint = find_string(df, sizeFractionEndString)
# smallestSizeFraction = df.iloc[endreferencePoint[0], endreferencePoint[1]]

# if startreferencePoint[1][0] == endreferencePoint[1][0]:

#     binIndex = np.arange(startreferencePoint[0][0], endreferencePoint[0][0] + 1)
#     binIndex = binIndex.tolist()
#     BINFRACTION = binIndex
