
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        prices = {'A': 50, 'B': 30, 'C':20, 'D':15, 'E':40}
        basket = {}
        for item in skus:
            if item not in prices:
                return -1
            basket[item] = basket.get(item, 0)+1
        total = 0
        if 'E' in basket and 'B' in basket:
            freeB = min(basket['E'] // 2, basket['B'])
            basket['B'] -= freeB
        if 'A' in basket:
            basketA = basket['A']
            total += (basket['A']//5)*200
            basketA %= 5
            total += (basket['A']//3)*130 
            basketA %= 3
            total += basket['A']* prices['A']
        if 'B' in basket:
            total += (basket['B']//2)*45 + (basket['B']%2)* prices['B']
        if 'C' in basket:
            total += basket['C'] * prices['C']
        if 'D' in basket:
            total += basket['D'] * prices['D']
        if 'E' in basket:
            totalk += basket['E'] * prices['E']
        return total
        
        
        
        
            

