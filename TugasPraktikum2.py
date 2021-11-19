A = int(input("Masukkan bilangan A: "))
B = int(input("Masukkan bilangan B: "))
C = int(input("Masukkan bilangan C: "))

if A > B and A > C:
    maks = A;
    print("Bilangan Terbesar adalah: A.",maks);
elif B > C and B > A:
    maks = B;
    print("Bilangan Terbesar adalah: B.",maks);
else:
    maks = C;
    print("Bilangan Terbesar adalah: C.",maks);
