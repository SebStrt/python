import Vignere as v
from tkinter import *
from tkinter import ttk

print("Encrypt: 1")
print("Decrypt: 2")
print("----------")

if input("Choose: ") == "1":
    ctext, key = v.encrypt(input("Please input plaintext: "))
    print("Ciphertext: " + ctext)
    print("Encryption key: " + key)

else:
    print("Please input ciphertext: ")
    ctext = input()
    print("Please input key: ")
    key = input()
    ptext = v.decrypt(ctext, key)
    print("Decrypted text: " + ptext)




