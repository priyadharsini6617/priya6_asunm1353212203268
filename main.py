#write a factorial program using recursive function
def fact_rec(n):
  if n==0 or n==1:
     return 1
  else:
    return n*fact_rec(n-1)
number=int(input("ENTER A NUMBER:"))
print("THE FACTORIAL OF",number,"IS:",fact_rec(number))
