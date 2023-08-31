iron_ppm=int(input("How much iron ore do you produce per minute"))
"""
Este input recibe un numero que se usa para definir que tanto matieral produces y luego
lo convierte en otro valor para decirte cuanto puedes construir
"""

iron_sheets=iron_ppm//30
iron_rods=iron_ppm//15
screws=iron_rods//.66
"""
Las operaciones calculan cuantas lineas de produccion puedes hacer para cada material
usando una division. Si necesitas 30 de hierro para una linea, divide el hierro que
tienes entre 30 y te da el numero esacto de lineas de producion que puedes hacer.
"""

if iron_sheets>=1:
    print("You can produce",iron_sheets,"lines of iron sheets")
else:
    print("You cannot produce iron sheets.")
if iron_rods>=1:
    print("You can produce",iron_rods,"lines of iron rods")
else:
    print("You cannot produce iron rods.")
if screws>=1:
    print("You can produce",screws,"lines of screws")
else:
    print("You cannot produce screws.")
"""
Estos "if" y "else" te dicen si puedes producir una linea de un material o si no
tienes suficiente material.
"""
