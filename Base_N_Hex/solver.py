from base64 import b64decode

with open("./output.txt", "r") as f:
    FLAG = f.read()

for i in range(10):
    try:
        FLAG = bytes.fromhex(FLAG).decode()
    except ValueError:
        FLAG = b64decode(FLAG).decode()

print(FLAG)
