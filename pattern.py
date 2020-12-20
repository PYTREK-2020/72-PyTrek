def pattern(n):
    for i in range(1,n+1):
        m=i
        for j in range(1,i+1):
            print(m,end=' ')
            m=m+1
        m=m-2
        for j in range(1,i):
            print(m,end=' ')
            m=m-1
        print()            

n=int(input("Enter the number of lines upto which the pattern to be printed : "))
pattern(n)