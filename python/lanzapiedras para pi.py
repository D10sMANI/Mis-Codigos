import random

N=1000000
M=N
c=0
q=0


while N>0:
  
    x=2*random.random()-1
    y=2*random.random()-1


    if x**2 + y**2 <= 1:
        c=c+1
    else:
        q=q+1

    N=N-1


Pi=4*c/M

print("Con ", M, "piedritas virtuales, he calculado el valor de Pi")

print("El valor aproximado de Pi es: ", Pi)

