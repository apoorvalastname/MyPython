
class mysort:
   def __init__(self,a):
      self.a=a
   def mergesort(self):
      self.a=sort_r(self.a)
   def print_a(self):
      print (self.a)

def sort_r(mid):
   if len(mid)==1 or len(mid)==0:
      return mid
   midval=int(len(mid)/2)
   x=sort_r(mid[:midval])
   y=sort_r(mid[midval:])
   return merge(x,y)
   
def merge(a, b):
   newlist=[]
   while len(a) and len(b):
      if a[0]<b[0]:
         newlist.append(a[0])
         a.remove(a[0])
      else:
         newlist.append(b[0])
         b.remove(b[0])
   if len(b):
      newlist+=b
   if len(a):
      newlist+=a
   return newlist
   
if __name__=="__main__":
   sort1 = mysort([4,2,6,8,7,1,5,9,3])
   sort1.print_a()
   sort1.mergesort()
   sort1.print_a()
