print(" ")#DEFINE UNA LINEA EN BLANCO
print("Roman De la Cruz Leonardo Antonio, 3-w.no.1211")
print(" ")
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(10)