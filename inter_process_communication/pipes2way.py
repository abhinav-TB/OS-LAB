import os 

def isPrime(num):
    if num == 1:
        return False
    for i in range(2 , (num//2)+1):
        if num % i == 0:
            return False

    return True



def main():
    r , w = os.pipe()
    r1 , w1 = os.pipe()

    pid = os.fork()
    
    if pid:
        os.close(w)
        os.close(r1)
        w_obj = os.fdopen(w1,"w")
        n = int(input("enter the value of n"))
        print("enter the numbers")
        s = ""
        for i in range(n):
            temp = str(input())
            s += (temp + " ")
        w_obj.write(s)
        w_obj.close()
        r_obj = os.fdopen(r)
        result = r_obj.read()
        if len(result) > 0:
            print("the prime  numbers are " , result)
        else:
            print("There are no prime numbers")


    else:
        os.close(w1)
        os.close(r)

        r_obj = os.fdopen(r1)
        numbers = map(int , r_obj.read().split())
        primes = ""
        for number in numbers:
         if isPrime(number):
             primes = primes + str(number) + " "
             
        
        w_obj = os.fdopen(w,"w") 
        w_obj.write(primes)
        w_obj.close()

main() 


    
