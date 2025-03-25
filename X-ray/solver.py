key = [ord(i) for i in list("*7^tVr4FZ#7S4RFNd2")]
encrypted = [ord(i) for i in list("xR\bG$G\a\031kPhgCa5~\t\001")]

print(''.join([chr(k ^ c) for k, c in zip(key, encrypted)]))