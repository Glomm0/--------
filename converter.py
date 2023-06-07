data=[]
with open("examples.txt",'r') as file:
    data=file.read().split(",\n")
new_data=[]
for i in data:
    temp=''
    for j in i:
        if j==",":
            temp+="&"
        else:
            temp+=j
    new_data.append(temp)
with open("expales2.txt",'w')as file:
    file.write(",\n".join(new_data))

    