# Write a Python Program to  open a Python file and read the first 25 character.
# Also, append a message to the file saying "I learnt File Handling today" using a variable.

vfile = open("sample.txt","r+")
print(vfile.read(25))
vfile.write("I learnt File Handling today")
vfile.close()
