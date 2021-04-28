# Import sqlite3 & os modules
# sqlite3 will help us interact with our database
import sqlite3

fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')
txtFiles = []

# This for loop will iterate over the values in
# fileList and find .txt file and store them in
# the txtFiles list variable.
for file in fileList:
    if file.split('.')[1] == 'txt':
        txtFiles += [file]

# Initialize connection with database
connection = sqlite3.connect('database_assignment.db')

# While the connection variable hold a token from the DB
# to create the table required for assignment if table does not exist.
# Then, we add in the values stored in the txtFiles variable to the table.
with connection:
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS tbl_files ( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        file_name TEXT \
        )")
    connection.commit()

    for file in txtFiles:
        fileName = file.split('.')[0]
        cursor.execute("INSERT INTO tbl_files (file_name) VALUES (?)", (fileName,))

    connection.commit()
connection.close()

# Display the qualifying text files to the console.
print('Here are the qualifying text files:\n')
for file in txtFiles:
    print('\t'+file)
