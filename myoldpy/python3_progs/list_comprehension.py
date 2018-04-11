
def main():
   tuplelist = [(letter,number) for letter in "apoorva" for number in range (10) if number%2]
   print ("Tuple list ---> ",tuplelist)

   dictlist = {letter:number for letter,number in zip('apoorva' , range(8))}
   print ("Dict list ---> ",dictlist)

if __name__=="__main__":
   main()
