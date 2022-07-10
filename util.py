# util.py>

import numpy as np
import pandas as pd

# function to import excel sheets
def get_sheet(path, sheetName=None):
    df = pd.read_excel(path, sheetName, header=None)
    return df

# function to locate indexes of a given string in and a given dataframe    
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

# function to extract a  line from a dataframe based on referencePoint found in a dataframe
def extract_line(df, referencePoint, xOffset = 0, yOffset = 0, direction = 'x', width = 1, stop = False, include = True):
    referencePoint[0] = referencePoint[0]+yOffset
    referencePoint[1] = referencePoint[1]+xOffset
      

    if direction == 'x':
        yStart = referencePoint[0]
        xStart = referencePoint[1]
        xStop = df.shape[1]
        line = df.iloc[yStart:yStart + width, xStart:xStop]

    if direction == 'y':
        xStart = referencePoint[1]
        yStart = referencePoint[0]
        yStop = df.shape[0]
        line = df.iloc[yStart:yStop, xStart:xStart + width]

    if stop != False:

        if isinstance(stop, int):
            if include == True:
                stop = stop + 1
            line = line[0:stop]
                
        if isinstance(stop, str):
                line = pd.DataFrame(line)
                stop = find_string(line, stop)[0]
                if include == True:
                    stop = stop + 1
                line = line[0:stop]
    
    if line.shape[1] > 1:
        line = line.transpose()
    
    return line
