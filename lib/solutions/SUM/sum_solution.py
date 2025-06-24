
class SumSolution:
    
    def compute(self, x, y):
        if(100<x<0 or 100<y<0):
            return "invalid"
        return x+y

def compute(x, y):
    if(100<x<0 or 100<y<0):
        return "invalid"
    return x+y

compute(1+2)
