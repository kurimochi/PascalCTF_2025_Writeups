# Romañs Empyre
## English version
### Code analysis
The `romanize` function in `romans_empire.py` indicates that the server in question has Caesar cipher encryption.
```python
import os, random, string

alphabet = string.ascii_letters + string.digits + "{}_-.,/%?$!@#"
FLAG : str = os.getenv("FLAG")
assert FLAG.startswith("pascalCTF{")
assert FLAG.endswith("}")

def romanize(input_string):
    key = random.randint(1, len(alphabet) - 1)
    result = [""] * len(input_string)
    for i, c in enumerate(input_string):
        result[i] = alphabet[(alphabet.index(c) + key) % len(alphabet)]
    return "".join(result)

if __name__ == "__main__":
    result = romanize(FLAG)
    assert result != FLAG
    with open("output.txt", "w") as f:
        f.write(result)
```
`alphabet = string.ascii_letters + string.digits + "{}_-.,/%?$!@#"` represents the characters used. In this case, it seems to set the ascii printable string.

### Cracking
Ciphers such as the Caesar cipher are extremely vulnerable to brute force attacks on keys, so they are used to crack them.

For example, in Python, the code would look like this:
```python
import string
alphabet = string.ascii_letters + string.digits + "{}_-.,/%?$!@#"

def brute_force_decrypt(encrypted_str):
    results = []
    for key in range(1, len(alphabet)):
        decrypted = []
        for c in encrypted_str:
            original_index = (alphabet.index(c) - key) % len(alphabet)
            decrypted.append(alphabet[original_index])
        results.append((key, "".join(decrypted)))
    return results

encrypted = "TEWGEP6a9rlPkltilGXlukWXxAAxkRGViTXihRuikkos"
flag = brute_force_decrypt(encrypted)
for attempt in flag:
    print(f"Key {attempt[0]:2d}: {attempt[1]}")
```
It can also be solved in C++ with the following code:
```c++
#include <bits/stdc++.h>
using namespace std;

string decrypt(string encrypted, string chars, int key) {
    string decrypted;
    for (int i = 0; i < encrypted.size(); i++) {
        int origin_index = (chars.find(encrypted.at(i)) - key + chars.size()) % chars.size();
        decrypted += chars.at(origin_index);
    }
    return decrypted;
}

int main() {
    string encrypted = "TEWGEP6a9rlPkltilGXlukWXxAAxkRGViTXihRuikkos";
    string alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{}_-.,/%?$!@#";

    for (int i = 1; i <= alphabets.size(); i++) {
        string results = decrypt(encrypted, alphabets, i);
        cout << "Key " << i << ": " << results << endl;
    }
}
```

```shell
$ python3 solver.py
...
# Key 30: pascalCTF{*********************************}
...
```
The flag was obtained with key 30.

## 日本語版
### コード解析
`romans_empire.py`の`romanize`関数から、この問題のサーバーではシーザー暗号の暗号化が行われていることがわかる。
```python
import os, random, string

alphabet = string.ascii_letters + string.digits + "{}_-.,/%?$!@#"
FLAG : str = os.getenv("FLAG")
assert FLAG.startswith("pascalCTF{")
assert FLAG.endswith("}")

def romanize(input_string):
    key = random.randint(1, len(alphabet) - 1)
    result = [""] * len(input_string)
    for i, c in enumerate(input_string):
        result[i] = alphabet[(alphabet.index(c) + key) % len(alphabet)]
    return "".join(result)

if __name__ == "__main__":
    result = romanize(FLAG)
    assert result != FLAG
    with open("output.txt", "w") as f:
        f.write(result)
```

`alphabet = string.ascii_letters + string.digits + "{}_-.,/%?$!@#"`は使用文字を表している。この場合、asciiの印字可能文字列を設定しているようだ。

### クラッキング
シーザー暗号のような暗号は鍵のブルートフォース攻撃に極めて脆弱なためそれを利用してクラッキングする。

例えばPythonでは、以下のようなコードになる。
```python
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
```
またC++でも、次のコードで解くことができる。
```c++
#include <bits/stdc++.h>
using namespace std;

string decrypt(string encrypted, string chars, int key) {
    string decrypted;
    for (int i = 0; i < encrypted.size(); i++) {
        int origin_index = (chars.find(encrypted.at(i)) - key + chars.size()) % chars.size();
        decrypted += chars.at(origin_index);
    }
    return decrypted;
}

int main() {
    string encrypted = "TEWGEP6a9rlPkltilGXlukWXxAAxkRGViTXihRuikkos";
    string alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{}_-.,/%?$!@#";

    for (int i = 1; i <= alphabets.size(); i++) {
        string results = decrypt(encrypted, alphabets, i);
        cout << "Key " << i << ": " << results << endl;
    }
}
```
```shell
$ python3 solver.py
...
# Key 30: pascalCTF{*********************************}
...
```
鍵30でフラグを入手できた。