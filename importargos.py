##---------------------------------------------------------------------
## ImportARGOS.py
##
## Description: Read in ARGOS formatted tracking data and create a line
##    feature class from the [filtered] tracking points
##
## Usage: ImportArgos <ARGOS folder> <Output feature class> 
##
## Created: Fall 2021
## Author: jcf55@duke.edu  (for ENV859)
##---------------------------------------------------------------------

# Import modules
import sys, os, arcpy

# Set input variables (Hard-wired)
#these are absolute paths; meaning it works for only us not everyone
inputFile = 'D:/ARGOSTracking/Data/ARGOSData/1997dg.txt'
outputFC = "D:/ARGOSTracking/Scratch/ARGOStrack.shp"

#%% Construct a while loop to iterate through all lines in the datafile
# Open the ARGOS data file for reading
# Import modules
import sys, os, arcpy

# Set input variables (Hard-wired)
inputFile = '../Data/ARGOSData/1997dg.txt'
outputFC = '../Scratch/ARGOStrack.shp'

## Construct a while loop to iterate through all lines in the datafile
# Open the ARGOS data file for reading
inputFileObj = open(inputFile,'r')

# Get the first line of data, so we can use a while loop
lineString = inputFileObj.readline()
while lineString:
    
   #We have 7 lines of information that we want to skip before we start read
    #Set the code to run only if the line contains the string "Date :"
    #This means if Date : is in the line that we are reading....
    #code below that is indented will only be run if this is true
    if ("Date :" in lineString):
        
        # Parse the line into a list
        lineData = lineString.split()
        
        # Extract attributes from the datum header line
        tagID = lineData[0]
        obsDate = lineData[3]
        obsTime = lineData[4]
        obsLC = lineData[7]
        
        #Because this data is on a different line we need it to read this
        # Extract location info from the next line
        line2String = inputFileObj.readline()
        
        # Parse the line into a list
        line2Data = line2String.split()
        
        # Extract the date we need to variables
        obsLat = line2Data[2]
        obsLon= line2Data[5]
        
        # Print results to see how we're doing
        print (tagID,obsDate,obsTime,obsLC,"Lat:"+obsLat,"Long:"+obsLon)
        
    # Move to the next line so the while loop progresses
    lineString = inputFileObj.readline()
    
#Close the file object
inputFileObj.close()