liquidity = {
    ("tokenA", "tokenB"): (17, 10),
    ("tokenA", "tokenC"): (11, 7),
    ("tokenA", "tokenD"): (15, 9),
    ("tokenA", "tokenE"): (21, 5),
    ("tokenB", "tokenC"): (36, 4),
    ("tokenB", "tokenD"): (13, 6),
    ("tokenB", "tokenE"): (25, 3),
    ("tokenC", "tokenD"): (30, 12),
    ("tokenC", "tokenE"): (10, 8),
    ("tokenD", "tokenE"): (60, 25),
}

def calculate(liquidity, token1, token2, curbalance):
    if token1>token2:
        token1,token2=token2,token1
        (reserve2,reserve1)=liquidity[(token1,token2)]
    else:
        (reserve1,reserve2)=liquidity[(token1,token2)]
    return (997*curbalance*reserve2)/(1000*reserve1+997*curbalance)
                
    

def find_arbitrage(liquidity, start_token, current_balance, visit, path):
    visited=visit.copy()
    current_token = start_token
    paths=path[:]
    paths.append(start_token)

    visited[current_token]=1
    
    temp=0
    if current_token!="tokenB":
        temp=calculate(liquidity,current_token,"tokenB",current_balance)
    if temp>20:
        paths.append("tokenB")
        # print(current_balance,temp,paths)
        return paths, temp, 1
        
    for token, vis in visited.items():
        if vis==0:
            tempprofit=calculate(liquidity,current_token,token,current_balance)
            # print(current_balance, tempprofit,paths)
            pp,ff,ok=find_arbitrage(liquidity,token,tempprofit,visited,paths)
            # print(ff,pp)
            if ok==1:
                return pp,ff,ok
    
    return paths, temp, 0
    

visited = {"tokenA":0, "tokenB":0, "tokenC":0, "tokenD":0,"tokenE":0}
pathinit = []

path, final, ok= find_arbitrage(liquidity, "tokenB", 5, visited, pathinit)

if ok==1:
    print("path: ", "->".join(path), ", tokenB balance=", final, sep="")
else:
    print("No profitable arbitrage path found")
# init=5
# for i in range(4):
#     after=calculate(liquidity,path[i],path[i+1],init)
#     print(path[i],"to", path[i+1],", amountIn=",init,", amountOut=",after)
#     init=after