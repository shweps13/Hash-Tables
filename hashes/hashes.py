import hashlib

key = b"str2" #byte string?
my_string = "just a string".encode()

# for i in range(10):
#     hashed = hashlib.sha256(key).hexdigest()
#     print(hashed)
    # hashed = hashlib.sha256(key)
    # breakpoint()

for i in range(10):
    hashed = hash(key)
    print(hashed % 8)

