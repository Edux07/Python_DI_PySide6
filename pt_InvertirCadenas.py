#Invirtiendo cadenas restando
def invest(txt:str):
    num_txt=len(txt)
    final_txt=" "
    for i in range(0,num_txt):
        final_txt +=txt[num_txt-1-i]
        print(final_txt)
invest("hola")



#Usando los metodos propios de la casa
cadena  ="Hola mundo"
cadena_invertida=cadena[::-1]
print(cadena_invertida)