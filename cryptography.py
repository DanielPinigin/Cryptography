"""
cryptography.py
Author: Daniel
Credit: 

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

#eord = input("Enter e to encrypt, d to decrypt, or q to quit: ")

mes = input("Message: ")
mes = list(mes)
print(mes)
    
message = [associations.find(x) for x in mes]
print(message)

key = input("Key: ")
key = [associations.find(x) for x in key]
print(key)


#Code that adds key to the message
