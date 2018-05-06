import sys
def func(num):
    for n in range(1, num+1):
        print(' '*(num-n),'#'*n)

if __name__=="__main__":
    num = int(sys.argv[1])	
    func(num)
