file=open("tops.txt","r")
l1=[]
for i in file:
    l1.append(i.strip())
print(l1)

print("---------------")

filename = "tops.txt"  # replace with your file name
file_list = []

with open(filename, "r") as file:
    for line in file:
        file_list.append(line.strip())

print(file_list)
