file = open("files.txt","r")

# cara 1
# print(file.readlines())

# cara 2 
listStatement = []

for f in file.readlines():
  listStatement.append(f.rstrip())

print(listStatement)