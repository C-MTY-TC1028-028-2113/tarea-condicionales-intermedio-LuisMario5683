def main():
    # Escribe tu código abajo de esta línea
    cm = int(input("Introduce los cm: "))
    if cm<100:
        print(cm,"cm")
    elif cm<1000:
        x=cm//100
        y=cm-(x*100)
        print(x,"m")
        if y!=0:
            print(y,"cm")
    else:
        x=cm//100000
        y=(cm-(x*100000))//100
        z=(cm-(x*100000)-(y*100))
        if x!=0:
            print(x,"km")
        if y!=0:
            print(y,"m")
        if z!=0:
            print(z,"cm")

if __name__ == '__main__':
    main()
