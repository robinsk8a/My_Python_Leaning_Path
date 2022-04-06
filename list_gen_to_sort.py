names = list()
inp=None

#El siguiente loop me genera una lista basada en entradas externas. Los numeros son convertidos a formato int y las entradas str se mantienen
#por lo que se genera una lista mixta de int y str

while inp != "Done":
  
  print("insgresa un nombre:")
  inp= input()
  if inp == "Done":
    break
  try:
    inp = int(inp)
  except:
    inp = inp
  names.append(inp)

print(names)

#Al final del primer loop se coge esa misma lista y se convierten los numeros en formato int a str para poder aplicar el metodo sort
#y conseguir una lista ordenada

for i in range(0, int(len(names))):
  if type(names[i]) != str:
    names[i]=str(names[i])

names.sort()
print(names)
