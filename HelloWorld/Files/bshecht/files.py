
from shutil import copyfile 

def printfiles():
    print("files.py")

# 1. Write a Python program to read an entire text file.
def file_read(fname):
        txt = open(fname)
        print(txt.read())

# 2. Write a Python program to count the number of lines in a text file.
def file_lengthy(fname):
        with open(fname) as f:
                for i, l in enumerate(f):
                        pass
        return i + 1

#3. Write a Python program to write a list to a file.
def write_file(fname):
    print("File: ",fname)
    color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    with open(fname, "w") as myfile:
        for c in color:
            myfile.write("%s\n" % c)
    content = open(fname)
    print(content.read())

# 4. Write a Python program to copy the contents of a file to another file .
def copy_content_from_to_file(ffrom, fto):
    copyfile(ffrom,fto)

# 5-0. Write a Python program to read a file line by line and store it into a list.
def read_file_by_line(fname):
    content = open(fname)
    print(content.read())
    
def read_file_into_list(fname):
    with open(fname) as f:
        #Content_list is the list that contains the read lines.     
        content_list = f.readlines()
        print(content_list)

# this is a main procedere for defined exersice  
def main():
    printfiles()
    # 1
    file_read('test.txt')
    # 2
    print("Number of lines in the file: ",file_lengthy("test.txt"))
    # 3
    write_file("colors.txt")
    # 4
    copy_content_from_to_file("a.dat","b.dat")
    content = open("b.dat")
    print(content.read())
    # 5-0 read file lines
    read_file_by_line("genom.txt")
    # 5
    read_file_into_list("genom.txt")
    


if __name__=="__main__":
    main()