def factorial(x):
    i = 1 
    factorial = 1
    while i <= x:
        factorial=factorial*i
        i=i+1
    return factorial

def sin(a):
    sin_a = 0
    for c in range(0,10,1):
        pi = 22/7
        b = a*(pi/180)
        sin_a = sin_a + ((-1)*c)(b**(2*c+1))/(factorial(2*c+1))
    return sin_a
        
def cos(a):
    cos_a = 0
    for c in range(0,10,1):
        pi = 22/7
        b = a*(pi/180)
        cos_a = cos_a + ((-1)*c)(b**(2*c))/(factorial(2*c))
    return cos_a

def tan(a):
    tan_a = sin(a)/cos(a)
    return tan_a

print("CHOOSE YOUR OPINION")
print("1-> TO CHECK SIN,COS,TAN OF AN ANGLE")
print("2-> DECIMAL TO BINARY CONVERSATION")
print()

choice = int(input("ENTER YOUR CHOICE :"))
print()
if choice == 1:
    d = float(input("Enter the sin value in degree:"))
    print()
    print("sin(",d,")",end=' = ')
    print(round(sin(d),3))
    print("cos(",d,")",end=' = ')
    print(round(cos(d),3))
    print("tan(",d,")",end=' = ')
    print(round(tan(d),4))
    
elif choice == 2:
    def DecimalToBinary(n):
        if n > 1:
            DecimalToBinary(n // 2)
        print(n % 2,end = '')
   
    d = float(input("Enter the decimal value:"))
    print()
    part1 = int(d)
    DecimalToBinary(part1)
    part2 = d - part1
    if part2 != 0:
        print(".",end ="")
    r=0
    while(part2 != 0 and r != 7):
        part2 = part2 * 2
        if part2 < 1:
            print("0",end='')
        else:
            print("1",end='')
            part2 = part2 - 1
        r=r+1
        
else:
    print("Invalid Choice!")