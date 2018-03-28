print("--------------Welcome To Kayles Game------------")
FirstP= str(input("Enter First Player Name : "))
SecondP=str(input("Enter Second Player Name : "))
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
    if TurnCounter%2!=0:
        if MainList==["--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--","--"]:
            break
        print(SecondP+"'s","turn")
        x=int(input("Choose a number : "))
        while MainList[x-1]=="--" or x==0:
            print("you can't use this number")
            x=int(input("Choose another number : "))
        y=int(input("Choose adjacent number or enter -1 to skip : "))
        while y !=(x+1) and y !=(x-1) and y != -1 :
            print("you can't use this number")
            y=int(input("Choose another adjacent number or -1 to skip : "))
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
    print(SecondP,"is the winner")
elif TurnCounter%2!=0:
    print(FirstP,"is the winner")
        
        
    






