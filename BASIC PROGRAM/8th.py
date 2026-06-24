unit=int(input("Enter the Units : "))

if(unit>0 and unit<=100):
    bill=unit*5
elif(unit>=101 and unit<=200):
    bill=unit*7
elif(unit>=200):
    bill=unit*10
else:
    print("invalid")

gst=bill*0.18
total=bill+gst

print("Bill Ammount : ",bill)
print("GST:",gst)
print("your electricity bill :",total)