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
