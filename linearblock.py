import random
import numpy

fp=open("output(linearblock)_108064501.txt","w")
#random 1Kbits for binary data
x=[]
checkbit=[]
P=numpy.zeros((1024,11))
errcount=0
counter1=len(x)
while counter1<1024:
    if random.random()<0.5:
        x.append(0)
        counter1=counter1+1
    else:
        x.append(1)
        checkbit.append(counter1)
        counter1=counter1+1
x=numpy.array(x)
print("Original data=",x)
fp.write("Original data=")
for i in x:
    fp.write(str(i))
#Setting P
for i in range(1024,0,-1):
    binary=format(i,'b').zfill(11)
    a=i
    for j in range(0,11):
        if binary == '10000000000':
            break
        if binary == '01000000000':
            break
        if binary == '00100000000':
            break
        if binary == '00010000000':
            break
        if binary == '00001000000':
            break
        if binary == '00000100000':
            break
        if binary == '00000010000':
            break
        if binary == '00000001000':
            break
        if binary == '00000000100':
            break
        if binary == '00000000010':
            break
        if binary == '00000000001':
            break
        if binary == '00000000000':
            break
        P[1024-i,j]=binary[j]
#Setting H_T
H_T=numpy.vstack((P,numpy.identity(11)))
#Setting H
H=numpy.transpose(H_T)
#Setting G
G=numpy.hstack((numpy.identity(1024),P))
#Setting C
C=numpy.mat(x)*numpy.mat(G)%2
C=C.astype(numpy.int64)
fp.write("\nEncoded data=")
for i in range(0,1024+11):
    fp.write(str(C[0,i]))
#Ruinning the data
ruinnum=random.randint(0,1024+11)
print("ruinplace=",ruinnum)
fp.write("\nruinplace=")
fp.write(str(ruinnum))
if C[0,ruinnum] == 0:
    C[0,ruinnum] = 1
else:
    C[0,ruinnum] = 0
fp.write("\nDefective data=")
for i in range(0,1024+11):
    fp.write(str(C[0,i]))
#Recover the data
H_T=H_T.astype(numpy.int64)
syndrome=numpy.mat(C)*numpy.mat(H_T)%2
syndrome=syndrome.astype(numpy.int64)
fp.write("\nDecoded data=")
fp.write(str(syndrome))
#Compare the original data and decoded data
for i in range(0,1024):
    if i == ruinnum:
        errcount=errcount+1
print("The number of bit(s) error detected:",errcount)
fp.write("\nThe number of bit(s) error detected:")
fp.write(str(errcount))
#Detect the error or not
if (syndrome.A==H_T[ruinnum]).all():
    print("Corrected!")
    fp.write("\nCorrected!")
else:
    print("Not Corrected!")
    fp.write("\nNot Corrected!")
fp.close()