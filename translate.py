# translates notations used in code to readable ones for verification in google calculator
# Input:  string
# Output: string

def translate(input):
    output = ""
    cube, cbrt = 0, 0 
    cube_par, cbrt_par = [],[]
    # cube: 'j'/cube()
    # cbrt: 'm'/cube_root()

    for char in input:
        if(char == 'a'):      # pi
            output += "pi"

        elif(char == 'b'):
            output += "e"

        elif(char == 'c'):    # sin(x)
            output += "sin"

        elif(char == 'd'):    # cos(x)
            output += "cos"

        elif(char == 'e'):    # tan(x)
            output += "tan"

        elif(char == 'f'):    # arcsin(x)
            output += "arcsin"

        elif(char == 'g'):    # arccos(x)
            output += "arccos"

        elif(char == 'h'):    # arctan(x)
            output += "arctan"

        elif(char == 'i'):    # square(x)
            output += "square"

        elif(char == 'j'):    # cube(x)
            cube += 1
            cube_par.append([])

        elif(char == 'k'):    # exp(x)
            output += "exp"

        elif(char == 'l'):    # square_root(x)
            output += "sqrt"

        elif(char == 'm'):    # cubic_root(x)
            cbrt += 1
            cbrt_par.append([])

        elif(char == 'n'):    # log(x)
            output += "log10"

        elif(char == 'o'):    # ln(x)
            output += "ln"

        elif(char == 'p'):    # abs(x)
            output += "abs"

        elif(char == 'q'):    # factorial(x)
            output += "factorial"
        
        elif(char == 'r'):    # deg(x)
            output += "degrees"
    
        elif(char == 's'):    # rad(x)
            output += "radians"
    
        elif(char == 't'):
            continue
    
        else:
            output += str(char)
            if(cube):
                if(char == '('):
                    cube_par[-1].append(1)
                elif(char == ')'):
                    cube_par[-1].pop()
                    if(not cube_par[-1]):
                        cube -= 1
                        cube_par.pop()
                        output += "^3"
  
            if(cbrt):
                if(char == '('):
                    cbrt_par[-1].append(1)
                elif(char == ')'):
                    cbrt_par[-1].pop()
                    if(not cbrt_par[-1]):
                        cbrt -= 1   
                        cbrt_par.pop()         
                        output += '^(1/3)'
    return output

if __name__ == "__main__":
    exp = [
    "m(11174148)*i(6.666)/p(18^2-3^11)-l(878791)*f(0.123)-g(0-0.4265)-a^a*k(8)-d(138)/h(72)",
    "h(72)+i(6.666)*b^3/k(8)+k(8)-g(0-0.4265)/p(18^2-3^11)/b^3/m(11174148)*c(140.5)",
    "p(18^2-3^11)-q(q(3))*m(11174148)*d(138)-c(140.5)*j(7.777)*p(18^2-3^11)*n(8*10^9-3.19*10^7)*a+b+d(138)",
    "b^3/b^3*f(0.123)+p(18^2-3^11)-l(878791)/c(140.5)/g(0-0.4265)+e(237)+f(0.123)+k(8)",
    "e(237)*k(8)*n(8*10^9-3.19*10^7)-p(18^2-3^11)/l(878791)+e(237)/l(878791)*c(140.5)*p(18^2-3^11)-o(8*a+b^b)",
    "k(8)-p(18^2-3^11)+n(8*10^9-3.19*10^7)*g(0-0.4265)*m(11174148)-e(237)-e(237)-m(11174148)*c(140.5)-a^a",
    "d(138)+b^3*p(18^2-3^11)*m(11174148)+a+b/q(q(3))-d(138)*e(237)+q(q(3))-j(7.777)",
    "p(18^2-3^11)+d(138)/c(140.5)-h(72)-h(72)/h(72)+p(18^2-3^11)-i(6.666)/q(q(3))*f(0.123)",
    "m(11174148)+g(0-0.4265)*b^3/c(140.5)/l(878791)/k(8)*f(0.123)+h(72)-o(8*a+b^b)+g(0-0.4265)",
    "m(11174148)*d(138)*o(8*a+b^b)*o(8*a+b^b)*j(7.777)*f(0.123)/g(0-0.4265)+g(0-0.4265)+g(0-0.4265)*a^a",
    "n(8*10^9-3.19*10^7)-o(8*a+b^b)-q(q(3))/i(6.666)-a+b*p(18^2-3^11)*p(18^2-3^11)+m(11174148)+n(8*10^9-3.19*10^7)+l(878791)",
    "n(8*10^9-3.19*10^7)*n(8*10^9-3.19*10^7)-p(18^2-3^11)*m(11174148)-q(q(3))+j(7.777)*q(q(3))+a+b+i(6.666)-e(237)",
    "i(6.666)*f(0.123)-e(237)/q(q(3))-a+b+o(8*a+b^b)*a+b-n(8*10^9-3.19*10^7)/h(72)/q(q(3))",
    "l(878791)-e(237)+l(878791)+c(140.5)+g(0-0.4265)/q(q(3))+i(6.666)-k(8)-k(8)-l(878791)",
    "f(0.123)+g(0-0.4265)/a+b*a+b*m(11174148)/j(7.777)*i(6.666)-j(7.777)-h(72)*k(8)"
    ]
    
    for i in exp:
        print(translate(i))

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