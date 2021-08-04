#%%
import numpy as np
import pandas as pd

# function to import excel sheets
def get_sheet(path, sheetName=None):
    df = pd.read_excel(path, sheetName, header=None)
    return df
def find_string(df, string):
    referencePoint = pd.DataFrame()
    for c in df.columns:                        #loop finds true/false for string
        try:
            filt = pd.DataFrame(df[c].str.startswith(string))
        except AttributeError:
            print("Found a blank column: #", c + 1)
        else:
            referencePoint = pd.concat([referencePoint, filt], axis=1)
    
    referencePoint = np.where(referencePoint == True)                 #tuple cord. of true values 1 [x, y]/per    
    referencePoint = list([referencePoint[0][0], referencePoint[1][0]])          #convert first tuple x  to list
    return referencePoint
def extract_line(df, referencePoint, xOffset=0, yOffset=0, direction = 'x', stop = False):
    referencePoint[0] = referencePoint[0]+yOffset
    referencePoint[1] = referencePoint[1]+xOffset
      
    if direction == 'x':
        yStart = referencePoint[0]
        xStart = referencePoint[1]
        xStop = df.shape[1]
        line = df.iloc[yStart][xStart:xStop]

    if direction == 'y':
        xStart = referencePoint[1]
        yStart = referencePoint[0]
        yStop = df.shape[0]
        line = df.iloc[yStart:yStop][xStart]

    if stop != False:
        if isinstance(stop, int):
                line = line[0:stop]
        if isinstance(stop, str):
                line = pd.DataFrame(line)
                stop = find_string(line, stop)[0]
                line = line[0:stop]
    return line
# -----------------------------------------
#%%
path = "magic_resave.xlsx"
sheetName = "July11"
df = get_sheet(path, sheetName)  #load sheet into df

# find site names
string = "SIZE (MM)"
referencePoint = find_string(df, string)

direction = "y"
xOffset = 0
yOffset = 1
stop = '<'
line = extract_line(df, referencePoint, xOffset, yOffset, direction, stop)
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
