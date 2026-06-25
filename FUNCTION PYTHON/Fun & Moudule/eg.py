import math

print(math.sqrt(5))
print(math.factorial(5))
print(math.ceil(45.56))
print(math.floor(47.23))
print(math.pow(2,3)) 
print(math.pi)

cal=2*math.pi*2
print(cal)

# random choices module
# import random 
import random as r
print(r.randint(1000,9999)) #int returen karen
print(r.random()) # float value betn 0.0 to < 1.0
print(r.randrange(2,10,2))



# list ke sath random
x=["red","black","blue","pink"]
print(r.choice(x))
print(r.choices(x,k=2))
r.shuffle(x)
print(x)



# Date & Time module
import datetime
# current time ---->now
d= datetime.datetime.now()
print(d)
print(d.time())
print(d.day)
print(d.month)
print(d.year)


# date ----> 26/06/25
today_date=datetime.date.today()
print(today_date)

# after days
after=today_date+datetime.timedelta(days=5)#timedelta(next day add karne ke liye(year data month time))
print(after)

dob=datetime.date(2000,10,10)
cd=datetime.date.today()
print(cd-dob)

print(cd.year-dob.year)