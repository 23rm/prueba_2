lista_vacia=[]
dias=["lunes", "martes","miércoles",
      "jueves","viernes","sábado","domingo"]
print(dias)
print(type(dias))

dias[1]="MARTES"
print(dias)

dias[2:4]=["MIERCOLES","JUEVES"]
print(dias)

dias[4:]=["VIERNES"]
print(dias)

dias[0]="LUNES"
print(dias)