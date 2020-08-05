import math

def GetGCD(a1,a2):
    temp = int(a1 / a2)
    modu = int(a1 % a2)
    while (a1 == a2 * temp + modu) and modu != 0:
        print(str(a1) + '==' + str(a2) + "*" + str(temp) + "+" + str(modu))
        return GetGCD(a2,modu)
    print(int(a1 / temp))


print("[*]Input angka untuk dicari fpbnya(a1 > a2):")
a1 = int(input())
a2 = int(input())
if a1 > a2:
    GetGCD(a1,a2)
else:
    print("[!]a1 > a2n\nExiting...")