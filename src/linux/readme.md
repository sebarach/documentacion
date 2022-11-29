# Linux Fundamentals
---

## touch 

-El comando permite crear y editar archivos
```shell
touch ejemplo.txt
```

## rm 

-El comando permite eliminar archivos
```shell
rm ejemplo.txt
```

## cp 

-El comando permite copiar archivos o carpertas
```shell
cp ejemplo.txt ejemploCopia.txt
```


## mv 

-El comando permite mover o renombrar un archivo
```shell
mv indexCopia.js indexCopiaEditado.js
mv index.js test
```

## head 

-El comando permite ver las primeras 10 filas de un archivo
```shell
head nombreArhcivo.md
```

## tail 

-El comando permite ver las ultimas 10 filas de un archivo
```shell
tail nombreArhcivo.md
```

## cat 

-El comando permite mostrar todo el contenido del archivo, concatena contenidos de archivo y puede insertarlo en un nuevo archivo
```shell
cat nombreArhcivo.md
cat nombreArchivo.md > prueba.txt
```

## echo 

-El comando permite imprimir en pantalla o escribir en un archivo
```shell
echo hola mundo
echo cualquier texto > nombreArhcivo.md
```

### apt upgrade
- upgrade actualiza los paquetes instalados a la ultima version

```shell
sudp apt upgrade
```

### apt update
- Update refresca el cache de los repositorios de ubuntu y te indica que package pueden actualizarse

```shell
sudp apt update
```


### rn
- El siguiente elimina  un archivo

```shell
rm nombrearchivo.txt
```

### touch
- El siguiente ejemplo crear un archivo

```shell
touch nombrearchivo.txt
```

### rmdir
- El siguiente ejemplo elimina un directorio

```shell
rmdir nombreCarpeta
```

### mkdir
- El siguiente ejemplo crea un directorio
```shell
mkdir nombreCarpeta
```

### pwd
- El siguiente ejemplo es para ver el path o el working directory donde se esta actualmente
```shell
pwd
```

### ls
- lista todos los archivos del directorio actual [-a incluye los archivos ocultos]
- [-a incluye los archivos ocultos]
- [-l muestra mas detalles]
```shell
ls -a
ls -l
```

### man
- man es para ver el manual del comando ll
```shell
man mkdir
```