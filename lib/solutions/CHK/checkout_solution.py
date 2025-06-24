
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
            total += (basketA//5)*200
            basketA %= 5
            total += (basketA//3)*130 
            basketA %= 3
            total += basketA* prices['A']
        if 'B' in basket:
            total += (basket['B']//2)*45 + (basket['B']%2)* prices['B']
        for item in ['C', 'D', 'E']:
            if item in basket:
                total += basket[item] * prices[item]
        return total
        
        
        
        
            



