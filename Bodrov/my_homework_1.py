from re import X


Ishodniy_spisok=[1,"ZERO",354,"What do you do?", 156]
End=[]
def revers(Ishodniy_spisok, End):
 for n in range(len(Ishodniy_spisok)):
    End[n]=Ishodniy_spisok[len(Ishodniy_spisok)-n - 1]

    return(End)


#------------------------------------------------

Spisok=[12, 378, 4]
sum=0
def Sred(sum, Spisok):
 for n in range(len(Spisok)):
    sum=sum+len(Spisok[n])

    return(sum/len(Spisok))

#------------------------------------------------
arg = ["her", "name", "is", "Masha", "Masha", "is", "a", "sister", "of", "Zhenya"]
def Slovar(arg):
    for n in range(len(arg)):
        return(arg[n]+n)

#------------------------------------------------

arg1 = ["my", "name", "is", "Masha"]
arg2 = ["my", "name", "is", "Zhenya"]
i=0
ARG=[]
A=0
def Sovpad(arg1, arg2):
    for n in range(len(arg1)):
        if arg1[n]==arg[i]:
            ARG[A]=arg1[n]
            A=A+1
    i=i+1
    
    return ARG

#------------------------------------------------

arg = ["aaa", "aaa", "bbb", "ccc", "bbb"]
i=0
N=1
def Chastota(arg):
    for i in range(len(arg)):
        for n in range(len(arg)):
            if arg[i]==arg[n]:
                N=N+1
                continue
            if n==len(arg)-1:
                return(arg[i]+N)

#--------------------------------------------

arg = ["abcd", "a", "ab", "abc", "bazinga", "bar"]
max=1000
arg2=[]
def sort(arg):
    for i in range(len(arg)):
        for n in range(len(arg)):
            if arg[n]<=min:
                b=n
                min=arg[n]
            
            if n==len(arg)-1:
                c=arg[b]
                arg[b]=arg[i]
                arg[i]=c
                n=n+1  

#-----------------------------------------------------
B0=1
N0=2
B1=2
N1=3
F=[B0,N0]
L=[B1, N1]

def Chess(F, L):
    for i in range(9):
        if F[0]==L[0] or F[1]==L[1]:
          print('true')
          
          if F[0]==L[0]-1*i and F[1]==L[1]-1*i:
              print ('true')

              if F[0]==L[0]+1*i and F[1]==L[1]+1*i:
                  print ('true')
                  
                  if F[0]==L[0]+1*i and F[1]==L[1]-1*i:
                    print ('true')

                  if F[0]==L[0]-1*i and F[1]==L[1]+1*i:
                     print ('true')
                     
        else:
            print("false")





