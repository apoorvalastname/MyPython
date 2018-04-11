mylist = ['apoorva','ram','gaurav','aarav','uddi','daddy','gaurav','nannamma','gaurav','gaurav']

i=0
mybkupstr=''
while i<len(mylist):
   myfinalstr=mybkupstr
   appustr=''
   for num,node in enumerate(mylist[i:]):
      if node=='gaurav': break
      if myfinalstr:myfinalstr+='->'
      myfinalstr+=node
      if appustr:appustr+=' , '
      appustr+=myfinalstr
   print 'Appustr : ',appustr
   if node == 'gaurav':
      print '!---- Appu found gaurav----!'
      mybkupstr=myfinalstr+'->'+node+'[x]'
   i+=(num+1)
      
print "-- len of the list : ",len(mylist)
for i,x in enumerate(mylist):
   parent = mylist[i-1]
   if not i: parent = None
   print "\n -- Apoorva --- %d "%i,x, parent

print "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n\n\n"

#print "\n mylist",mylist
#x = mylist.remove('gaurav')
#print "\n x",mylist

for x in mylist:
   
   print x
   if x=='gaurav': mylist.remove('gaurav') 


