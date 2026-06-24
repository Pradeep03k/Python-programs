# 3rd print upper case string 
s = "hello"
result = ""

for ch in s:
    if ord(ch) >= 97 and ord(ch) <= 122:
        result += chr(ord(ch) - 32)
    else:
        result += ch

print(result)