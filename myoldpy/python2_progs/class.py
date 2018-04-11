from __future__ import print_function
import sys

class myClass:
   def __init__(self, field1=20, field2=30):
      print (" Base Class Init")
      self.myfield1 = field1*5
      self.myfield2 = field2+2

   def print_myfields(self):
      print (self.myfield1, self.myfield2)

   def test_print_formats(self):
      var1 = "a {0}".format("Apoorva")
      var2 = "b {0} {{0}}".format("Apoorva -- is ")

      print (var1,end="")
      print (var2)
      print (var2.format("name"))

      for s in sys.argv:
         print("{s}".format(s=s))
      self.print_myfields()

class myDerivedClass(myClass):
   def __init__(self, field1=11, field2=22):
      print (" Derived Class Init")
      myClass.__init__(self, field1, field2)

def main():
   print ("\n Creating Base Class \n")   
   newobj = myClass(100,200)
   newobj.test_print_formats()
   print ("\n Creating Derived Class \n")   
   newder = myDerivedClass()
   newder.test_print_formats()

if __name__ == "__main__" :
   main()

