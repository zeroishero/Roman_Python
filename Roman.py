class CharCalc():
    def __init__(self,n):
        self.n=n
        t=int(n)
        if t >= 0 and t <= 3:
            self.char='I'
            self.val=1
        elif t >= 4 and t <= 8:
            self.char='V'
            self.val=5
        elif t >= 9 and t <= 39:
            self.char='X'
            self.val=10
        elif t >= 40 and t <= 89:
            self.char='L'
            self.val=50
        elif t >=90 and t <= 399:
            self.char='C'
            self.val=100
        elif t >= 400 and t <= 899:
            self.char='D'
            self.val=500
      #elif t >=900: 
                
        else:
            self.char=''
            self.val=0
                        
        if self.char=='V' or self.char=='X':
            self.sub='I'
            self.subn=1
        elif self.char=='L' or self.char=='C':
            self.sub='X'
            self.subn=10
        elif self.char=='D' or self.char=='M':
            self.sub='C'
            self.subn=100
        else:
            self.sub=''
            self.subn=0
def calc(n):
    lit=CharCalc(n)
    if int(n)==0:
        return ""
    else:
        if int(n)>=lit.val:
            return lit.char + calc(int(n)-lit.val)
        else:
            return lit.sub + lit.char + calc(int(n)-lit.val+lit.subn)
            
print(calc(input()))


