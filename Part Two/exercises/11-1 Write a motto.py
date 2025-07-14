import os

# Obtain current python file's path
path = os.path.dirname(os.path.abspath(__file__))

# create a file!
new_file = open(path + '/motto.txt', 'w')

try:
    new_file.write("Fiat Lux!")

except IOError:
    print('IO Error! Please check valid file names and paths')

finally:
    new_file.close()
    print("File created successfully with the motto!")

# open the file again to read its content + write more content
try:
    new_file = open(path + '/motto.txt', 'r+')
    content = new_file.read()
    print("Content of the file:", content)
    new_file.write("\nLet there be light!")

except IOError:
    print('IO Error! Please check valid file names and paths')

finally:
    new_file.close()
    print("File read successfully.")