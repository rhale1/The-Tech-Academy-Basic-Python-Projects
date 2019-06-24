import sqlite3
import os

#For this drill, write a script that creates a database and adds new data into that database

#Your db will require 2 fields, an auto-increment primary integer field and a field with the data type of string.
#Your script will need to read from the supplied list of file names and determine only the files from the list which ends with a “.txt” file extension.
#Next, your script should add those file names from the list ending with “.txt” file extension within your database.
#Finally, your script should legibly print the qualifying text files to the console.

#fileList = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt', 'data.pdf','myPhoto.jpg')


def start():
    fileList = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt', 'data.pdf','myPhoto.jpg')
    tempList = []

    for file in fileList:
        if file.endswith('.txt'):
            tempList.append(file)

    conn = sqlite3.connect('txtfiles.db') #db connection
    with conn:
        cur = conn.cursor() #cursor object stored in cur 
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_txtfiles ( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, col_fileName TEXT)")
        for i in tempList:
            cur.execute("INSERT INTO tbl_txtfiles (col_fileName) VALUES (?)",[i])
        conn.commit()
    conn.close()

    for i in tempList:
        print("File Name: {}".format(i))

if __name__=='__main__':
    start()



