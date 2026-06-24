# 2nd evenodd char 
x="maharasiehtra"
count=0
for i in x:
    count+=1
print("the main string length :",count)
evenchar=0
oddchar=0
for ch in range(0,count):
    if x[ch]=="a" or x[ch]=="e" or x[ch]=="i" :
        print("vowels : ",x[ch])
    if ch%2==0:
        evenchar+=1
    else:
        oddchar+=1
print("Even char present in string :",evenchar)
print("Odd  char present in string :",oddchar)


