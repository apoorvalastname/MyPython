


def looknsay (n):
   nextn=[]
   p=1
   for i,char in enumerate(n):
      if i+1<len(n) and char==n[i+1]: 
         p+=1
      else:
         nextn.append(str(p)+str(char))
         p=1
   return ''.join(nextn)

if __name__=="__main__":
   num=raw_input("anynumber : ")
   n='1'
   i=0
   while i<int(num):
      print n
      n=looknsay(n)
      i+=1
   

