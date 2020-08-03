class Solution(object):
    def numWaterBottles(self,numBottles,numEx):
            numBottles = int(numBottles)
            numEx = int(numEx)

            left = 0
            sum = numBottles
            exchange = (numBottles) // (numEx)
            left = (numBottles) % (numEx)
            sum = sum+exchange
            while exchange > 0 :
                sumOfLeft = exchange + left
                exchange = sumOfLeft//(numEx)
                left = sumOfLeft%(numEx)
                sum = sum + exchange
                
            return sum
           
bottleNums = input("How many water you drank? ")
exchangeNums = input ("How many bottles you can exchange for 1 full bottle? ")
solution = Solution()
print (str(solution.numWaterBottles(bottleNums, exchangeNums)))
            

                

                

                

            
            
          
            
