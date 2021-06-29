# Input:    mathematical expression in type string; 
#           with operators and functions expressed in corresponding notations 
#           (see page bottom)
# Output:   type float


import numpy as np
import math
import time

class Node1:
    def __init__(self, c):
        self.content = c
        self.parent  = None
        self.r_child = None
        self.l_child = None

class ParseTree1:
    def __init__(self, a):
        self.angle = a
        self.nums = "0123456789."
        self.codes = "ab"
        self.funcs = "cdefghijklmnop"
        self.ops = {'(':-1, '+':5, '-':5, '*':4, '/':4, '^':3, 'c':2, 'd':2,\
                    'e': 2, 'f':2, 'g':2, 'h':2, 'i':2, 'j':2, 'k':2, 'l':2,\
                    'm': 2, 'n':2, 'o':2, 'p':2, 'q':2, 'r':2, 's':2 }
        self.root = Node1(None)
    
    
    def toNum(self, char):
        if(char == 'a'):    # pi
            return float(np.pi)
        if(char == 'b'):    # e
            return float(np.exp(1))


    def rank(self,expr):
        rk = []
        in_par = 0
        new_expr = []
        i = 0

        while i < len(expr):
            char = expr[i]
            if(char == '('):
                in_par += 1               

            elif(char == ')'):
                in_par -= 1
    
            elif(char in self.codes):
                rk.append(-10000000000000)
                new_expr.append(self.toNum(char))
            
            elif(char in self.nums):
                temp = ""
                while(i < len(expr) and expr[i] in self.nums):
                    temp += expr[i]
                    i += 1
                i -= 1
                
                rk.append(-10000000000000)
                new_expr.append(float(temp))
                
            elif(char in self.ops):
                rk.append(-in_par*6 + self.ops.get(char))
                new_expr.append(char)
            i += 1

        return rk, new_expr  

    def split(self, node, expr, rk):

        max = 0
        for i in range(len(expr)):
            if(rk[i] > rk[max]):
                max = i
    
        if(i == 3):
            for i in range(len(expr)-1, -1):
                if(rk[i] >= rk[max]):
                    max = i
        
        node.content = expr[max]
        node.r_child, node.l_child = Node1(None), Node1(None)
        node.r_child.parent, node.l_child.parent = node, node
        
        if(expr[:max]):
            self.split(node.l_child, expr[:max],   rk[:max])
        if(expr[max+1:]):
            self.split(node.r_child, expr[max+1:], rk[max+1:])

    def merge(self, node):
   
        if(node.content == '+'):
            return self.merge(node.r_child) + self.merge(node.l_child)

        if(node.content == '-'):
            return self.merge(node.r_child) - self.merge(node.l_child)

        if(node.content == '*'):
            return self.merge(node.r_child) * self.merge(node.l_child)

        if(node.content == '/'):
            return self.merge(node.r_child) / self.merge(node.l_child)

        if(node.content == '^'):
            return pow(self.merge(node.r_child), self.merge(node.l_child))
        
        if(node.content == 'c'):    # sin(x)
            if(self.angle):
                return np.sin(self.merge(node.l_child)*np.pi/180)
            return np.sin(self.merge(node.l_child))

        if(node.content == 'd'):    # cos(x)
            if(self.angle):
                return np.cos(self.merge(node.l_child)*np.pi/180)
            return np.cos(self.merge(node.l_child))

        if(node.content == 'e'):    # tan(x)
            if(self.angle):
                return np.tan(self.merge(node.l_child)*np.pi/180)
            return np.tan(self.merge(node.l_child))

        if(node.content == 'f'):    # arcsin(x)
            if(self.angle):
                return np.arcsin(self.merge(node.l_child))/np.pi*180
            return np.arcsin(self.merge(node.l_child))

        if(node.content == 'g'):    # arccos(x)
            if(self.angle):
                return np.arccos(self.merge(node.l_child))/np.pi*180
            return np.arccos(self.merge(node.l_child))

        if(node.content == 'h'):    # arctan(x)
            if(self.angle):
                return np.arctan(self.merge(node.l_child))/np.pi*180
            return np.arctan(self.merge(node.l_child))

        if(node.content == 'i'):    # square(x)
            return pow(self.merge(node.l_child),2)

        if(node.content == 'j'):    # cube(x)
            return pow(self.merge(node.l_child),3)

        if(node.content == 'k'):    # exp(x)
            return np.exp(self.merge(node.l_child))

        if(node.content == 'l'):    # square_root(x)
            return pow(self.merge(node.l_child),(1/2))

        if(node.content == 'm'):    # cubic_root(x)
            return pow(self.merge(node.l_child),(1/3))

        if(node.content == 'n'):    # log(x)
            return np.log10(self.merge(node.l_child))

        if(node.content == 'o'):    # ln(x)
            return np.log(self.merge(node.l_child))

        if(node.content == 'p'):    # abs(x)
            return abs(self.merge(node.l_child))

        if(node.content == 'q'):    # factorial(x)
            return math.factorial(int(abs(self.merge(node.l_child))))
        
        else:
            return node.content


    def output(self,expr):
        ranking, expr = self.rank(expr)
        self.split(self.root, expr[::-1], ranking[::-1])
        return self.merge(self.root)
        

class Calculator1:
    def __init__(self):
        self.rnd_to = 10
        self.angle = True 
    
    def changeRnd(self, rnd):        # round to decimal points
        self.rnd_to = abs(int(rnd))        

    def changeAngle(self):     # evaluate angle in degrees/radius
        self.angle = not self.angle

    def calculate(self,expr):
        tree = ParseTree1(self.angle)
        return round(tree.output(expr), self.rnd_to)
        

if __name__ == "__main__":
    test = Calculator1()
    #expr = "c(60)*e(45)/0.2+i(4)*1.5-k(0.3)"
    expr = "2^3^2"

    t1 = time.time()
    ans = test.calculate(expr)
    t2 = time.time()
    print(ans)
    print("time:",t2-t1)
    
# function/operator:notation
#   a:   pi
#   b:   e
#   c(): sin()
#   d(): cos()
#   e(): tan()
#   f(): arcsin()
#   g(): arccos()
#   h(): arctan()
#   i(): square()
#   j(): cube()
#   k(): exp()
#   l(): square_root()
#   m(): cubic_root()
#   n(): log()
#   o(): ln()
#   p(): abs()
#   q(): factorial()
#   +:   addition
#   -:   subtraction
#   *:   multiplication
#   /:   division
#   ^:   power
#   .:   decimal point