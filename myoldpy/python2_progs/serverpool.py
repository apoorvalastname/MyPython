#Design a system to support a pool of servers. The pool Api should be able to add a server, get a server (can be random) and delete a server from the pool.
#You need to design and implement an interface for such pool.
#The pool implementation should operate with a high performance so all operations need to be done in O(1).

serverpool={}
def addServer(sname,info):
   serverpool.update({sname:info})

def delServer(sname):
   if sname in serverpool.keys():
      del serverpool[sname]
      return
   print "No server data for ",sname
   
def printallservers():
   for server in serverpool:
      print server,':',serverpool[server]
def getServer(sname):
   if sname in serverpool.keys():
      print sname,':',serverpool[sname]
      return
   print "No server data for ",sname

addServer('server1','This is server 1')
addServer('server2','This is server 2')
addServer('server3','This is server 3')
addServer('server4','This is server 4')
addServer('server5','This is server 5')
addServer('server6','This is server 6')
printallservers()
getServer('server10')
getServer('server4')
delServer('server15')
delServer('server5')
printallservers()


