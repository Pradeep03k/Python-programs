userpass=input("enter Your password : ")


if len(userpass)>=3 and len(userpass)<=6:
    print("weak password")
elif len(userpass)>=6 and len(userpass)<=8:
    print("strong password")
elif len(userpass)>=8 and len(userpass)<20:
    print("very strong password")
else: 
    print("invlaid format")