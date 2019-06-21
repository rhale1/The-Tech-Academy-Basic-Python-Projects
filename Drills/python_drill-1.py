#For this drill, you will need to write a script that will check a 
#specific folder on the hard drive, verify whether those files end 
#with a “.txt” file extension and if they do, print those qualifying 
#file names and their corresponding modified time-stamps to the console.

    #Your script will need to use the listdir() method from the OS module to iterate through all files within a specific directory.
    #Your script will need to use the path.join() method from the OS module to concatenate the file name to its file path, forming an absolute path.
    #Your script will need to use the getmtime() method from the OS module to find the latest date that each text file has been created or modified.
    #Your script will need to print each file ending with a “.txt” file extension and its corresponding mtime to the console.

import os
import time

def openFile() :    
    fPath = os.getcwd() # gets current working directory and stores in fPath
    allFiles = os.path.join(fPath, 'python_drill-1-files') # gets all files in directory and stores in allFiles
    
    for file in os.listdir(allFiles):
        if file.endswith(".txt"):
            abPath= os.path.join(allFiles, file)
            modifiedDate= time.strftime('%m/%d/%Y', time.gmtime(os.path.getmtime(abPath)))
            print('File Name: {} \nModified:{} \nFile Path: {}\n'.format(file,modifiedDate, abPath))
  
if __name__== '__main__':
    openFile()
