num = list(input('输入一串整数数组:'))
def char_int(a):
    dic = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,
           '6':6,'7':7,'8':8,'9':9
           }
    return dic[a]
num = list(map(char_int,num))
def removedull(num):
    index = 2
    if num is  None:
        return False
    for i, valuei in enumerate(num):
        if i in [0,1]:
            continue

        if num[index-2] != num[i]:#011123344555
            num[index] = num[i]
            index +=1



    return index
len1 = removedull(num)
print(num[:len1])
print(len1)


