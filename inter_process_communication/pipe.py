import os

r , w = os.pipe()

pid = os.fork()

if pid > 0:
    os.close(r)
    w = os.fdopen(w,'w')
    print("inside parent process !")
    n = int(input("enter the value of n : "))
    print("enter the numbers")
    s = ""
    for i in range(n):
        tmp = input()
        s += (str(tmp) + " ")
        
    w.write(s)
    w.close()
    
else:
    os.close(w)
    r = os.fdopen(r)
    s = r.read()
    s_items = s.split()
    print("inside child processes!")
    print("the numbers read from parent processes are")
    for item in s_items: print(item)
    r.close()

