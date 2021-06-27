# Reference: Shunting-yard Algorithm (Wikipedia) 
#            https://en.wikipedia.org/wiki/Shunting-yard_algorithm
# 
# Input:    expression in type string; 
#           with operators and functions expressed in corresponding notations 
#           (see page bottom)
# Output:   type float
# ToDo:     1. complex numbers
#           2. checking for errors

import numpy as np
import math  

class Calculator:

    def __init__(self):
        self.rnd_to = 10            # decimal points to round to
        self.angle = True           # True for Degrees, False for Radius

        self.nums = "0123456789."
        self.codes = "ab"
        self.funcs = "cdefghijklmnop"
        self.ops = {'(':-1, '+':2, '-':2, '*':3, '/':3, '^':4, 'c':5, 'd':5,\
                    'e': 5, 'f':5, 'g':5, 'h':5, 'i':5, 'j':5, 'k':5, 'l':5,\
                    'm': 5, 'n':5, 'o':5, 'p':5, 'q':5, 'r':5, 's':5 }
        # self.ops: operands/functions to corresponding precedence


    def changeRnd(self, rnd):        # round to decimal points
        self.rnd_to = abs(int(rnd))        


    def changeAngle(self):     # evaluate angle in degrees/radius
        self.angle = not self.angle   

    
    def toNum(self, char):
        if(char == 'a'):
            return np.pi
        if(char == 'b'):
            return np.exp(1)
    

    def genRP(self, expr):  # converts inflix to reverse polish
        rp_stack = []       # stack
        operators = []      # queue 

        i = 0
        while(i < len(expr)):         # shunting yard algorithm

            char = expr[i]
            if(char in self.codes):   
                rp_stack.append(self.toNum(char))
                
            elif(char in self.nums): 
                temp = ""
                while(i < len(expr) and expr[i] in self.nums):
                    temp += str(expr[i])
                    i += 1
                i = i-1
                rp_stack.append(float(temp))

            elif(char == '('):      
                operators.append(char)

            elif(char in self.ops): 
                # '^' is exception for it is evaluated from right to left
                while(operators and self.ops.get(char) <= self.ops.get(operators[-1])\
                and (char != '^' or operators[-1] != '^')): 
                    rp_stack.append(operators[-1])
                    operators.pop()
                operators.append(char)

            elif(char == ')'):   
                while(operators[-1] != '('):
                    rp_stack.append(operators[-1])
                    operators.pop()
                operators.pop()

            i += 1
            #for j in rp_stack+operators[::-1]:
            #    print(j, end = " ")
            #print()

        return rp_stack + operators[::-1]

    
    def funcOp(self, x, func):      # functions
        if(func == 'c'):    # sin(x)
            if(self.angle):
                return np.sin(x*np.pi/180)
            return np.sin(x)

        if(func == 'd'):    # cos(x)
            if(self.angle):
                return np.cos(x*np.pi/180)
            return np.cos(x)

        if(func == 'e'):    # tan(x)
            if(self.angle):
                return np.tan(x*np.pi/180)
            return np.tan(x)

        if(func == 'f'):    # arcsin(x)
            if(self.angle):
                return np.arcsin(x)/np.pi*180
            return np.arcsin(x)

        if(func == 'g'):    # arccos(x)
            if(self.angle):
                return np.arccos(x)/np.pi*180
            return np.arccos(x)

        if(func == 'h'):    # arctan(x)
            if(self.angle):
                return np.arctan(x)/np.pi*180
            return np.arctan(x)

        if(func == 'i'):    # square(x)
            return pow(x,2)

        if(func == 'j'):    # cube(x)
            return pow(x,3)

        if(func == 'k'):    # exp(x)
            return np.exp(x)

        if(func == 'l'):    # square_root(x)
            return pow(x,(1/2))

        if(func == 'm'):    # cubic_root(x)
            return pow(x,(1/3))

        if(func == 'n'):    # log(x)
            return np.log10(x)

        if(func == 'o'):    # ln(x)
            return np.log(x)

        if(func == 'p'):    # abs(x)
            return abs(x)

        if(func == 'q'):    # factorial(x)
            return math.factorial(int(abs(x)))
        
        if(func == 'r'):    # deg(x)
            if(self.angle):
                return x/np.pi*180
            return x
    
        if(func == 's'):    # rad(x)
            if(self.angle):
                return x
            return x/180*np.pi

    def operate(self, x, y, op):    # operand calculation
        if(op == '+'):
            return x + y
        if(op == '-'):
            return x - y
        if(op == '*'):
            return x * y
        if(op == '/'):
            return x / y
        if(op == '^'):
            return pow(x,y)
    

    def findVal(self, rp): # derive output from rp stack
        numStack = []
        for i in rp:
            temp = None
            if(type(i) == float): 
                temp = i
            elif(ascii(i) >= ascii('c') and ascii(i) <= ascii('s')):
                temp = self.funcOp(numStack[-1], i)
                numStack.pop()
            elif(type(i) == str):
                temp = self.operate(numStack[-2], numStack[-1], i)
                numStack.pop()  
                numStack.pop()
            #print(temp)
            numStack.append(temp)

        return round(numStack[0], self.rnd_to)

    def calculate(self, expr):
        return self.findVal( self.genRP(expr) )
         

if __name__ == "__main__":
    test = Calculator()
    expr = "12+4-c(21)^(0.5-1)+o(j(24.1/42)+f(0.24))"
    print(expr,'=')
    print(test.calculate(expr))

    test.changeRnd(4)
    print(expr,'=')
    print(test.calculate(expr))
    
    print()
    print(test.calculate("c(45)+d(60)"))
    print(test.calculate("c(45)+d(r(a/3))"))
    test.changeAngle()
    print(test.calculate("c(a/4)+d(a/3)"))
    print(test.calculate("c(a/4)+d(s(60))"))

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
#   r(): deg()
#   s(): rad()
#   +:   addition
#   -:   subtraction
#   *:   multiplication
#   /:   division
#   ^:   power
#   .:   decimal point