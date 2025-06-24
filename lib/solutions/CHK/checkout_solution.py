
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        basket = skus.split
        Acount = 0
        Bcount = 0
        sum = 0
        for i in range(basket):
            if basket[i] == "A":
                Acount += 1
            elif basket[i] == "B":
                Bcount += 1
            elif basket[i] == "C":
                sum += 20
            elif basket[i] == "D":
                sum += 15
            else:
                return -1
        Amult = Acount//3
        Asurp = Acount%3
        Bmult = Bcount//2
        Bsurp = Bcount%2
        specials_sum = (Amult*130) + (Asurp*50) + (Bmult*45) + (Bsurp*30)
        return specials_sum+sum
        
        
            





