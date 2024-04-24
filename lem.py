n=int(input("enter of lemons:"))
s=n-21
r=21-n
print("{} more lemons".format(s) if n>21 else "sufficient lemons" if n==21 else "{} less lemons".format(r))