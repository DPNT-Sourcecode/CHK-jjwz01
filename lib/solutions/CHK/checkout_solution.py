
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        if len.skus == 0:
            return -1
        sum = 0
        for i in range(skus):
            sum += skus[i]
            i+=1
        return sum
            


