n=int(input())
c=n
s=0
r=0
while(n>0):
    r=n%10
    s=(s*10)+r
    n=n//10
if(c==s):
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")
    
