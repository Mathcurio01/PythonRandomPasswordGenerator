import random
alphabet = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
numbers ="0,1,2,3,4,5,6,7,8,9"
symbols ="@,$,%,^,&,*,(),!"
all = alphabet.split(",") + (alphabet.upper()).split(",")+ numbers.split(",")+symbols.split(",")

length = int(input("Enter password length: "))
random.shuffle(all)

password = ""

for i in range(0,length):
    password+=all[i]

print(f"Password is: {password}")