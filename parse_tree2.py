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
import argparse
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
        self.funcs = "cdefghijklmnopq"
        self.ops = {'(':-1, '+':2, '-':2, '*':3, '/':3, '^':4, 'c':5, 'd':5,\
                    'e': 5, 'f':5, 'g':5, 'h':5, 'i':5, 'j':5, 'k':5, 'l':5,\
                    'm': 5, 'n':5, 'o':5, 'p':5, 'q':5 }
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
        
        was_index = False
        count_idx = 0
        par_bound = []

        i = 0
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
                if(current.parent.content):
                    #print("current.parent.content exists")
                    par_bound.append(current.parent)

            elif(char == ')'):
                if(par_bound):
                    par_bound.pop()

            elif(char in self.funcs):
                current.content = char
                current.l_child = Node2(None)
                current.l_child.parent = current
                current = current.l_child

            ## char is operand starts here
            elif(char in self.ops):

                if(char != '^' and was_index):
                    #print(count_idx)
                    #print("current was",current.content)
                    for j in range(count_idx):
                        current = current.parent
                    #print("current is now",current.content)
                    count_idx = 0
                    was_index = False
    

                #if(not current):
                    #print("current is void")    
                
                if(not current.content):
                    #print(char,"filled in")
                    current.content = char
                    current.r_child = Node2(None)
                    current.r_child.parent = current
                    current = current.r_child
                           
                else:
                    if(self.ops.get(char) > self.ops.get(current.content)\
                    or (par_bound and par_bound[-1] == current) or char == '^'):
                        new_node = Node2(char)
                        if(current.r_child):
                            #print(char,"takes path DOWN RIGHT")
                            new_node.l_child = current.r_child
                            new_node.l_child.parent = new_node
                            current.r_child = new_node
                            new_node.parent = current
                            new_node.r_child = Node2(None)
                            new_node.r_child.parent = new_node
                            current = new_node.r_child
                        else:
                            #print(char,"takes path DOWN LEFT")
                            new_node.l_child =  current.l_child
                            new_node.l_child.parent = new_node
                            current.l_child = new_node
                            new_node.parent = current
                            new_node.r_child = Node2(None)
                            new_node.r_child.parent = new_node
                            current = new_node.r_child
                    
                    else:
                        #print(char,current.content,"takes path UP")
                        while(current.parent and current.parent.content and\
                        self.ops.get(char) <= self.ops.get(current.parent.content)\
                        and (not par_bound or current.parent != par_bound[-1])):
                            current = current.parent
                            # current is child of new node

                        new_node = Node2(char)
                        if(current.parent):
                            new_node.parent = current.parent
                            if(current.parent.l_child == current):
                                current.parent.l_child = new_node
                            elif(current.parent.r_child == current):
                                current. parent.r_child  = new_node

                        new_node.l_child = current
                        current.parent = new_node
                        new_node.r_child = Node2(None)
                        new_node.r_child.parent = new_node
                        current = new_node.r_child 
            
                        while(self.root.parent):
                            self.root = self.root.parent

                if(char == '^'):
                    was_index = True
                    count_idx += 1

            ## char is operand ends here
            i+=1

        if(self.root.content == None):
            self.root.content = 'r'

    
    def eval(self, node):
        cmd = node.content
 
        if(type(cmd) == float):
            return cmd
        
        if(cmd in "+-*/^"):
            a = self.eval(node.l_child)
            b = self.eval(node.r_child)
            c = None
            
            if(cmd == '+'):
                c = a + b
            elif(cmd == '-'):
                c = a - b
            elif(cmd == '*'):
                c = a * b
            elif(cmd == '/'):
                c = a / b
            elif(cmd == '^'):
                c = a ** b
            
            #print(c,"=",a,cmd,b)
            return c

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

        if(cmd == 'r'):    # void root
            return self.eval(node.l_child)

    def output(self):
        return self.eval(self.root)
        
class Calculator2:
    def __init__(self):
        self.rnd_to = 3
        self.angle  = True

    def changeRnd(self, rnd):        # round to decimal points
        self.rnd_to = abs(int(rnd))        

    def changeAngle(self):     # evaluate angle in degrees/radius
        self.angle = not self.angle

    def calculate(self, expr):
        tree = ParseTree2(self.angle)
        tree.buildTree(expr)
        return str(round(tree.output(), self.rnd_to))

    def main(self, input_path, output_path):
        output = open(output_path, 'w')
        with open(input_path, 'r') as file_in:
            f = file_in.read().splitlines()
            t1 = time.time()
            for lines in f:
                ans = self.calculate(lines)
                output.write(ans)
                output.write('\n')
            t2 = time.time()
            #print('time:'+str(t2-t1))

if __name__  == "__main__":

    test = Calculator2()
    #expr = "m(11174148)*i(6.666)/p(18^2-3^11)-l(878791)*f(0.123)-g(0-0.4265)-a^a*k(8)-d(138)/h(72)"
    #expr ="m(1)*i(1)"

    #t1 = time.time()
    #ans = test.calculate(expr)
    #t2 = time.time()
    #print(ans)
    #print("time:",t2-t1)

    #parser = argparse.ArgumentParser()
    #parser.add_argument("--input", type=str, default='./correctness/correct_1.txt',help="Input file root")
    #parser.add_argument("--output", type=str, default='./ouput_1.txt', help="Output file root")
    #args = parser.parse_args()
    #Cal = Calculator2()
    #Cal.main(args.input, args.output) 
        

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