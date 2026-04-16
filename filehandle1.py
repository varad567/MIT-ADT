file = open("mylife.txt", "w")
file.write("I am learning Python.\n")
file.close()


file = open("mylife.txt", "a")
file.write(" \n I am enjoying it.\n")
file.close()



file = open("mylife.txt", "r")
content = file.read()
print(content)
file.close()