
numest = int(1)


while(numest <= 10):
    print()
    print(f"Encuestado #{numest}")
    stu = str(input("Estudiante: "))
    proy = str(input("Proyecto: "))
    print(f"Estudiante{numest}: ",stu, " - ","Proyecto: ", proy)
    numest += 1
