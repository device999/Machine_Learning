

if __name__ == '__main__':
    # Write a Python program to read an entire text file.   
    # Write a Python program to copy the contents of a file to another file . 
    newFile = open("./HelloWorld/Files Math/device999/demo.txt","r")
    cloneFile = open("./HelloWorld/Files Math/device999/clone.txt","w+")
    if newFile.mode == 'r':
        contents =newFile.read()
        #print(contents)
    cloneFile.write(contents)
    cloneFile.close()
    # Write a Python program to count the number of lines in a text file.
    # Write a Python program to read a file line by line and store it into a list
    input_list = []
    with open("./HelloWorld/Files Math/device999/demo.txt") as f:
        for i, l in enumerate(f):
                input_list.append(l)
    print(str(i+1)+ " lines")
    print(input_list)
    newFile.close()
    # Write a Python program to write a list to a file.
    str_list = ["Hello", "World", " Benjamin"]
    
    appendFile=open("./HelloWorld/Files Math/device999/demo.txt", "a+")
    appendFile.write("\r\n")
    for i in str_list:
        appendFile.write(i)
        appendFile.write("\r\n")
    appendFile.close()
    