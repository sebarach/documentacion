# Python 
---

-  **Excepciones**

```python
try:
    result = 2 / 0
except ZeroDivisionError:
    print("No se puede dividir por 0")
except:
    print("Pueden haber varios tipos de error")
else:
    print("Ha ocurrido un error generico")
finally:
    print("Fin de la ejecucion")
```

```python
try:
    raise Exception("HA ocurrido un error")
except Exception as error:
    print(error)
```


-  **Anotations**

1-Se le puede indicar a la funcion que va a recibir un entero y va a devolver un entero
```python
def AumentarNumero(numero : int) -> int:
    return numero + 1
```
2-Tambien a variables
```python
contador : int = 0
```



-  **map()** **filter()** **reduce()**

- CTR + ALT + S => ABRE CONFIGURACION DE PYCHARM

1- Map() = Crea otro objeto a partir de una coleccion
```python
numeros = [2,4,8,10,11]
resultado = map(lambda numero : numero * 2,numeros) #primer agumento es una accion , en este caso una funcion y despues la coleccion
print(list(resultado))
```

2- Filter() => Crea otro objeto a partir de una condicion(funcion) que retorna true o false y una coleccion
```python
numeros = [2,4,8,10,11,13,15,16,17,20]
esPar = lambda numero : numero % 2 == 0
reusltado = filter(esPar, numeros) # [2, 4, 8, 10, 16, 20]
print(list(reusltado))
```

3- Reduce() => Permite ejecutar una funcion de 2 argumentos para un iterable, en el ejemplo se suman los elemtnos de la posicion 2 = [1]
```python
from functools import reduce

gastos = [
    ('ARREGLOAUTO', 150),
    ('ComidaDiaria', 350)
]
resultado = reduce(lambda a, b : a[1] + b[1], gastos)
print(resultado) # 500
```

-  **lambaExpresion** **Anonimous function**

```python
duplicador = lambda numero : numero * numero
suma = lambda a,b : a + b

print(duplicador(6)) #36
print(suma(6,6)) #12
```


-  **Modules**

1-archivo 1
```python
def saludar():
    print("Hola desde otro archivo")
```
2-archivo 2
```python
from utils import saludar

saludar() #Hola desde otro archivo
```

-  **Clases y herencia**

```python


class Animal():
  def caminar(self):
    print("Caminando")


class Perro(Animal): #en el argumento de la clase se le pasa otra clase para heredad sus atributos y metodos segun corresponda
  def __init__(self,nombre,edad): #self hace referencia a la instancia , self no es una palabra reservada solo es una convencion
    self.nombre = nombre
    self.edad = edad

  def ladrar:
    print("wowwww")


agustin = Perro("agustin",14)
agustin.ladrar()
agustin.caminar()

```




-  **Loops**

```python

contador = 0
coleccion = ["seba","diego","cristobal","felipe"]

while contador < 4:
    print(contador) # 1 2 3 4
    contador=contador+1

for variableNueva in coleccion:
    print(variableNueva + " Sepulveda") # todos los nombers mas el sepulveda

for listaNueva in range(15):
    print(listaNueva)# range crea una lista del 0 al 15

for index,listaNueva in enumerate(coleccion):
    print(index,listaNueva)# enumarete devuelve el index y el valor del arreglo 0 "seba" , 1 "diego" , etc ...

```


-  **Functions**

```python
def saludar(nombre ="Amigo"):
    return print(f"Saludos {nombre}")

saludar("Seba")
saludar()

```



-  **Instalar dependencias**

```python
pip install pyenv #instalar ambientes virtuales
pip install flask #flask framework y servidor web
```

-  **Ejecutar flask**

```python
import sys
from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def hello_world():
    titulo ='Titulo Personalizado';
    return render_template('index.html', titulo=titulo);

if __name__ == '__main__':
    app.run()


```
- En el HTML se puede recibir la variable asi

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
    <meta charset="UTF-8">
    {% if titulo %}
    <title>{{titulo}}</title>
    {% else %}
    <title>Sin titulo</title>
    {% endif%}

