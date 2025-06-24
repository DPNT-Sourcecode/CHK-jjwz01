
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        if skus == 0:
            return -1
        sum = 0
        for i in range(skus):
            sum += skus
        return sum
            

