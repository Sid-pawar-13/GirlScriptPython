dict1 = {}
print('dict1 :',dict1)
print('type(dict1) :',type(dict1))

dict2 = {1:'A',2:'B',3:'c',4:'d'}
print('dict2 :',dict2)

dict3 = dict([(1,'hi'),(2,'i am'),(3,'fine')])
print('dict3 :',dict3)
print('keys :',dict3.keys())
print('values :',dict3.values())
print('dict3[1] :',dict3[1])

dict4 = {1:'a',2:'b',3:'c',4:'d',5:['e','f'],6:{'A':'hi','B':'I','C':'am'}}
print('dict4 :',dict4)
print('dict4 :',dict4[5])
print('dict4[5][1]',dict4[5][1])
print('dict4[6]',dict4[6])
print('dict4[6]["B"]',dict4[6]["B"])

dict5 = {1:'a',2:'b',3:'c',4:'d'}
print('dict5 :',dict5)
dict5[5] = 'e'
print('dict5 :',dict5)
dict5.pop(5)
print('dict5 :',dict5)
dict5.clear()
print('dict5 :',dict5)

dict6 = {1:'a',2:'b',3:'c',4:'d'}
dict7 = {5:'e',6:'f'}
print(dict6)
print(dict7)
dict6.update(dict7)
print(dict6)

del dict7
print(dict7)
