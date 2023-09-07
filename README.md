# Proyecto
El programa “Ficsit Efficient Factory Module” tiene como objetivo apoyar a los pioneros en el juego Satisfactory encontrando los requisitos y posibilidades que se pueden encontrar dentro del juego una vez que encuentres un depósito de minerales en el mundo. El propósito de esto es encontrar la manera más eficiente de producir materiales para que siempre se esté haciendo lo mejor y no se pierda el tiempo por el mal uso de materiales.

Dependiendo del tipo y la calidad del depósito de minerales este programa encontrará que puedes construir para que puedas definir qué es lo que necesitas y si tienes los materiales requeridos o si quieres puedes mejorar la eficiencia de las fábricas que ya tienes. Así podrás ver si es que tienes los materiales necesarios para construir materiales avanzados como motores, o si sólo puedes construir algo básico como placas o barras de metal.

Dependiendo de la información que introduzcas el programa checara si tienes los requisitos mínimos de cada material y luego te dirá cuantos constructores podrías tener del material. Con el material más básico en el juego el hierro, como ejemplo describiré cómo podría ser útil. Podrías introducir que solo tienen un depósito de baja calidad y te diria que puedes producir una línea de placas de metal, dos líneas de barras de hierro, o tres líneas de tornillos, pero en cambio si pones que tienes una mina de hierro puro te diria que puedes producir 4 líneas de placas de hierro, 8 líneas de barras de hierro, 12 líneas de tornillos, 2 líneas de placas de hierro reforzadas, o una línea de marcos modulares.

Avanze 1:
El programa empieza preguntando cuanto hiero produces por minuto "iron_ppm" y basado en eso te dice cuantas lineas de producion puedes crear de un material, por ejemplo para laminas de hierro "iron_sheets" necesitan 30 ppm asi que divide el hierro entre 30 y te dice cuantas lineas puedes crear. Si no puedes crear una linea te dice que no tienes suficientes para una linea de ese material. Para los tornillos "screws" es un poco distinto ya que estan hechos de un material que no es el hierro basico. Esta hecho de barras de hierro "iron_rods" haci que divide el resultado de esa operacion para decirte si puedes hacer una linea de tornillos.

Avanze 2:
El programa usa operaciones para encontrar que tantas lineas completas de producion para cada material puedes hacer, usa divisiones sin residuo para esto.

Avanze 3:
Empeze a usar Def para las areas que se repiten, no se puede usar en todas las partes del codigo ya que en muchas de estas se usan valores que van variando de material a material. Los estoy usando para unos edificios que se necesitan para la producion de materiales. Muchos de estos materiales tienen un numero similar de edificios requiridos. Tambien se usa para que determine que nivel de conveyor belts que necesita segun cuanto produce.

Avanze 4:
El codigo usa if y else para determinar si tienes lo suficiente para poder fabricar algun material, tambien se puede ver dentro de una funcion para ver que nivel de conveyorbelt necesita la producion del material, entre mas materiales produces, mas alto va a ser el nivel de los conveyor belts que necesitas.
