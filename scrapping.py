"""
Traten de escribir:

(empleados es una lista, jefes es otra lista)
En la lista empleados no hay elementos que también estén en la lista jefes)

(empleados es una lista, esJefe es una función que da True o False) 
En la lista empleados no hay elementos que esJefe dé True

Todos los elementos de la lista precios son mayores o iguales que 2000

(precio es una función que devuelve números)
Los precios de la lista productos son todos mayores que 1000

(n es un número)
La sumatoria de los números de 0 a n (contando el 0, sin contar el n) da menos que 100

(precio es una función que devuelve números)
La sumatoria de los precios de la lista compra da menos que 20000

(sueldo es una función que devuelve números)
Todos los elementos de la lista jefes tienen un sueldo mayor que 800000

(sueldo es una función que devuelve números, esJefe devuelve Bool)
En la lista empleados hay por lo menos uno que no es jefe y que gana más de 800000

Voy a expresar formalmente cada uno de estos enunciados usando notación de cálculo de predicados:

1. **En la lista empleados no hay elementos que también estén en la lista jefes.**

   \[
   \forall x \, (x \in \text{empleados} \implies x \notin \text{jefes})
   \]

   "Para todo \(x\), si \(x\) está en la lista `empleados`, entonces \(x\) no está en la lista `jefes`."

2. **En la lista empleados no hay elementos para los que esJefe dé True.**

   \[
   \forall x \, (x \in \text{empleados} \implies \neg \text{esJefe}(x))
   \]

   "Para todo \(x\), si \(x\) está en la lista `empleados`, entonces `esJefe(x)` es `False`."

3. **Todos los elementos de la lista precios son mayores o iguales que 2000.**

   \[
   \forall x \, (x \in \text{precios} \implies x \geq 2000)
   \]

   "Para todo \(x\), si \(x\) está en la lista `precios`, entonces \(x\) es mayor o igual a 2000."

4. **Los precios de la lista productos son todos mayores que 1000.**

   \[
   \forall x \, (x \in \text{productos} \implies \text{precio}(x) > 1000)
   \]

   "Para todo \(x\), si \(x\) está en la lista `productos`, entonces `precio(x)` es mayor que 1000."

5. **La sumatoria de los números de 0 a n (contando el 0, sin contar el n) da menos que 100.**

   \[
   \sum_{i = 0}^{n-1} i < 100
   \]

   "La sumatoria de todos los números desde 0 hasta \(n-1\) es menor que 100."

6. **La sumatoria de los precios de la lista compra da menos que 20000.**

   \[
   \sum_{x \in \text{compra}} \text{precio}(x) < 20000
   \]

   "La sumatoria de los precios de todos los elementos \(x\) en la lista `compra` es menor que 20000."

7. **Todos los elementos de la lista jefes tienen un sueldo mayor que 800000.**

   \[
   \forall x \, (x \in \text{jefes} \implies \text{sueldo}(x) > 800000)
   \]

   "Para todo \(x\), si \(x\) está en la lista `jefes`, entonces `sueldo(x)` es mayor que 800000."

8. **En la lista empleados hay por lo menos uno que no es jefe y que gana más de 800000.**

   \[
   \exists x \, (x \in \text{empleados} \land \neg \text{esJefe}(x) \land \text{sueldo}(x) > 800000)
   \]

   "Existe al menos un \(x\) tal que \(x\) está en la lista `empleados`, no es jefe (`esJefe(x)` es `False`), y el sueldo de \(x\) es mayor que 800000."

Estas expresiones usan la notación estándar de lógica matemática para representar cada uno de los enunciados.

"""


1#
empleados = [...]  # Lista de empleados
jefes = [...]  # Lista de jefes

# Comprobar que no hay ningún empleado que también sea jefe
no_duplicados = all(x not in jefes for x in empleados)
print(no_duplicados)


#2
empleados = [...]  # Lista de empleados

# Función esJefe
def esJefe(empleado):
    # Implementación que devuelve True o False
    pass

# Comprobar que no hay ningún empleado que sea jefe
ningun_jefe = all(not esJefe(x) for x in empleados)
print(ningun_jefe)

#3
precios = [...]  # Lista de precios

# Comprobar que todos los precios son mayores o iguales a 2000
todos_mayores = all(x >= 2000 for x in precios)
print(todos_mayores)

#4
productos = [...]  # Lista de productos

# Función que devuelve el precio de un producto
def precio(producto):
    # Implementación que devuelve el precio
    pass

# Comprobar que todos los productos tienen un precio mayor a 1000
precios_mayores = all(precio(x) > 1000 for x in productos)
print(precios_mayores)

#5
n = 10  # Ejemplo de valor para n

# Comprobar si la sumatoria de 0 a n-1 es menor que 100
sumatoria_menor_100 = sum(range(n)) < 100
print(sumatoria_menor_100)

#6
compra = [...]  # Lista de compra

# Función que devuelve el precio de un producto
def precio(producto):
    # Implementación que devuelve el precio
    pass

# Comprobar si la sumatoria de precios de la compra es menor que 20000
suma_precios_menor = sum(precio(x) for x in compra) < 20000
print(suma_precios_menor)

#7
jefes = [...]  # Lista de jefes

# Función que devuelve el sueldo de un jefe
def sueldo(jefe):
    # Implementación que devuelve el sueldo
    pass

# Comprobar si todos los jefes tienen un sueldo mayor que 800000
sueldo_mayor = all(sueldo(x) > 800000 for x in jefes)
print(sueldo_mayor)

#8
empleados = [...]  # Lista de empleados

# Funciones esJefe y sueldo
def esJefe(empleado):
    # Implementación que devuelve True o False
    pass

def sueldo(empleado):
    # Implementación que devuelve el sueldo
    pass

# Comprobar si hay al menos un empleado que no sea jefe y gane más de 800000
existe_empleado = any(not esJefe(x) and sueldo(x) > 800000 for x in empleados)
print(existe_empleado)

