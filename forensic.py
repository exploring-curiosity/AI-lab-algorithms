import hashlib

i = 0
while True:
    str_ = "Mallory Rules CryptoLand" + str(i)
    result = str(hashlib.sha256(str_.encode()).hexdigest())
    if result[0:4] == "0000":
        print(i)
        break
    i += 1
'''
74164
'''
