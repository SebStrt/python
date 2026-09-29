import Vignere as v

print("Encrypt: 1")
print("Decrypt: 2")
print("----------")

if input("Choose: ") == "1":
    v.encrypt(input("Please input plaintext: "))
    print("Ciphertext: " + v.ctext)
    print("Encryption key: " + v.key)




