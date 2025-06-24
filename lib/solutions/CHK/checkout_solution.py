
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        prices = {'A': 50, 'B': 30, 'C':20, 'D':15}
        basket = {}
        for item in skus:
            if item not in prices:
                return -1
            basket[item] = basket.get(item, 0)+1
        total = 0
        if 'A' in basket:
            total += (basket['A']//3)*130 + (basket['A']%3)* prices['A']
        if 'B' in basket:
            total += (basket['B']//2)*45 + (basket['B']%2)* prices['B']
        if 'C' in basket:
            total += basket['C'] * prices['C']
        if 'D' in basket:
            total += basket['D'] * prices['D']
        return total
        
        
        
        
            
