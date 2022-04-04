import os 

def main():
    r , w = os.pipe()
    r1 , w1 = os.pipe()

    pid = os.fork()
    
    if pid:
        os.close(w)
        os.close(r1)
        w_obj = os.fdopen(w1,"w")
        s = str(input("enter the string "))
        w_obj.write(s)
        w_obj.close()
        r_obj = os.fdopen(r)
        result = r_obj.read()
        if int(result) > 0:
            print("The string is palindrome ")
        else:
            print("The string is not palindrome")

    else:
        os.close(w1)
        os.close(r)

        r_obj = os.fdopen(r1)
        s = r_obj.read() 
        is_palindrome = str(1) if (s == s[::-1]) else str(0)
    
        w_obj = os.fdopen(w,"w") 
        w_obj.write(is_palindrome)
        w_obj.close()

main() 

