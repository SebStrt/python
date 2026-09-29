#Vigenere

import string
import secrets as s

alphabet = string.ascii_lowercase + string.digits + string.punctuation

def genkey(length):
    return ''.join(s.choice(alphabet) for l in range(length))

def encrypt(ptext):
    
    key = ""
    ctext = []
    
    ptextarray = []
    keyarray = []
    ctextarray = []
    
    ptext = ptext.lower()
    
    ptext = ptext.replace("ä", "ae")
    ptext = ptext.replace("ö", "oe")
    ptext = ptext.replace("ü", "ue")
    ptext = ptext.replace("ß", "ss")
    ptext = ptext.replace (" ", "")
    
    key = genkey(len(ptext))

   
    for char in ptext:
        ptextarray.append(alphabet.find(char))
            
            
    for char in key:
        keyarray.append(alphabet.find(char))

    
    for x in range(len(ptextarray)):
        ctextarray.append((int(ptextarray[x] + int(keyarray[x])) % len(alphabet)))
    
    for x in ctextarray:
        ctext.append(alphabet[x])
    ctext = ''.join(ctext)

    return ctext, key


def decrypt(ctext, key):
    
    ptext = ""
    
    ptextarray = []
    ctextarray = []
    keyarray = []
    
    ctext = ctext.lower()
    key = key.lower()
    
    
    for char in ctext:
        ctextarray.append(alphabet.find(char))
            
            
    for char in key:
        keyarray.append(alphabet.find(char))
            
      
    for x in range(len(ctextarray)):
        ptextarray.append((int(ctextarray[x]) - int(keyarray[x])) % len(alphabet))
    
    for x in ptextarray:
        ptext = ptext + alphabet[x]
    return ptext

if __name__ == "__main__":
    



    print("Encrypt: 1")
    print("Decrypt: 2")
    print("----------")

    if input("Choose: ") == "1":
        ctext, key = encrypt(input("Please input plaintext: "))
        print("Ciphertext: " + ctext)
        print("Encryption key: " + key)

    else:
        print("Please input ciphertext: ")
        ctext = input()
        print("Please input key: ")
        key = input()
        ptext = decrypt(ctext, key)
        print("Decrypted text: " + ptext)
    
