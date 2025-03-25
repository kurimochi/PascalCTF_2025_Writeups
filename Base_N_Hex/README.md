# Base N' Hex
## English version
I solved this problem in a very aggressive way. It may not be very helpful, but please take a look.

### Code analysis
The `encode` function in `basenhex.py` has the following statement.
```python
if random.randint(0, 1) == 0:
    return b64encode(input_string)
else:
    return input_string.hex().encode()
```
This is a statement that one-half of the plaintext is base64-encoded and the other half is hex-encoded. Also, as you can see from the for loop in `main`, it appears that the `encode` function is performed 10 times.

### Get Flag
These operations cause `UnicodeDecodeError` or `ValueError` if the wrong one decodes. To take advantage of this, conditional branching is performed using `try-catch`.
```python
from base64 import b64decode

with open("./output.txt", "r") as f:
    FLAG = f.read()

for i in range(10):
    try:
        FLAG = bytes.fromhex(FLAG).decode()
    except ValueError:
        FLAG = b64decode(FLAG).decode()

print(FLAG)
```
```shell
$ python3 solver.py
# pascalCTF{nex7_T1m3_ch3ck_cyb3rCH3F_$b64-d/e$}
```

## 日本語版
この問題だが、私はかなり強引な方法で解いた。あまり参考にならないかもしれないがぜひ見ていってほしい。

### コード解析
`basenhex.py`の`encode`関数には次のような文がある。
```python
if random.randint(0, 1) == 0:
    return b64encode(input_string)
else:
    return input_string.hex().encode()
```
これは平文を2分の1でbase64エンコードに、もう2分の1でhexエンコードにかけるといった文である。また`main`内のforループを見ればわかるように、`encode`関数は10回実行されているようだ。

### フラグの入手
これらの操作は間違ったほうでデコードすると`UnicodeDecodeError`あるいは`ValueError`が起こる。これを利用するために、`try-catch`を使って条件分岐を行っていく。
```python
from base64 import b64decode

with open("./output.txt", "r") as f:
    FLAG = f.read()

for i in range(10):
    try:
        FLAG = bytes.fromhex(FLAG).decode()
    except ValueError:
        FLAG = b64decode(FLAG).decode()

print(FLAG)
```
```shell
$ python3 solver.py
# pascalCTF{nex7_T1m3_ch3ck_cyb3rCH3F_$b64-d/e$}
```