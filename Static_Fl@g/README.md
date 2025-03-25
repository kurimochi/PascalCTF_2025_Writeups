# Static Fl@g
## English version
In `<script>` of `index.html`, there is a conditional branch called **`if (flag === atob('cGFzY2FsQ1RGe1MwX3kwdV9jNG5fVVMzXzFuc3BlY3RfM2wzbTNudF90MF9jaDM0dF9odWg/fQ=='))`**.  
Since its contents are base64, the flag can be obtained by reverting the original text with a Linux command or [CyberChef](https://gchq.github.io/CyberChef/).

The following is an example of output from the Linux command.
```shell
$ echo "cGFzY2FsQ1RGe1MwX3kwdV9jNG5fVVMzXzFuc3BlY3RfM2wzbTNudF90MF9jaDM0dF9odWg/fQ==" | base64 -d
# pascalCTF{S0_y0u_c4n_US3_1nspect_3l3m3nt_t0_ch34t_huh?}
```

## 日本語版
`index.html`の`<script>`には、 **`if (flag === atob('cGFzY2FsQ1RGe1MwX3kwdV9jNG5fVVMzXzFuc3BlY3RfM2wzbTNudF90MF9jaDM0dF9odWg/fQ=='))`** という条件分岐がある。  
この中身はbase64となっているため、Linuxコマンドや[CyberChef](https://gchq.github.io/CyberChef/)などでデコードするとフラグが入手できる。

以下はLinuxコマンドで出力した例だ。
```shell
$ echo "cGFzY2FsQ1RGe1MwX3kwdV9jNG5fVVMzXzFuc3BlY3RfM2wzbTNudF90MF9jaDM0dF9odWg/fQ==" | base64 -d
# pascalCTF{S0_y0u_c4n_US3_1nspect_3l3m3nt_t0_ch34t_huh?}
```
