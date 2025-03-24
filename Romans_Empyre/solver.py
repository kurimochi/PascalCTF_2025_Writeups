import string

def decrypt(encrypted, chars, key):
    decrypted = []
    for c in encrypted:
        origin_index = (chars.index(c) - key) % len(chars)
        print(origin_index, end=" ")
        decrypted.append(chars[origin_index])
    return "".join(decrypted)

def main():
    encrypted = "TEWGEP6a9rlPkltilGXlukWXxAAxkRGViTXihRuikkos"
    alphabets = string.ascii_letters + string.digits + "{}_-.,/%?$!@#"
    for i in range(1, len(alphabets)):
        flag = decrypt(encrypted, alphabets, i)
        print(f"Key {i}: {flag}")

if __name__ == '__main__':
    main()
    