</head>
<body>
<form class="container-fluid h-100" action="/" method="POST">
  <div class="form-group">
    <label for="titulo">Ejemplo</label>
    <input type="text" class="form-control" id="titulo" name="titulo" placeholder="">
  </div>
  <button type="submit" class="btn btn-success">Submit</button>
</form>
</body>
</html>
```


-  **Variables y funciones**
- Identacion es primordial en python


```python
def saludar():
  return "Saludos" 

def saludarConArgumento(nombre):
  return "Saludos",nombre
  
respuesta = saludar()

print(respuesta)
print(saludarConArgumento("Sebastian"))
```


-  **Dictionary**
- Sirve para crear pares de llaves valor

```python
result = {"nombre":"Sebastian" , "edad":26}
print(result.get("nombre")) #sebastian
print(result.get("color","Sin color disponible")) #si no encuentra la llave imprime el valor por defecto
del result # elimina objetos, listas diccionarios etc
```


-  **Importar Libreria Random y Template string en Python**
- Sirve para crear pares de llaves valor

```python
import random

def ObtenerOpciones():
  opcionJugador = input("Eliga una opcion (Piedra,Papel,Tijera)")
  opciones = ["piedra","papel","tijera"]
  opcionComputador = random.choice(opciones)
  resultado = VerificarGanador(opcionJugador,opcionComputador)
  return resultado


def VerificarGanador(jugador,computador):
  print(f"Jugador: {jugador} --- Computador: {computador}")
  if (jugador==computador):
    return "Es un Empate"
  elif(jugador == "piedra" and computador == "tijera"):
    return "Jugador Gana"
  elif(jugador == "papel" and computador == "piedra"):
    return "Jugador Gana"
  elif(jugador == "tijera" and computador == "papel"):
    return "Jugador Gana"
  elif(jugador !="papel" and jugador !="piedra" and jugador != "tijera"):
    return "Debe ingresar una opcion valida"
  else:
    return "Computador gana"
      
print(ObtenerOpciones())
```


-  **Comentario**
```python
# esto es un comentario en python
```

-  **Verificar tipo de variable**
```python
print(type("asd")==str) # true
print(isinstance("asd",str))# true
print(isinstance(3,float))# false
print(isinstance(float(3),float))#true, se usa el casteo implicito
```

-  **String Method**
```python
print("sebastian".upper()) # SEBASTIAN
print("sebastian".title()) # Sebastian
print("Seba" in "Sebastian") # in es como el contains
```

-  **any**
```python
# Devuelve true si algun valor del enumerable es verdadero
libro1 = True
libro2 = False

existeLibro = any([libro1,libro2])
print(existeLibro) # true
```

-  **Enum**
```python
class Estado(Enum):
  INACTIVO =0 #son constantes que no cambian, ya que en python no se pueden declarar constantes
  ACTIVO= 1

print(Estado.ACTIVO.value) #1
print(Estado.ACTIVO) #Estado.ACTIVO
print(Estado(1)) #Estado.ACTIVO
```

-  **Listas**
```python
lista = ["agustin","toby",1,False]
print(lista[0]) #agustin
print("agustin" in lista) #true
lista.append("Seba") #agrega un nuevo elemento a la lista
print(lista[-1]) # devuelve el ultimo en la lista
print(lista.pop()) # elimina el ultimo elemnto ded la lista y lo muestra
```

-  **Tuples**
1- Las tuplas no se pueden modificar
```python
nombres = ("sebas", "diego")
print(nombres[0]) #sebas
print(nombres.index("sebas"))#0 devuelve el index
```

-  **Sets**
```python
setNombres1 = {"seba","diego"}
setNombres2 = {"seba","cristobal"}

intersect = setNombres1 & setNombres2 #chekea las similutdes
print(intersect) #seba

unir = setNombres1 | setNombres2
print(unir) # {'cristobal', 'seba', 'diego'}
print(list(unir)) # ['diego', 'cristobal', 'seba']
```
