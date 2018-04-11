a=[{'name':'Apoorva','place':'France'},{'name':'Ram','place':'SF'},{'name':'Gaurav','place':'Australia'},{'name':'Aarav','place':'LegoLand'}]

key='gaurav'
myplace = [x['place'] for x in a if x['name']==key]
print key, ' is from ',myplace

for x in a :
   print '\n ',x['name'], ' is from ',x['place']


list1=[1,2,3,4,5]
list2=[1,2,6,7,8,9]
for i in list(set(list1+list2)):
   print '\n Apoorva -- this is i %d' %i









