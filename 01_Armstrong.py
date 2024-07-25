n=int(input("Enter the number="))
c=n
s=0
r=0
while n>0:
    r=n%10
    s=s+r**3
    n=n//10
if s==c:
    print("Armstrong Number")
else:
    print("Not a Armstrong Number")
