#for eg i used "and"
input=[[1,1,1],[1,0,1],[0,1,1],[0,0,1]]
#the targets are defined bipolar
target=[1,-1,-1,-1]
#you can change thies parameters(line 6-8)
teta=0.5
alpha=1
lastweight=[0,0,0]
#
weight=[[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
temp=0
epoch=0
flag=True
#the main algorithm
while (flag):
    epoch+=1
    weight=[[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
    yin=[]
    out=[]
    for x in range(0,4):    
        temp=lastweight[2]+((input[x][0]*lastweight[0])+(input[x][1]*lastweight[1]))
        yin.append(temp)
        if yin[x] > teta :
            out.append(1)
        elif yin[x]==0:
                out.append(0)
        else :
            out.append(-1)
        if target[x] != out[x] :
            weight[x][0]=lastweight[0]+(alpha*input[x][0]*target[x])
            weight[x][1]=lastweight[1]+(alpha*input[x][1]*target[x])
            weight[x][2]=lastweight[2]+(alpha*target[x])
        else:
            weight[x][0]=lastweight[0]
            weight[x][1]=lastweight[1]
            weight[x][2]=lastweight[2]
        lastweight[0]=weight[x][0]
        lastweight[1]=weight[x][1]
        lastweight[2]=weight[x][2]
    print("\nepoch ",epoch,"\n")
    print("input\t\tnet\tout\ttarget\t  weight")
    for x in range(0,4):
        print(input[x],"\t",yin[x],"\t",out[x],"\t",target[x],"\t",weight[x])
    if weight[0]==weight[1] and weight[1]==weight[2] and weight[3]==weight[2] and target==out:
        flag=False
    
#developed by amirrezaghc
#hope you enjoyed :)