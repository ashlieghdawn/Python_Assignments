import sqlite3

conn = sqlite3.connect('drill.db')

fileList = ('information.docx','Hello.txt','myImage.png',\
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

# Find files that end with .txt, aka text files
def findTxt():
    for i in fileList:
        if i.endswith('.txt'):
            txtFiles = i
            print(txtFiles)
            insertData(txtFiles)
            

# Insert that data into database
def insertData(txtFiles):
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_file(col_doctype) VALUES (?)", \
          (txtFiles,))
    conn.commit() #commit changes to database
    



# create database for drill
def createDB():
    conn = sqlite3.connect('drill.db') # Connect to database
    with conn: # with the connection
        cur = conn.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS tbl_file(\
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_doctype TEXT \
            )')
        conn.commit() # commit changes to database
    conn.close() # close connection
    findTxt()
    
createDB() # runs the function createDB which will print the text files for dev.
