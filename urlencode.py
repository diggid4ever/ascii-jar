from sys import prefix

filename = "eviljsp-jar/646-behinder1.jar"

with open(filename, "rb") as f:
    data = f.read()

prefix = b"DIRTY DATA AT THE BEGINNING "
suffix = b" DIRTY DATA AT THE END"

data = data.replace(prefix, b"").replace(suffix, b"")
res = ""
tmp = ""
for d in data:
    res += "%"
    tmp = hex(d)[2:]
    if len(tmp) == 1:
        res += "0"
    res += tmp

with open("data.txt", "w") as f:
    f.write(res)