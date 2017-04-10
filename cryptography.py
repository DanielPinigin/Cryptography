"""
cryptography.py
Author: Daniel
Credit: Brendan

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
#Enter e to encrypt, d to decrypt, or q to quit: z
#Did not understand command, try again.
#Enter e to encrypt, d to decrypt, or q to quit: e
#Message: Two plus two = Five
#Key: Lorem ipsum
#+KF;B(CH=NIZ}m;R\Dt
#Enter e to encrypt, d to decrypt, or q to quit: d
#Message: +KF;B(CH=NIZ}m;R\Dt
#Key: Lorem ipsum
#Two plus two = Five
#Enter e to encrypt, d to decrypt, or q to quit: q
#Goodbye!
#___________________________________________________________________________________________________________________

associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
thing = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
t = 1
while t == 1:
    inp = input("Enter e to encrypt, d to decrypt, or q to quit: ")
    if inp == "e":
        mes = input("Message: ")
        #mes = ("test")
        mes = list(mes)
        #print(mes)
    
        message = [thing.find(x) for x in mes]
        #print(message)
    
        key = input("Key: ")
        #key = ("hi")
        key = [thing.find(x) for x in key]

        b = len(message)/len(key)
        b = int(b)
        c = b*key
        #print(c)

        ultracode = zip(message, c)
        ultracode = list(ultracode)
        g = [x+y for x,y in ultracode]
        #print(g)

        enc = [thing[x] for x in g]
        print("".join(enc))
    elif inp == "d":
        mes = input("Message: ")
        #mes = ("test")
        mes = list(mes)
        #print(mes)
    
        message = [thing.find(x) for x in mes]
        #print(message)
    
        key = input("Key: ")
        #key = ("hi")
        key = [thing.find(x) for x in key]

        b = len(message)/len(key)
        b = int(b)
        c = b*key
        #print(c)

        ultracode = zip(message, c)
        ultracode = list(ultracode)
        g = [x-y for x,y in ultracode]
        #print(g)
        
        enc = [thing[x] for x in g]
        print("".join(enc))
    elif inp == "q":
            t = 2
            print("Goodbye!")
    else:
        print("Did not understand command, try again.")

#________________________________________________________________________________________________________________








