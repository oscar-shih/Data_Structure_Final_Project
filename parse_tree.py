# Input:    mathematical expression in type string; 
#           with operators and functions expressed in corresponding notations 
#           (see page bottom)
# Output:   type float
# ToDo:     1. parse tree traversal (combining nodes)
#           2. calculation for functions and operators
#           2. conditional statement for functions in rank
#           3. decimal numbers



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
        self.ops = {'(':-1, '+':2, '-':2, '*':3, '/':3, '^':4, 'c':5, 'd':5,\
                    'e': 5, 'f':5, 'g':5, 'h':5, 'i':5, 'j':5, 'k':5, 'l':5,\
                    'm': 5, 'n':5, 'o':5, 'p':5, 'q':5, 'r':5, 's':5 }
        self.root = Node1(None)


    def rank(self,expr):
        rk = []
        in_par = 0
        for i in range(len(expr)):
            char = expr[i]
            if(char == '('):
                in_par += 1
                rk.append(-1)                

            elif(char == ')'):
                in_par -= 1
                rk.append(-1)
            
            elif(char in self.nums):
                rk.append(0)
                
            elif(char in self.ops):
                rk.append(in_par*100 + self.ops.get(char))
        print(rk)
        return rk    

    def split(self, node, expr, rk):
        min = 0
        for i in range(len(expr)):
            if(rk[i] < rk[min]):
                min = i

        if(rk[min] < 0):
            return
        
        node.content = rk[min]
        print(node.content)
        node.r_child, node.l_child = Node1(None), Node1(None)
        node.r_child.parent, node.l_child.parent = node, node

        if(expr[:min]):
            self.split(node.r_child, expr[:min],   rk[:min])
        if(expr[min+1:]):
            self.split(node.l_child, expr[min+1:], rk[min+1:])

    def buildTree(self,expr):
        ranking = self.rank(expr)
        split(self, self.root, expr, ranking)
        

class Calculator1:
    def __init__(self):
        self.rnd_to = 10
        self.angle = True 
    
    def changeRnd(self, rnd):        # round to decimal points
        self.rnd_to = abs(int(rnd))        

    def changeAngle(self):     # evaluate angle in degrees/radius
        self.angle = not self.angle
    

if __name__ == "__main__":
    tree = ParseTree1(True)
    expr = "1+2*3"
    tree.split(tree.root, expr, tree.rank(expr))
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