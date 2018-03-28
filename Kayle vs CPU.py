import random
print("--------------Welcome To Kayles Game------------")
FirstP= str(input("Enter First Player Name : "))
MainList= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
TurnCounter=0
print(MainList)
while MainList != ["--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--"]:
    if TurnCounter%2==0:
        print(FirstP+"'s","turn")
        x=int(input("Choose a number : "))
        while MainList[x-1]=="--" or x==0:
            print("you can't use this number")
            x=int(input("Choose another number : "))
        y=int(input("Choose adjacent number or enter -1 to skip : "))
        while y !=(x+1) and y !=(x-1) and y != -1 :
            print("you can't use this number")
            y=int(input("Choose another adjacent number or -1 to skip : "))
        if y == -1:
            MainList[x-1]="--"
            print(MainList)
            TurnCounter+=1
        elif y != -1:
            MainList[x-1]="--"
            MainList[y-1]="--"
            print(MainList)
            TurnCounter+=1
    else:
        if MainList==["--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--"]:
            break
        print("CPU's turn")
        x=random.randint(1,20)
        while MainList[x-1]=="--" or x==0:
            x=random.randint(1,20)
        if x == 1:
            a=[-1,2]
        elif x== 20:
            a=[-1,19]
        else:
            a=[x-1,x+1,-1]
        y=a[random.randint(0,len(a)-1)]
        while y !=(x+1) and y !=(x-1) and y != -1 :
            a.remove(y)
            y=a[random.randint(0,len(a)-1)]
        if y == -1 :
            MainList[x-1]="--"
            print(MainList)
            TurnCounter+=1
        elif y != -1:
            MainList[x-1]="--"
            MainList[y-1]="--"
            print(MainList)
            TurnCounter+=1
if TurnCounter%2==0:
    print("CPU is the winner")
elif TurnCounter%2!=0:
    print(FirstP,"is the winner")
