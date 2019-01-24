def avg(*args):
    result=0
    for i in args:
        result=result+i
    result=result/len(args)
    print(result)
