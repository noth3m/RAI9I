''' This is the official assignment 3 file for RAI subject of Class 9 I , Please do note that the code is not commented and question number 2 , 5 ,6 and 9 are not 
included so they will give input error when asked for '''
class assignment3:    
    class tablequestions :   
        def ques1(n):
            for i in range(n):
                for j in range(i+1):
                    print('*',end='')
                print()
        def ques2(n):
            str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            for i in range(n):
                for j in range(i+1):
                    print(str[j],end =' ')
                print()
        def ques3(n):
            for i in range(1,n+1):
                for j in range(i):
                    print(i,end =' ')
                print()
        def ques4(n):
            k = 1
            for i in range(0,n):
                for j in range(0,i+1):
                    print(k-1,end = '')
                    k = k + 1
                print()
        def ques5(n):
            for i in range(n):
                x = 1
                for j in range(n-i):
                    print(end= ' ')
                for k in range(i+1):
                    print(x,end='')
                    x = x + 1
                print()
        def ques6(n):
            for i in range(n):
                i = n-i
                for j in range(i):
                    print('*',end='')
                print()
        def ques7(n):
            for i in range(1,n+1):
                for j in range(n-i):
                    print(end=' ')
                for k in range(2*i-1):
                    print('*',end='')
                print()
        def ques8(n):
            for i in range(n):
                for j in range(i):
                    print(end=' ')
                x = n - i 
                for k in range(2*x-1):
                    print('*',end='')
                print('')
        def ques9(n):
            for i in range(n):
                for k in range(n-i):
                    print(" ",end='')
                x = 1
                for j in range(i + 1):
                    print(x,end='')
                    x = x + 1
                for k in range(i):
                    print(i,end='')
                    i = i-1
                print()
        def ques10(n):
            x = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            m = n
            for i in range(n):
                for j in range(i):
                    print(' ',end='')
                u = 0
                for k in range(m):
                    print(x[slice(u,u +1)],end=' ')
                    u = u + 1
                m= m -1
                print()
        def ques11(n):
            for i in range(n):
                x = 1
                if i%2 == 0 :
                    for j in range(i+1):
                        print(x,end='')
                        x = x + 1
                    print()
            for l in range(1,n):
                x = 1
                if l%2 == 0:
                    for m in range(n-l):
                        print(x,end='')
                        x = x + 1
                    print()
        def ques12(n):
            for i in range(n):
                for j in range(n-i):
                    print('*',end='')
                for k in range(i):
                    print(' ',end='')
                for l in range(i-1):
                    print(' ',end='') 
                if i == 0:
                    for m in range(n-i-1):
                        print('*',end='')
                else:
                    for m in range(n-i):
                        print('*',end='')
                print()      
        def ques13(n):
            for i in range((n+1)//2):
                for j in range(n-i):
                    print('*',end='')
                print()
            for k in range(((n+1)//2)+1,n+1):
                for l in range(k):
                    print('*',end='')
                print()
        def ques14(n):
            for i in range(1,n+1):
                if i <= (n+1)//2:
                    for j in range(((n+1)//2)-i):
                        print(' ',end='')
                    for j in range((2*(i))-1):
                        print('*',end='')
                    print()
                else:
                    for j in range(i-(n+1)//2 ):
                        print(' ',end='')
                    for j in range(2*(n-i+1)-1):
                        print('*',end='')                    
                    print()                        
        def ques15(n):
            for i in range(n):
                if i == 0 or i == n-1:
                    for j in range(n):
                        print('*',end='')
                else:
                    for k in range(n):
                        if k == 0 or k == n-1:
                            print('*',end='')
                        else:
                            print(' ',end='')
                print()
        def ques16(n):
            for i in range(n):
                for j in range(n):
                    if j == i:
                        print('$',end='')
                    elif j == 0 or i == 0 or j == n -1 or i == n- 1:
                        print('*',end='')
                    else:
                        print(' ',end='')
                print() 
        def ques17(n):
            for i in range(n):
                for j in range(n):
                    if j == i or j == n-i-1:
                        print('$',end='')
                    elif j == 0 or i == 0 or j == n -1 or i == n- 1:
                        print('*',end='')
                    else:
                        print(' ',end='')
                print()
        def ques18(n):
           print()
        def ques19(n):
            for i in range(n):
                for j in range(n):
                    if  j == n-i-1:
                        print('*',end='')
                    elif i == 0  or i == n- 1:
                        print('*',end='')
                    else:
                        print(' ',end='')
                print()
    class textquestions:
        def ques1(n):
            assignment3.tablequestions.ques18(n)
        def ques2(n):
            str_abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            for i in range(n):
                x = []
                for j in range(n-i):
                    print(str_abc[j],end='')
                    x = x + [str_abc[j]]
                for k in range(2*i):
                    print(' ',end='')
                for l in range(1,n-i+1):
                    print(x[-l],end='')
                print()
        def ques3(n):
            y = []
            for i in range(1,n+1):
                x=0
                for j in range(1,i+1):
                    if j == i or j == 1:
                        continue
                    else:
                        if i%j == 0:
                            x= 1
                            break
                if x != 1:
                    print(i)
                    y = y + [j]
                else:
                    continue
            print()
            print(f'The sum of all prime numbers is:{sum(y)}')
        def ques4(n):
            for i in range(1,n+1):
                for j in range(2**n):
                    print()
        def ques6(n):
            x=[]
            for i in range(1,n+1):
                k=i
                for j in range(1,i+1):
                    k = k*j
                x = x + [i/k]
                if i == n:
                    print(f'The Factorial of n is: {k}')
            print()
            z = sum(x) + 1
            print(f'The sum of the division of the numbers and their factorial till n is {z}')
        def ques7(n):
            for i in range(1,n+1):
                if i > 9:
                    x = str(i)
                    y = []
                    for j in range(len(x)):
                        y = y + [int(x[j])**3]
                    if sum(y) == i:
                        print(i)
                    else:
                        continue
        def ques8(dec_num):
            oct_num = ''
            while dec_num > 0:
                z = dec_num%8
                dec_num = dec_num//8
                oct_num += str(z)
            oct_num = int(oct_num[::-1])
            hex_num = ''
            while dec_num > 0:
                z = dec_num%16
                if z > 9:
                    ab = 'ABCDEFGH'
                    z = ab[z-10]
                dec_num = dec_num//16
                hex_num += str(z)
            hex_num = (hex_num[::-1])
            bin_num =''
            while dec_num > 0:
                z = dec_num%2
                dec_num = dec_num//2
                bin_num += str(z)
            bin_num = (bin_num[::-1])
            print(f'\nBinary Number: {bin_num}')
            print(f'\nOctal Number: {oct_num}')
            print(f'\nHexaDecimal Number: {hex_num}')
        def ques9(x,n):
            x = []
            for i in range(1,n+1):
                x = x + (1/2)*((x-1)/x)**i
            print(f'Natural Logarithm is {sum(x)}')
        def ques10(n):
            x = []
            m = n
            while m > 0:
                grade = int(input(f'Enter Grade of subject {m}'))
                x = x + grade
                m = m - 1
            print(f'Average of all grades is {(sum(x)/n)}')
            if (sum(x)/n) <= 40:
                print('\nFAIL')


