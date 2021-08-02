import numpy as np
import pandas as pd


#%%
# function to import excel sheets
def get_sheet(path, sheetName=None):
    df = pd.read_excel(path, sheetName, header=None)
    return df

# 
def find_string(df, string):
    ref = pd.DataFrame()
    for c in df.columns:                        #loop finds true/false for string
        try:
            filt = pd.DataFrame(df[c].str.startswith(string))
        except AttributeError:
            print("Found a blank column: #", c + 1)
        else:
            ref = pd.concat([ref, filt], axis=1)
    
    ref = np.where(ref == True)                 #tuple cord. of true values 1 [row, col]/per    
    ref = list([ref[0][0], ref[1][0]])          #convert first tuple row  to list
    return ref



def extract_line(df, ref, rowOffset=0, colOffset=0, d = 'row', stop = False):
    if d == 'row':
        ref[0] = ref[0]+colOffset
        ref[1] = ref[1]+rowOffset
        line = df.iloc[ref[0]+colOffset][ref[1]:df.shape[0]]
    else:
        line = df[ref+colOffset[0]][ref+rowOffset[1]]

    if stop != False:
        if stop.is_integer:
            try:
                line = line[0:stop]
            except TypeError:
                print('stop variable must be INT or FALSE')
        else:
             
            

return line
# -----------------------------------------
#%%



path = "magic_resave.xlsx"
sheetName = "July11"
df = get_sheet(path, sheetName)  #load sheet into df
#%%

# find site names
string = "SIZE (MM)"
ref = find_string(df, string)
#%%

d = "row"
rowOffset = -2
colOffset = 1
line = extract_line(df, ref, rowOffset=0, colOffset=0, d = 'row')
#%%



sizeFractionEndString = "<"
# load sheet

# Find the first sample site name 


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
