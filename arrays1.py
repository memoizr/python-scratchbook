array = [1,2,3,4]

def pigarray(a, b):
  print array[a] + array[b]
  
#pigarray(0,2)

array = ["pig","fig","tig","tag","toog"]

def hellopig(a):
  print "hello " + array[a]
  
#hellopig(1)


def hellotig(a):
  if (array[a] == "tig"):
    print ("dee hee hee deep")
  else:
    print ("oh man!")
                                                                                
#hellotig(2)
 
 
def allpigs(pigs):
  for pig in pigs:
    print "hello " + pig
    
allpigs(array)
  
  
  
   