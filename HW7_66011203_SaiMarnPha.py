#Start of problem 1- Clock ----------------------------------------------

class Clock:

    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

        self.set_time(hour, minute, second)
    
    def set_time(self, hr , mn, sec) :

        if hr >= 24 or mn > 60 or sec > 60:
            exit("Invalid time format")
        
        self.hour = hr
        if hr == 24 :
            self.hour = 0
        if mn == 60 :
            self.minute = 0
            if self.hour < 23 :
                self.hour = hr+1
            else:
                self.hour = 0

        else :
            self.minute = mn
        if sec >= 60 :
            self.second = sec - self.second
        else :
            self.second = sec
    def get_time (self) :

        hr = self.hour
        mn = self.minute
        sec = self.second
        pm_am = 'am'
        if self.hour < 12 and self.hour > 0: #1-am to 11 am
            hr = self.hour
            pm_am = 'am'
        elif self.hour == 12 : #12 pm
            hr = self.hour
            pm_am = "pm"
        elif self.hour > 12 and self.hour < 24: #13 - 23
            hr = self.hour - 12
            pm_am = "pm"
        elif self.hour == 0 or self.hour == 24: # midnight
            hr = 12
            pm_am = 'am'
        return f'{hr:02}:{mn:02}:{sec:02} {pm_am}'

    def tick(self) :
        self.second += 1
        if self.second == 60 :
            self.second = 0
            self.set_time(self.hour, self.minute +1, self.second)


myclock = Clock(12,59,57)
print(myclock.get_time())
print("Set time to : 23:59:59")
myclock.set_time(23,59,59)
print("Increase time by ticking one second")
myclock.tick()
print(myclock.get_time())



#-------------------End of problem 1 ------------------------------------------------------

#Start of problem 2 -Polynomial ---------------


class Poly :
    

    def __init__(self, polynomial : tuple = ()):
        
        if type(polynomial) != tuple :
            exit("Polynomial argument must be in tuple")
        self.x = polynomial
    
    def print(self) :

        y = ''
        for (i, elem) in enumerate(self.x) :
            if elem == 0 :
                continue
            if i ==0 :
                y += f'{elem}'
            elif i == 1:
                elem = "{:+}".format(elem)
                y += f'{elem}x'
            else :
                elem = "{:+}".format(elem)
                y += f'{elem}x^{i}'
        if y[0] =='+' :
            y=y[1:len(y)]
        print(y)
    def scalar_multiply(self, n) :
        y = []
        for i, elem in enumerate(self.x) :
            y.append(elem * n)
        self.x = tuple(y)
        return self

    def multiply(self, P) :
        if type(P) != Poly :
            exit("P argument must be instance of Poly class")

        P = list(P.x)
        x = list(self.x)
        y = [0] * (len(P) * len(x))

        for (a, elem) in enumerate(P) :
            for (b, elem2) in enumerate(x) :
                y[ a+b ] += elem * elem2
       
        for i in range(len(y)-1, -1, -1) :
            if y[i] == 0 :
                y.pop(i)
            else :
                break
        return tuple(y)

    def power(self, n) :

        mulitpler = self
        for i in range(1, n) :
            multiply_res = self.multiply(mulitpler)
            mulitpler = Poly(multiply_res)
        return mulitpler
    
    def eval(self, n) :
        summation = 0
        for i, elem in enumerate(self.x) :
            summation += elem * n**i
        return summation


    def diff(self) :

        y = list(self.x)
        res = [0] * (len(y)-1)
        for i in range(0, len(y)) :
            if i == 0 :
                res[i]=0
            else :
                res[i-1]= y[i] * i
        self.x = tuple(res)
        return self

    def add(self, p) :

        larger_poly = self.x
        smaller_poly = p.x

        if len(p.x) >= len(self.x) :
            larger_poly = p.x
            smaller_poly = self.x
        
        larger_poly = list(larger_poly)
        smaller_poly = list(smaller_poly)

        for i in range(0, len(smaller_poly)) :
            larger_poly[i] += smaller_poly[i]
        
        self.x = tuple(larger_poly)
        return self

    def integrate(self) :
        
        poly = list(self.x)
        poly.append(0)
        res = [0] * len(poly)
        for i in range(0, len(poly)-1) :
            index = i+1
            res[index] = round(poly[i]/index, 2)
        
        self.x = tuple(res)
        return self
        


pol = Poly((1,0,-2))
pol.print()

q = pol.power(2)
q.print()

eval_val = pol.eval(3)


r = pol.add(q)
r.print()

r.diff().print()
pol.integrate().print()

#----------------------------------- End of problem 2 ---------------------

# Start of problem 3 -Linear equation-----------------

class LinearEquation:

    def __init__(self, a, b, c, d, e, f):

        self.__a = a
        self.__b = b
        self.__c = c 
        self.__d = d
        self.__e = e 
        self.__f = f

    def get_a(self) :
        return self.__a
    def get_b(self) :
        return self.__b
    def get_c (self) :
        return self.__c
    def get_d(self) :
        return self.__d
    def get_e(self) :
        return self.__e
    def get_f(self) :
        return self.__f
    
    def isSolvable(self) :
        return not (( self.__a * self.__d - self.__b * self.__c ) == 0 )
    
    def getX(self) :
        x = (self.__e * self.__d  - self.__b * self.__f) / (self.__a * self.__d - self.__b * self.__c)
        return round(x, 3)

    def getY(self) :
        y = (self.__a * self.__f  - self.__e * self.__c) / (self.__a * self.__d - self.__b * self.__c)
        return round(y, 3)

lq = LinearEquation(10,2,3,4,50,6)
print("get_a: ", lq.get_a())
print("get_b : ", lq.get_b())
print("get_c : ", lq.get_c())
print("get_d : ", lq.get_d())
print("get_e : ", lq.get_e())
print("get_f : ", lq.get_f())
print("Get Y value : ",lq.getY())
print("Get X value : ",lq.getX())


