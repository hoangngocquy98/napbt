a=input("nhap a:").split()
dodai=len(a[0])
chuoi=a[0]
for i in a:
    if len(i)>dodai:
        dodai=len(i)
        chuoi=i
print(chuoi)