class Iterator:
   def __init__(self,val):
      self.val=val
      self.index=len(val)
   def __iter__(self):
      return self
   def __next__(self):
      if not self.index : 
         raise StopIteration
      self.index -=1
      return self.val[self.index]
   def printval(self):
      print ("val : {} index : {}".format(self.val,self.index))
class DictIterator(Iterator):
   def __init__(self,val):
      Iterator.__init__(self,val)
      self.key = self.val.keys()
      print (self.key)
      print (self.key[0])
   def __iter__(self):
      return self
   def __next__(self):
      if not self.index:
         raise StopIteration
      self.index-=1
      return(self.key[self.index],self.val[self.key[self.index]])
   def printval(self):
      super().printval()

def main():
   myiter = Iterator("Apoorva")
   for i in myiter:
      print (i)
   myiter.printval()

   mylistiter = Iterator([1,2,3,4,5,6,7])
   for x in mylistiter:
      print (x)

   mydictiter = DictIterator({1:"Apoorva", 2:"Gaurav", 3:"Ram", 4:"Aarav"})
   mydictiter.printval()
   for key,val in mydictiter:
      print (key, val)

if __name__=="__main__":
   main()
