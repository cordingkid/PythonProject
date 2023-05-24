def fnum(a):
    strr = ""
    for i in range(1,9+1):
        strr += "{} x {} = {}\n".format(a,i,a*i)
    print(strr)


if __name__ == '__main__':
    a = list(range(2,9+1))
    a.reverse()
    
    for i in a:
        if (i % 2 == 1) or (i==2):
            fnum(i)
            
