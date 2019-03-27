a= [1,2,3,4,5,77]

a.append(20)  #append添加數值在陣列後面
a.insert(0,50) #insert 在第a陣列中 加入b值
a.remove(5)  #remove 移除某value 而不是序列值
print(a)

print(a[0:3])  #print 陣列0~2位
print(a[:3]) #print list 0~2位
print(a[3:]) #print list 3~最後一位

print(a.index(77)) #print index索引 輸入value
print(a.count(2)) #count 計數

a.sort(reverse=True) #sort 排序 reverse=true 由大到小
print(a)



## 多維陣列

a = [[1,2,3],
     [2,3,4],
     [3,4,5]]

print(a[2][2])  #print 5 


## 字典 dictornary 需要一個key 一個value(可以是一個值、一個list、一個字典...)

a_list = [1,2,45,346,345,2,36,0]
d = {'apple':1, 'pear':2, 'orange':[10,20,30]}
d2 = {1:'a', 2:'b', 3:'c'}

print(d['pear'])

del d['apple'] #delete 一個元素

d['happy']= 20 #create 一個元素 但沒有順序性


print(d['orange'][2])   #print 30


