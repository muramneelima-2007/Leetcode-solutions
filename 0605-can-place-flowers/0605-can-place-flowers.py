class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        l=len(flowerbed)
        if(n==0):
            return True
        if(l==1):
            if(flowerbed[0]==0 and n==1):
                return True 
            return False
        for i in range(l):
            if(i==0):
                if(flowerbed[i]==0 and flowerbed[i+1]==0):
                    flowerbed[i]=1
                    n=n-1
            elif(i==l-1):
                if(flowerbed[i]==0 and flowerbed[i-1]==0):
                    flowerbed[i]=1
                    n=n-1
            else:
                if(flowerbed[i]==0 and flowerbed[i-1]==0 and flowerbed[i+1]==0):
                    flowerbed[i]=1
                    n=n-1 
            if(n<=0):
                return True 
        return False
            
        