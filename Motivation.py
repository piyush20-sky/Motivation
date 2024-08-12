#The Faster one always thinks they are much ahead and can rest
faster = 365
slower = 0

ct = 7 #Represent Week
while slower != faster:
    ct-=1 
    slower+=1
    if ct>2: #Represent Weekdays
        faster+=1
    if ct==0:
        ct=7

print("Days to catch Up:"+ str(slower) )
print("years to catch up:"+ str(round(slower/365,2)))
