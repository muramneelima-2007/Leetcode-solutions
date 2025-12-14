class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ops=operations.copy()
        li=[]
        l=len(ops)
        for i in range(l):
            if(ops[i]=='+'):
                s=li[-1]+li[-2]
                li.append(s)
            elif(ops[i]=='D'):
                s=(li[-1])*2
                li.append(s)
            elif(ops[i]=='C'):
                li.pop()
            else:
                li.append(int(ops[i]))
        return sum(li)
        