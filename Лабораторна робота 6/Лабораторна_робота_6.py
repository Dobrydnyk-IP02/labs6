def user_input():
    n=int(input("n = "))
    return n

def fact(k):
 if k==0:   
   return 1
 else:
    return k*fact(k-1)

def draw_triangle(number):
    for j in range(0, n+1):
         for c in range(j+1):
             print(fact(j) // (fact(c) * fact(j - c)), end=" ")
         print()


def do_exercise(n):
   if n>0:
     draw_triangle(n)
   else:
       print("Error!!!")   


n=user_input()
do_exercise(n)