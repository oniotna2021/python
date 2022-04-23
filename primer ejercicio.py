class Empleado:
    def __init__(self):
        self.nombre=input("Digite su nombre: ")
        self.sueldo=float(input("Digite el sueldo: "))
    
    def imprimir(self):
        print("El nombre es: ", self.nombre)
        print("El sueldo es: ", self.sueldo)
    
    def impuesto(self):
        if self.sueldo>3000:
            print(f"EL empleado {self.nombre} debe pagar impuestos")
        else:
            print(f"EL empleado {self.nombre} no debe pagar impuestos")


empl1=Empleado()
print()
empl1.imprimir()
print()
empl1.impuesto()

empl2=Empleado()