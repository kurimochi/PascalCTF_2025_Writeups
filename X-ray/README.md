# X-ray
## English version
### Decompile
I'll run it anyway.
```shell
$ ./x-ray
Insert the secret code: test
Sorry, the secret code is wrong!
```
Decompiled by Ghidra and others, I found the `checkSignature` function.
```c
undefined8 checkSignature(char *param_1)

{
  size_t sVar1;
  undefined8 uVar2;
  uint local_c;
  
  sVar1 = strlen(param_1);
  if (sVar1 == 18) {
    for (local_c = 0; local_c < 18; local_c = loca l_c + 1) {
      if ((char)(param_1[(int)local_c] ^ key[(in t)local_c]) != encrypted[(int)local_c]) {
        return 0;
      }
    }
    uVar2 = 1;
  }
  else {
    uVar2 = 0;
  }
  return uVar2;
}
```
Information about the secret code can be read from the `checkSignature` function.
- **for (local_c = 0; local_c < 18; local_c = loca l_c + 1)** -> *Secret code is 18 characters*
- **if ((char)(param_1[(int)local_c] ^ key[(in t)local_c]) != encrypted[(int)local_c])** -> *Secret code and `key` xor compared to `encrypted`*

### Dynamic Analysis
Use these information to get `key` and `encrypted` in `gdb`.
```shell
$ gdb x-ray
pwndbg> b *0x5555555551c3
Breakpoint 1 at 0x5555555551c3
pwndbg> b *0x5555555551d5
Breakpoint 2 at 0x5555555551d5
pwndbg> r
Insert the secret code: dummydummydummydum
Breakpoint 1, 0x00005555555551c3 in checkSignature ()
-----[ REGISTERS / show-flags off / show-compact-regs off ]-----
RDX  0x555555556010 (key) ◂— '*7^tVr4FZ#7S4RFNd2'

pwndbg> c
Continuing.

Breakpoint 2, 0x00005555555551d5 in checkSignature ()
-----[ REGISTERS / show-flags off / show-compact-regs off ]-----
*RDX  0x555555556030 (encrypted) ◂— 0x1907472447085278
pwndbg> x/s $rdx
0x555555556030 <encrypted>:     "xR\bG$G\a\031kPhgCa5~\t\001"
```

### Obtain secret codes and flags
I was able to get the `key` and `encrypted` by dynamic analysis, so I can now get the secret code.
```python
key = [ord(i) for i in list("*7^tVr4FZ#7S4RFNd2")]
encrypted = [ord(i) for i in list("xR\bG$G\a\031kPhgCa5~\t\001")]

print(''.join([chr(k ^ c) for k, c in zip(key, encrypted)]))
```
```shell
$ python3 solver.py
ReV3r53_1s_4w3s0m3
```
Now all you have to do is enter the secret code to get the flag.
```shell
$ ./x-ray 
Insert the secret code: ReV3r53_1s_4w3s0m3
Congrats! You have found the secret code, pascalCTF{******************}
```

## 日本語版
### 逆コンパイル
とりあえず実行してみる。
```shell
$ ./x-ray
Insert the secret code: test
Sorry, the secret code is wrong!
```
Ghidraなどで逆コンパイルし、`checkSignature`関数を見つけた。
```c
undefined8 checkSignature(char *param_1)

{
  size_t sVar1;
  undefined8 uVar2;
  uint local_c;
  
  sVar1 = strlen(param_1);
  if (sVar1 == 18) {
    for (local_c = 0; local_c < 18; local_c = loca l_c + 1) {
      if ((char)(param_1[(int)local_c] ^ key[(in t)local_c]) != encrypted[(int)local_c]) {
        return 0;
      }
    }
    uVar2 = 1;
  }
  else {
    uVar2 = 0;
  }
  return uVar2;
}
```
`checkSignature`関数からシークレットコードに関する情報が読み取れる。
- **for (local_c = 0; local_c < 18; local_c = loca l_c + 1)** -> *シークレットコードは18文字*
- **if ((char)(param_1[(int)local_c] ^ key[(in t)local_c]) != encrypted[(int)local_c])** -> *シークレットコードと`key`をxorして`encrypted`と比較している*

### 動的解析
これらの情報を利用して、`gdb`で`key`と`encrypted`を取得する。
```shell
$ gdb x-ray
pwndbg> b *0x5555555551c3
Breakpoint 1 at 0x5555555551c3
pwndbg> b *0x5555555551d5
Breakpoint 2 at 0x5555555551d5
pwndbg> r
Insert the secret code: dummydummydummydum
Breakpoint 1, 0x00005555555551c3 in checkSignature ()
-----[ REGISTERS / show-flags off / show-compact-regs off ]-----
RDX  0x555555556010 (key) ◂— '*7^tVr4FZ#7S4RFNd2'

pwndbg> c
Continuing.

Breakpoint 2, 0x00005555555551d5 in checkSignature ()
-----[ REGISTERS / show-flags off / show-compact-regs off ]-----
*RDX  0x555555556030 (encrypted) ◂— 0x1907472447085278
pwndbg> x/s $rdx
0x555555556030 <encrypted>:     "xR\bG$G\a\031kPhgCa5~\t\001"
```

### シークレットコードとフラグの入手
動的解析で`key`と`encrypted`を取得できたので、シークレットコードを入手することができるようになった。
```python
key = [ord(i) for i in list("*7^tVr4FZ#7S4RFNd2")]
encrypted = [ord(i) for i in list("xR\bG$G\a\031kPhgCa5~\t\001")]

print(''.join([chr(k ^ c) for k, c in zip(key, encrypted)]))
```
```shell
$ python3 solver.py
ReV3r53_1s_4w3s0m3
```
あとはシークレットコードを入力してフラグを入手するだけだ。
```shell
$ ./x-ray 
Insert the secret code: ReV3r53_1s_4w3s0m3
Congrats! You have found the secret code, pascalCTF{******************}
```