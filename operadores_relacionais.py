idade = int(input("Coloque a sua idade: "))
if(idade<=0):
    print("A sua idade não pode ser 0 ou menor do que 0")
else:
    if(idade>150):
        print("A sua idade é maior que 150")
    else:
        if(idade>18):
            print("A sua idade é maior que 18 anos")