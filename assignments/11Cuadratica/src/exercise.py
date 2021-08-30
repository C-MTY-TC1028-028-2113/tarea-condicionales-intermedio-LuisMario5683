import math

def main():
    # Escribe tu código abajo de esta línea
    aa=int(input("Da el valor de a: "))
    b=int(input("Da el valor de b: "))
    c=int(input("Da el valor de c: "))
    if (aa==0) and (b==0):
        print("No tiene solucion")
    elif (aa==0):
        raiz=-c/b
        print(raiz)
    else:
        discrim=b**2-4*aa*c
        if (discrim)>0:
            x1=(-b+math.sqrt(discrim))/(2*aa)
            x2=(-b-math.sqrt(discrim))/(2*aa)
            print(x1)
            print(x2)
        elif (discrim < 0):
            print("Raices complejas")
        else:
            x=-b/(2*aa)
            print(x)

if __name__ == '__main__':
    main()
