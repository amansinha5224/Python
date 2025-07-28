'''
File Modes:-
    - r (default)       - w         - a
    - r+ (read + write) - w+        - a+ (append + read)
    - rb                - wb        - ab
    - rb+               - wb+       - ab+
'''

# Read Mode
f = open("C:/Users/user/Desktop/Python/28_FileHandling/myfile.txt", "r")

text = f.read()
print(text)
f.close()

# Append Mode
f = open("C:/Users/user/Desktop/Python/28_FileHandling/myfile.txt", "a")

f.write("\nThis is new line append in file")
f.close()

# With Operation: Need not to close the file
with open("C:/Users/user/Desktop/Python/28_FileHandling/myfile.txt", "a") as f:
    f.write("\nAppend new line using with keyword")

# readline(): Able to read line by line
f = open("C:/Users/user/Desktop/Python/28_FileHandling/myfile.txt", "r")

while True:
    line = f.readline()
    print(line)

    if(not line):
        break

# seek(): Helps to move coursor more starting to a file till desired location, position is specificed in bytes and can move forward or direction backward from current position
with open("C:/Users/user/Desktop/Python/28_FileHandling/myfile.txt", "r") as f:
    f.seek(10)

    # tell(): Tell wheather the reading starts form (Tells current position of coursor in bytes)
    currentPosition = f.tell()
    print(currentPosition)  # 10

    data = f.read(5)
    print(data)

# turncate(): Specifies the number of characters soulf remain in the file
with open("C:/Users/user/Desktop/Python/28_FileHandling/helloWorld.txt", "w+") as f:
    f.write("Hello World!")
    f.seek(0)
    print(f.read()) # Hello World!
    
    f.truncate(5)
    f.seek(0)
    print(f.read()) # Hello