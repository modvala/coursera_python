import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
print(int((-b+(b*b-4*a*c)**.5)/2*a), '\n',int((-b-(b*b-4*a*c)**.5)/2*a))  
