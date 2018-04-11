def returnname(xpath):
   returnname.index +=1
   if returnname.index == 2:
      return 'Apoorva'
   else:
      return None

if __name__=='__main__':
   myxpath='/apoorva:ram/apoorva:gaurav/apoorva:aarav'
   returnname.index=0
   cb=None
   n=1
   xpath=myxpath.split('/')[:-n]
   while len(xpath)>1:
      n+=1
      cb=returnname(xpath)
      if cb is not None: break
      xpath=myxpath.split('/')[:-n]
   print "parent node : ",xpath ,'/'.join(xpath)



