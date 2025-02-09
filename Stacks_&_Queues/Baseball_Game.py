class Solution(object):
    def calPoints(self, operations):
        lis=[]
        p1= 0
        p2= 0

        for i in range(len(operations)):
            
            if "-" in operations[i] or operations[i].isnumeric():
                lis.append(int(operations[i]))

            if operations[i]  == "+":
                lis.append(lis[p1] + lis[p2])
            
            if operations[i] == "C":
                lis.remove(lis[p1])
            
            if operations[i] == "D":
                lis.append(lis[p1] * 2)
              
            if len(lis) > 0:
                p1 = len(lis) - 1 
            if len(lis) > 1:
                p2 = len(lis) - 2 


        return sum(lis)