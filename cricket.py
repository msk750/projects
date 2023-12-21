overs=5
over1=[]
over2=[]
over3=[]
over4=[]
over5=[]
numballs=6
def wickets():
    while True:
        wickets_t=int(input("how many wickets were taken"))
        if wickets_t>10:
            print("Cant be possible")
            continue
        return wickets_t
def score(n,overno):
    for i in range(numballs):
        x=i+1
        print(f"Enter the runs scored on ball number {x}")
        runs=int(input())
        overno.append(runs)
    over_total=sum(overno)
    print(f"Score in over number {n}: {overno} runs scored:{over_total}")
        
score(1,over1)
score(2,over2)
score(3,over3)
score(4,over4)
score(5,over5)
totalr=sum(over1)+sum(over2)+sum(over3)+sum(over4)+sum(over5)
print(totalr)
print(f"Over1:{over1}")
print(f"Over2:{over2}")
print(f"Over3:{over3}")
print(f"Over 4:{over4}")
print(f"Over 5:{over5}")
wicketst=wickets()
def average():
    average_r=totalr/wicketst
    return average_r
as=average()
print(f"Average score was {as}")
    
        
a=int(input("a?"))
b=int(input("b?"))
c=int(input("c?"))
squarecalc(a,b,c)