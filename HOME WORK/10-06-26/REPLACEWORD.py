str="python_programming"
print("This is old string :",str)
char1="o"
char2="x"
store=""

for ch in str:
    if ch == char1:
        store += char2
    else:
        store += ch
print("After replacing word string :",store)
