list1 = [1,2,3,'hi',9]
print('list1',list1)
list1.append(10)
print('list1',list1)

list2 = [1,2,4,5]
print('list2',list2)
list2.append('6')
print('list2',list2)

list3 = []
print('list3',list3)
for i in range(5):
    list3.append(i)
print('list3',list3)

list4 = [1,2,3,4,5,6]
print('list4',list4)
list4.extend([7,8,9])
print('list4',list4)

list5 = [1,2,3,'hi',9]
print('list5',list5)
list5.remove('hi')
print('list5',list5)
list5.pop()
print('list5',list5)
list5.pop(1)
print('list5',list5)

list6 = [1,5,2,5,7,3,2,1]
print('list6',list6)
list6.clear()
print('list6',list6)

list7 = [1,5,2,5,7,3,2,1]
print('list7',list7)
list7.sort()
print('list7',list7)
list7.sort(reverse=True)
print('list7',list7)

list = []
n = 50
for i in range(1,n+1):
    if i%2 ==0:
        list.append(i)
print(list)
