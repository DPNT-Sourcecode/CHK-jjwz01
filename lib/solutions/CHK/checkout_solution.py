
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        prices = {'A': 50, 'B': 30, 'C':20, 'D':15, 'E':40, 'F':10, 'G':20, 'H':10, 'I':35, 'J':60, 'K':80, 'L':90, 'M':15, 'N':40 , 'O':10, 'P':50, 'Q':30, 'R':50, 'S':30, 'T':20, 'U':40, 'V':50, 'W':20, 'X':90 ,'Y':10, 'Z':50}
        basket = {}
        for item in skus:
            if item not in prices:
                return -1
            basket[item] = basket.get(item, 0)+1
        total = 0
        if 'E' in basket and 'B' in basket:
            freeB = min(basket['E'] // 2, basket['B'])
            basket['B'] -= freeB
        if 'N' in basket and 'M' in basket:
            freeM = min(basket['N'] // 3, basket['M'])
            basket['M'] -= freeM
        if 'R' in basket and 'Q' in basket:
            freeQ = min(basket['R'] // 3, basket['Q'])
            basket['Q'] -= freeQ
        if 'F' in basket:
            basketF = basket['F']
            paidF = basketF - (basketF//3)
            total += paidF * prices['F']
        if 'U' in basket:
            basketU = basket['U']
            paidU = basketU - (basketU//4)
            total += paidU * prices['U']
        if 'A' in basket:
            basketA = basket['A']
            total += (basketA//5)*200
            basketA %= 5
            total += (basketA//3)*130 
            basketA %= 3
            total += basketA* prices['A']
        if 'H' in basket:
            basketH = basket['H']
            total += (basketH//10)*80
            basketH %= 10
            total += (basketH//5)*45 
            basketH %= 5
            total += basketH* prices['H']
        if 'V' in basket:
            basketV = basket['V']
            total += (basketV//3)*130
            basketV %= 3
            total += (basketV//2)*90 
            basketV %= 2
            total += basketV* prices['V']
        if 'Q' in basket:
            basketQ = basket['Q']
            total += (basketQ//3)*80
            basketQ %= 3
            total += basketQ* prices['Q']
        if 'P' in basket:
            basketP = basket['P']
            total += (basketP//5)*200
            basketP %= 5
            total += basketP* prices['P']
        if 'K' in basket:
            basketK = basket['K']
            total += (basketK//2)*150
            basketK %= 2
            total += basketK* prices['K']
        if 'B' in basket:
            total += (basket['B']//2)*45 + (basket['B']%2)* prices['B']
        for item in ['C', 'D', 'E', 'G', 'I', 'J', 'L', 'M', 'N', 'O', 'R', 'S', 'T', 'W', 'X', 'Y', 'Z']:
            if item in basket:
                total += basket[item] * prices[item]
        return total
        
        
        
        
            
