f=open("C:/Users/서희/Desktop/git/git/ddd.txt",'r')
while True:
    line=f.readline()
    if not line: break
    print(line)
f.close()
