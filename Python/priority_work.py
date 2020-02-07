# input
str = input()
str1, str2 = str.split(" ")
n, m = int(str1), int(str2)
lst = []
dic = {}
for i in range(0, m):
    flag_str1 = 1
    flag_str2 = 1
    str = input()
    str1, str2 = str.split(" ")

    # insert in list
    for i in lst:
        if i == str1:
            flag_str1 = 0
        if i == str2:
            flag_str2 = 0
    if flag_str1:
        lst.append(str1)
    if flag_str2:
        lst.append(str2)

    # insert in dictionary
    try:
        dic[str1].append(str2)
    except:
        dic[str1] = []
        dic[str1].append(str2)



#print("Relation : ", dic)
#print("Inputs : ", lst)


# function
output = []
lst2 = [] # [1, 2]
lst3 = []
for i in dic:
    lst2.append(i)

flag = 1
while len(lst):
    a = lst.pop(0)
    try:
        for b in dic[a]:
            for i in dic[b]:
                if i == a:
                    flag = 3
                    break
    except:
        pass
    if flag == 3:
        break
    f = 1
    for b in output:
        if a==b:
            f = 0
    if f:
        x = a
        i = 0
        while i < len(lst2):
            flag = 0
            y = lst2[i]
            for j in dic[y]:
                if x == j:
                    for b in output:
                        if y==b:
                            flag = 2
                            break
                    if flag == 2:
                        break
                    lst.insert(0,x)
                    x = y
                    flag = 1
                    break
            if flag == 1:
                i = 0
            elif flag == 3:
                break
            else:
                i += 1
        output.append(x)
    if flag == 3:
        break


if flag != 3:
    str = ""
    for i in output:
        str = str + i + " "
    print(str)
else:
    print("Not Possible")