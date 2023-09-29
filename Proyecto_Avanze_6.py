def smelt_and_construct(metal,product):
    smelters=metal//30
    print("You need",smelters,"smelters for this line")
def conveyors(conveyors):
    if conveyors<=2:
        print("Use Level 1 Conveyors")
    if conveyors==3:
        print("Use Level 2 Conveyors")
    if conveyors==4:
        print("Use Level 3 Conveyors")
    if conveyors>=5:
        print("Use Level 4 Conveyors")
    
"""
Esta funcion la escribi para encontrar cuantos edificios va a tener la fabrica,
un smelter es constante ya que siempre se necesita uno por cada 30 iron_ppm,
los constructors son uno por cada linea de fabricacion. Los conveyors son para
indicar si son suficientemente rapidos para tansportar los productos sin que
se acumulen los materiales. Si son muchos materiales necesitas mejores conveyors
"""

print("Welcome to the Ficsit Efficient Factory Module")

active_program=0

iron_ppm=0

factorynumber=1

while active_program!=1:
    quicklist=["Factory number"]
    quicklist.append(factorynumber)
    quicklist.append("Quicklist factory for:")
    active_program=int(input("What ore does your factory use? \n"
                             "Press 1 To End Program \n"
                             "Press 2 For Iron"))
    if active_program==2:
        iron_ppm=int(input("How much iron ore do you produce per minute in this module"))
        """
        Este input recibe un numero que se usa para definir que tanto matieral
        produces y luego lo convierte en otro valor para decirte
        cuanto puedes construir.
        """

        iron_sheets=iron_ppm//30
        iron_rods=iron_ppm//15
        screws=iron_rods//.66
        
        """
        Las operaciones calculan cuantas lineas de produccion puedes hacer
        para cada material usando una division. Si necesitas 30 de hierro
        para una linea, divide el hierro quetienes entre 30 y te da el numero
        esacto de lineas de producion que puedes hacer.
        """
        quicklist.append(iron_ppm)
        quicklist.append("iron or per minute")
        if iron_sheets>=1:
            print("You can produce",iron_sheets,"lines of iron sheets")
            smelt_and_construct(iron_ppm,iron_sheets)
            conveyors(iron_sheets)
            quicklist.append("Iron Sheet Line(s)")
            quicklist.append(iron_sheets)
    
        else:
            print("You cannot produce iron sheets.")
            quicklist.append("Iron Sheet Line(s) 0")
    
        if iron_rods>=1:
            print("You can produce",iron_rods,"lines of iron rods")
            smelt_and_construct(iron_ppm,iron_rods)
            conveyors(iron_rods)
            quicklist.append("Iron Rod Line(s)")
            quicklist.append(iron_rods)

        else:
            print("You cannot produce iron rods.")
            quicklist.append("Iron Rod(s) 0")
    
        if screws>=1:
            print("You can produce",screws,"lines of screws")
            smelt_and_construct(iron_ppm,screws)
            print("You also need", iron_rods,\
            "more constructors for metal pipes for the screws.")
            conveyors(screws)
            quicklist.append("Screw Line(s)")
            quicklist.append(screws)

        else:
            print("You cannot produce screws.")
            quicklist.append("Screw Line(s) 0")
        print(quicklist)
        factorynumber=factorynumber+1
"""
Estos "if" y "else" te dicen si puedes producir una linea de un material o si no
tienes suficiente material.
"""
print("Thank you for using the Ficsit Efficient Factory Module")
