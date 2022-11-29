# Introduccion

- ### Crear aplicacion de consola NET  CORE 6 VS CODE

``` .net cli
dotnet new console --framework net6.0
```

- ### Debugear en VS Code
``` .net cli
Instalar en la paleta de comandos 
.net generated assets for build and debug
Se crea la pestana para debugear al lado izquierdo
```


### Structs de registro
- Puede declarar los registros de tipo de valor mediante las declaraciones record struct o readonly record struct. Ahora puede aclarar que un elemento record es un tipo de referencia con la declaración record class.

### Mejoras de tipos de estructura
###### C# 10 presenta las mejoras siguientes relacionadas con los tipos de estructura:

- Puede declarar un constructor sin parámetros de instancia en un tipo de estructura e inicializar un campo o propiedad de instancia en su declaración. Para obtener más información, vea la sección Constructores sin parámetros e inicializadores de campo del artículo Tipos de estructura.
- Un operando izquierdo de la expresión with puede ser de cualquier tipo de estructura o un tipo anónimo (de referencia).