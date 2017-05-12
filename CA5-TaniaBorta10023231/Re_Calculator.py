#Tatiana Borta
#10023231
#CA5 part_a 

def add(first, second):#add numbers
	return map(lambda x, y: x+y, first, second)

def substract(values):#substract two numbers
    return reduce(lambda x, y: x-y, values)

def devide(first, second):#devide two numbers
    return map(lambda x, y: x/float(y) if y != 0 else 'nan',first, second)
	
def multiply(values):#multiplying two numbers
    return reduce(lambda x, y: x*y, values)

def exponential(values): #exponential
    return reduce(lambda x, y: x**float(y), values)
	
def cube(num): #cube
	return map(lambda x: x**3, num)
	
def sqrt(num1): #square root
    return map(lambda x: x ** (1/2.0), num1)

def lessthanmean(values): # numbers less than mean
	mean = sum(values)/len(values)
	return filter(lambda x: x<mean, values)
	
def fizzbuzz(values): #and legendary fizzbuzz
    return filter(lambda x: x%3==0 and x%5==0, values)	
	
def pythagorean(n):#as generator
	for x in range(1,n):
		for y in range(x,n):
			for z in range(y,n):
				if x**2 + y**2 == z**2:
					yield (x,y,z)

pyt = pythagorean(50)
for v in pyt:
    print 'Pythagorean as generator\n', v,

#as list comprehension
pythagorean = [(x,y,z) for x in range(1,30) for y in range(x,30) for z in range(y,30) if x**2 + y**2 == z**2]	
print 'Pythagorean as list comprehension: \n', pythagorean

print 'Addition function: ', add([12, 45, 34, 23], [2, 4, 6, 0])	
print 'Substraction function: ', substract([45, 34, 12])
print 'Devision function: ', devide([2, 4,6], [3, 5, 0])
print 'Multiplying function: ', multiply([2, 4, 6])
print 'Exponential function: ',exponential([3, 3, 2])
print 'Cube function: ', cube([1, 2, 3, 5, 7, 9])
print 'Square root function: ', sqrt([2, 3, 4, 5])
print 'Less than mean :', lessthanmean([22, 33, 44, 55, 66]) 
print 'Legendary FizzBuzz: ', fizzbuzz([15, 34, 30, 100, 9, 20, 60])




