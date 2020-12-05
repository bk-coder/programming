a,b,c = input().split()
if a>b:
    if a>c:
        print("meximum=",a)
    else:
        print("meximum=",c)
elif b>c:
    print("meximum=",b)
else:
    print("meximum=",c)