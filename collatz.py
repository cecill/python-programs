def collatz(t):
 if (t % 2) == 1:
  return (3 * t + 1)
 else:
  return (t // 2)
  
count = 0
num = 1

while num != 100:
    print (collatz(num))
    num = collatz(num)
    count = count + 1
    print ("Number =", num, " Iterations =", count)
    num = num + 1 
 
