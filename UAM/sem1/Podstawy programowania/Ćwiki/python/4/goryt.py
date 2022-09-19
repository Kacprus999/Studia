n=int(input())
i=1
najwyzsze=[]
while(i<=n):
    szczyty=input()
    max=0
    for part in szczyty.split():
        part=int(part)
        if part>max:
            max=part
    najwyzsze.append(max)
    i=i+1
for s in range(len(najwyzsze)):
    print (najwyzsze[s])   
