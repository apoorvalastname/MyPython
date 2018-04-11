list1 = ['a','b','c','d','e','f']
print list1, len(list1)
list2 = reversed(list1)
print list2,#len(list2)
list3 = [item for item in reversed(list1)]
print list3,len(list3)
mystr = '''
      apoorva this is a string testing !!
      multiline string testing
'''
mystr+='''
      please do print this line also !!!
'''
print mystr
list3str = 'appu:'.join(list3)
print list3str
