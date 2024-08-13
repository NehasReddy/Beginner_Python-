for i in range(5):
    for j in range(5):
        print("*",end="")
    print()

for i in range(5):
    for j in range(i+1):
        print("*",end="")
    print()


for i in range(5):
    for j in range(i+1):
        print(j,end=" ")
    print()

for i in range(3):
    for j in range(i+1):
        print(i+1,end="")
    print()

for i in range(7):
    for j in range(i+1):
        print(chr(65+i),end="")
    print()

for i in range(4):
    for j in range(i+1):
        print(chr(65+j+i),end="")
    print()

for i in range(5):
    for j in range(5-i-1,5):
        print(chr(65+j),end="")
    print()

for i in range(4):
    for j in range(4-i-1):
        print(" ",end=" ")
    for j in range(i+1):
        print(j+1,end=" ")
    print()

for i in range(4):
    for j in range(i+3):
        print(4-i,end="")
    print()
#REP
for i in range(4):
    #print leading spaces
    for j in range(4-i-1):
        print(" ",end="")
    #print increasing sequence
    for j in range(i+1):
        print(i+j+1,end="")
    #print decreasing sequence
    for j in range(i,0,-1):
        print(i+j,end="")
    print()




    
