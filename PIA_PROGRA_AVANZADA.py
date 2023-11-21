class Tres_programas:

    def __init__(self, compra, NOM, PES, LON, GAL):
        self.compra = compra

        self.NOM = NOM
        self.PES = PES
        self.LON = LON

        self.GAL = GAL

    def descuento_clientes(self):
        if self.compra < 500:
            pagar = self.compra
            print("El costo a pagar es:", pagar)
        elif (self.compra >= 500) and (self.compra < 1000):
            pagar = (self.compra) - (self.compra *.05)
            print("El descuento es del 5% y el costo final es:", pagar)
        elif (self.compra >= 1000) and (self.compra < 7000):
            pagar = (self.compra) - (self.compra *.11)
            print("El descuento es del 11% y el costo final es:", pagar)
        elif (self.compra >= 7000) and (self.compra <= 15000):
            pagar = (self.compra) - (self.compra *.18)
            print("El descuento es del 18% y el costo final es:", pagar)
        elif (self.compra > 15000):
            pagar = (self.compra) - (self.compra *.25)
            print("El descuento es del 25% y el costo final es:", pagar)


    def dinosaurio(self):
        peskil = (self.PES) * (1000/1)
        lonmet = (self.LON) * (0.3047/1)

        print("Nombre:",self.NOM)
        print("Peso en kilogramos de",self.NOM,":",peskil)
        print("Longitud en metros de",self.NOM,":",lonmet)

    def gasolina(self):
        cant_litros = (self.GAL * 3.785)
        total = cant_litros * 8.20

        print("Total a pagar:",total)

    def archivos_texto(self, modo='lectura', contenido=None):
        nombre_archivo = f"{self.NOM}_info.txt"

        if modo == 'escritura':
            with open(nombre_archivo, 'w') as archivo:
                archivo.write(f"{self.NOM} - Información:\n")
                archivo.write(f"Compra: {self.compra}\n")
                archivo.write(f"Peso: {self.PES}\n")
                archivo.write(f"Longitud: {self.LON}\n")
                archivo.write(f"Galones: {self.GAL}\n")

            print(f'Se ha creado y escrito en el archivo {nombre_archivo}')

        elif modo == 'lectura':
            try:
                with open(nombre_archivo, 'r') as archivo:
                    contenido = archivo.read()
                print(f'Contenido del archivo {nombre_archivo}:\n{contenido}')
                return contenido
            except FileNotFoundError:
                print(f'El archivo {nombre_archivo} no existe.')
   

#bloque principal
print("\nMetodo 1 - Descuento a clientes.")
print("------------------------------------------------------------------")
print("     [Cliente Descuento 1]")
cliente1 = Tres_programas(25314.18, "", "", "", "")
cliente1.descuento_clientes()
cliente1.archivos_texto(modo='escritura')
cliente1.archivos_texto()
print("     [Cliente Descuento 2]")
cliente2 = Tres_programas(6850, "", "", "", "")
cliente2.descuento_clientes()
cliente2.archivos_texto(modo='escritura')
cliente2.archivos_texto()
print("\n")

print("Metodo 2 - Dinosaurio.")
print("------------------------------------------------------------------")
print("      [Dinosaurio 1]")
dinosaurio1 = Tres_programas("", "Plateosaurus", 5, 30, "")
dinosaurio1.dinosaurio()
dinosaurio1.archivos_texto(modo='escritura')
dinosaurio1.archivos_texto()
print("     [Dinosaurio 2]")
dinosaurio2 = Tres_programas("", "Diplojocus", 15, 90, "")
dinosaurio2.dinosaurio()
dinosaurio2.archivos_texto(modo='escritura')
dinosaurio2.archivos_texto()
print("\n")

print("Metodo 3 - Gasolinera.")
print("------------------------------------------------------------------")
print("      [Cliente Gasolinera 1]")
gasolinera = Tres_programas("","","","", 19.90)
gasolinera.gasolina()
gasolinera.archivos_texto(modo='escritura')
gasolinera.archivos_texto()
print("     [Cliente gasolinera 2]")
gasolinera2 = Tres_programas("","","","", 8.40)
gasolinera2.gasolina()
gasolinera2.archivos_texto(modo='escritura')
gasolinera2.archivos_texto()
print("\n")