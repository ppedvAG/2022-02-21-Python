import rsa

# publicKey, privateKey = rsa.newkeys(512)
# print(publicKey)
# print(privateKey)
# pk[1].save_pkcs1("PEM")
# with open("blabla.pem", "wb+") as f:
#     key = privateKey.save_pkcs1("PEM")
#     f.write(key)
#
# with open("encrypted.txt", "wb+") as f:
#     text = "Streng geheim"
#     text = rsa.encrypt(text.encode(), publicKey)
#     f.write(text)


with open("blabla.pem", "rb") as f:
    pem = f.read()
privateKey = rsa.PrivateKey.load_pkcs1(pem)
# print(privateKey)
with open("encrypted.txt", "rb") as f:
    encryptedStr = f.read()
text = rsa.decrypt(encryptedStr, privateKey).decode()
print(text)
