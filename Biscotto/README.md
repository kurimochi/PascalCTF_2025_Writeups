# Biscotto
## English version
### Source analysis
This time the problem is in the white box. After extracting the `challenge.zip` and checking the source code, `server.js`, I found an interesting statement.
```javascript
app.get("/me", (req, res) => {
    const username = req.cookies.user;
    if (!username || username !== "admin") {
        res.send("<a href='/login'>Log in</a> as admin if you want the flag.");
    } else res.send(env.FLAG);
});
```
The **`const username = req.cookies.user; if (!username || username !== "admin")`** part is noteworthy. From here, we can see that if the value of the cookie named `username` is `admin`, the authentication is successful.

### Authentication breakthrough
Any method is acceptable as long as you can create a cookie with the content `username=admin`, but this time we will introduce the easiest method **using browser DevTools**.

#### DevTools
DevTools is a tool used for testing, editing, and debugging websites that comes standard with most browsers.

You can also change the value of the cookie in DevTools. Go to `Application -> Cookies -> {URL}`, enter `user` for `Name` and `admin` for `Value`, create the cookie and reload it, and you will get the flag.
```
pascalCTF{********************}
```

## 日本語版
### ソースの解析
今回はホワイトボックスでの問題だ。`challenge.zip`を展開し、ソースコードである`server.js`を確認すると、興味深い文が見つかった。
```javascript
app.get("/me", (req, res) => {
    const username = req.cookies.user;
    if (!username || username !== "admin") {
        res.send("<a href='/login'>Log in</a> as admin if you want the flag.");
    } else res.send(env.FLAG);
});
```
注目すべきは **`const username = req.cookies.user; if (!username || username !== "admin")`** の部分だ。ここから、`username`というCookieの値が`admin`であれば認証成功となることがわかる。

### 認証突破
`username=admin`という内容のCookieを作成できればどんな手法でもいいが、今回は一番手軽にできる**ブラウザのDevToolsを使った方法**を紹介する。

#### DevTools
DevToolsは、ほとんどのブラウザに標準でついているWebサイトのテスト・編集・デバッグに使われるツールだ。「開発者ツール」(Google Chrome)や「デベロッパーツール」(Microsoft Edge)といった名前なら、もしかしたら聞き覚えがあるかもしれない。

本題に戻るが、DevToolsではCookieの値を変更することもできる。`Application -> Cookies -> {URL}`で、`Name`に`user`と、`Value`が`admin`と入力してCookieを作成し再読み込みすると、フラグがが手に入るだろう。
```
pascalCTF{********************}
```