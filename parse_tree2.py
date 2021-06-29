# Reference: 7.6 Parse Tree (Pythonds)
#            https://runestone.academy/runestone/books/published/pythonds/Trees/ParseTree.html
# 
# Input:    mathematical expression in type string; 
#           with operators and functions expressed in corresponding notations 
#           (see page bottom)
# Output:   type float


import numpy as np
import math
import time

class Node2:
    def __init__(self, c):
        self.content = c
        self.parent  = None
        self.r_child = None
        self.l_child = None

class ParseTree2:
    def __init__(self, a):
        self.angle = a
        self.nums = "0123456789."
        self.codes = "ab"
        self.funcs = "cdefghijklmnop"
        self.ops = {'(':-1, '+':2, '-':2, '*':3, '/':3, '^':4, 'c':5, 'd':5,\
                    'e': 5, 'f':5, 'g':5, 'h':5, 'i':5, 'j':5, 'k':5, 'l':5,\
                    'm': 5, 'n':5, 'o':5, 'p':5, 'q':5, 'r':5}
        self.root = Node2(None)


    def toNum(self, char):
        if(char == 'a'):    # pi
            return float(np.pi)
        if(char == 'b'):    # e
            return float(np.exp(1))


    def buildTree(self, expr):
        
        self.root.l_child = Node2(None)   # start from left child of root
        self.root.l_child.parent = self.root
        current = self.root.l_child
        
        i = 0
        was_index = False
        first_index = None
        while i < len(expr):
            char = expr[i]  
   
            if(char in self.nums):
                temp = ""
                while(i < len(expr) and expr[i] in self.nums):
                    temp += str(expr[i])
                    i += 1
                i = i-1
                current.content = float(temp)
                current = current.parent
        
            elif(char in self.codes):
                current.content = self.toNum(char)
                current = current.parent

            elif(char == '('):
                current.l_child = Node2(None)
                current.l_child.parent = current
                current = current.l_child

            elif(char == ')'):
                current = current.parent

            elif(char in self.funcs):
                current.content = char

            elif(char in self.ops):       
                
                if(char != '^' and was_index):
                    was_index = False   
                    current = self.root
                    #if(first_index == None):
                    #    print("is none!")

                if(current.content):    # current node not empty
                    new_node = Node2(char)
                    # current node has lower precedence -> new node is child of current node
                    if(self.ops.get(char) > self.ops.get(current.content)\
                    or char == '^'):  
                        #print(char,"takes path Down") 
                        new_node.l_child, current.r_child.parent = current.r_child, new_node
                        current.r_child, new_node.parent = new_node, current
                    # current node has higher precedence -> new node is parent of current node
                    else:
                        #print(char,"takes path Up")
                        if(current.parent != None):
                            new_node.parent = current.parent
                            if(current.parent.l_child == current):
                               current.parent.l_child = new_node
                            else:
                                current.parent.r_child = new_node
                        else:
                            self.root = new_node
                        new_node.l_child, current.parent = current, new_node   
                    current = new_node

                else:                    # current node is empty -> fill in operand
                    current.content = char
            
                if(char == '^'):
                    was_index = True
                    
                current.r_child = Node2(None)
                current.r_child.parent = current
                current = current.r_child
 
            i+=1

        if(self.root.content == None):
            self.root.content = 'r'

    
    def eval(self, node):
        cmd = node.content
        #print(cmd)

        if(type(cmd) == float):
            return cmd

        if(cmd == '+'):
            return self.eval(node.l_child) + self.eval(node.r_child)

        if(cmd == '-'):
            return self.eval(node.l_child) - self.eval(node.r_child) 
         
        if(cmd == '*'):
            return self.eval(node.l_child) * self.eval(node.r_child)

        if(cmd == '/'):
            return self.eval(node.l_child) / self.eval(node.r_child)
        
        if(cmd == '^'):
            return self.eval(node.l_child) ** self.eval(node.r_child)

        if(cmd == 'c'):    # sin(x)
            if(self.angle):
                return np.sin(self.eval(node.l_child)*np.pi/180)
            return np.sin(self.eval(node.l_child))

        if(cmd == 'd'):    # cos(x)
            if(self.angle):
                return np.cos(self.eval(node.l_child)*np.pi/180)
            return np.cos(self.eval(node.l_child))

        if(cmd == 'e'):    # tan(x)
            if(self.angle):
                return np.tan(self.eval(node.l_child)*np.pi/180)
            return np.tan(self.eval(node.l_child))

        if(cmd == 'f'):    # arcsin(x)
            if(self.angle):
                return np.arcsin(self.eval(node.l_child))/np.pi*180
            return np.arcsin(self.eval(node.l_child))

        if(cmd == 'g'):    # arccos(x)
            if(self.angle):
                return np.arccos(self.eval(node.l_child))/np.pi*180
            return np.arccos(self.eval(node.l_child))

        if(cmd == 'h'):    # arctan(x)
            if(self.angle):
                return np.arctan(self.eval(node.l_child))/np.pi*180
            return np.arctan(self.eval(node.l_child))

        if(cmd == 'i'):    # square(x)
            return pow(self.eval(node.l_child),2)

        if(cmd == 'j'):    # cube(x)
            return pow(self.eval(node.l_child),3)

        if(cmd == 'k'):    # exp(x)
            return np.exp(self.eval(node.l_child))

        if(cmd == 'l'):    # square_root(x)
            return pow(self.eval(node.l_child),(1/2))

        if(cmd == 'm'):    # cubic_root(x)
            return pow(self.eval(node.l_child),(1/3))

        if(cmd == 'n'):    # log(x)
            return np.log10(self.eval(node.l_child))

        if(cmd == 'o'):    # ln(x)
            return np.log(self.eval(node.l_child))

        if(cmd == 'p'):    # abs(x)
            return abs(self.eval(node.l_child))

        if(cmd == 'q'):    # factorial(x)
            return math.factorial(int(abs(self.eval(node.l_child))))
    
        if(cmd == 'r'):    # for void root
            return self.eval(node.l_child)
        

    def output(self):
        return self.eval(self.root)
        
class Calculator2:
    def __init__(self):
        self.rnd_to = 10
        self.angle  = True

    def changeRnd(self, rnd):        # round to decimal points
        self.rnd_to = abs(int(rnd))        

    def changeAngle(self):     # evaluate angle in degrees/radius
        self.angle = not self.angle

    def calculate(self, expr):
        tree = ParseTree2(self.angle)
        tree.buildTree(expr)
        return round(tree.output(), self.rnd_to)

if __name__  == "__main__":
    test = Calculator2()
    expr = "c(60)*e(45)/0.2+i(4)*1.5-k(0.3)"

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
#   r(): special function for void root
#   +:   addition
#   -:   subtraction
#   *:   multiplication
#   /:   division
#   ^:   power
#   .:   decimal point
