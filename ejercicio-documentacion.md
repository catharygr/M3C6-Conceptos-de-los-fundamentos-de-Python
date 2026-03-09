# Documentación sobre lo conceptos fundamentales de Python, APIs y DB.

# ¿Para qué usamos Clases en Python?

Las clases en Python son una herramienta fundamental de la programación orientada a objetos. Nos permiten crear nuestros propios tipos de datos, agrupando variables (llamadas atributos) y funciones (llamadas métodos) que tienen sentido juntas. Así, podemos modelar cosas del mundo real o conceptos abstractos de forma ordenada y reutilizable. Se puede decir que son como un molde o una plantilla a partir de cual podemos crear los diferentes objetos que comparten funcionalidades heredadas.

**¿Por qué se usan?**

- Para organizar el código y evitar repeticiones.
- Para reutilizar funcionalidades en diferentes partes del programa.
- Para modelar entidades complejas (por ejemplo: un auto, un usuario, una factura).
- Para facilitar el mantenimiento y la ampliación del código.

**Analogía:**

Piensa en una clase como un plano para construir casas. El plano define cómo será la casa (puertas, ventanas, habitaciones), pero cada casa construida a partir de ese plano puede tener detalles propios (color, dueño, dirección). Cada casa es un objeto (instancia) de la clase "Casa".

**Sintaxis básica:**

```python
class NombreDeLaClase:
	def __init__(self, atributo1, atributo2):
		self.atributo1 = atributo1
		self.atributo2 = atributo2

	def metodo(self):
		# Código del método
		pass
```

**Ejemplo paso a paso:**

```python
# Definimos la clase Persona
class Persona:
	def __init__(self, nombre, edad):  # Método especial para crear la persona / constructor
		self.nombre = nombre            # Guardamos el nombre
		self.edad = edad                # Guardamos la edad

	def saludar(self):                 # Método para saludar
		print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

# Creamos una persona (objeto/instancia) llamando la Classe y passando los atributos
p1 = Persona("Caty", 25)
# Usamos el método saludar
p1.saludar()  # Salida: Hola, mi nombre es Ana y tengo 25 años.
```

**¿Qué es `self`?**

En Python, `self` es una palabra que se usa dentro de las clases para referirse al propio objeto que se está creando o usando. Es como decir "yo mismo" dentro de la clase. Gracias a `self`, cada objeto puede tener sus propios datos y métodos.

Por ejemplo, cuando escribimos `self.nombre`, estamos accediendo al atributo `nombre` del objeto actual. Es obligatorio poner `self` como primer parámetro en los métodos de la clase.

**Ejemplo sencillo:**

```python
class Ejemplo:
	def mostrar(self):
		print("Este objeto es:", self)

e = Ejemplo()
e.mostrar()  # Muestra la dirección en memoria del objeto 'e'
```

**Resumen:**

- `self` permite que cada objeto tenga sus propios datos.
- Es necesario en todos los métodos de instancia.
- No es una palabra reservada, pero es una convención universal en Python.

**Buenas prácticas:**

- El nombre de la clase debe empezar con mayúscula.
- Los métodos y atributos suelen ir en minúscula y con guiones bajos si tienen varias palabras.
- Usa clases cuando necesites agrupar datos y comportamientos relacionados.

**Advertencia común:**

No olvides poner `self` como primer parámetro en los métodos de la clase. `self` representa al propio objeto.

**Enlaces a documentación:**

[Clases en Python](https://docs.python.org/es/3/tutorial/classes.html): Explica cómo crear y usar clases, atributos, métodos, herencia y conceptos fundamentales de la programación orientada a objetos en Python. Incluye ejemplos y buenas prácticas.
