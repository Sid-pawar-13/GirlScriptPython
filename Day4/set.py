list1 = [1,2,3,40]
print(list1)
print(type(list1))
set1 = set(list1)
print(set1)
print(type(set1))

set2 = {}
print(type(set2))
set3 = set()
print(type(set3))

set4 = set([1,2,3,4,5,6,7])
print(set4)
set4.add(8)
print(set4)
set4.add(3)
print(set4)
set4.remove(8)
print(set4)
set4.pop()
print(set4)
set4.discard(8)
print(set4)
set4.clear()
print(set4)

A = {'red','blue','orange','green'}
B = {'black','white','pink','green','red'}
print(A|B) #pip
C = A.union(B)
print(C)

print(A&B)
print(A.intersection(B))

print(A-B)
print(A.difference(B))

print('green' in A)
print(A==B)
print(A!=B)
print(A<=B) # subset
print(A<B) # proper subset
print(A^B) # returns elements which are not common
