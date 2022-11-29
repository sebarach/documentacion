# Utils de Javascript y Jquery
---


## Ejemplos de ajax con jquery

```js

let obj = {};

obj.foo = "Sebastian";
obj.faa = "Diego";

    $.ajax({
        url: 'urlMetodo',
        type: 'POST',
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        async: false,
        data: JSON.stringify(obj),
        beforeSend: function () {

        },
        complete: function () {

        },
        error: function (jqXHR, status, error) {

        },
        success: function (data) {
            if (data != '') {
                
                } else {

                }
            }
    });

```


## Utils JS

```js
// Pintar hmtl
 function DrawTblResultado(nodoId, html) {
        nodoId.innerHTML += `
            <tr>
            <td>${html.sesion}</td>
            <td>${html.mensaje}, Revise las filas de la sesion Indicada</td>
            </tr>`;
    }


// block UI
    function blockUI() {
        jQuery.blockUI({
            message: '<h1> La carga del Excel podria tardar unos minutos, espere por favor ...</h1>',
            css: {
                border: 'none',
                padding: '15px',
                backgroundColor: '#000',
                '-webkit-border-radius': '10px',
                '-moz-border-radius': '10px',
                opacity: .5,
                color: '#fff',
                dislay: 'block!important'
            }
        });
    }

// desbloquear UI
    function unblockUI() {
        jQuery.unblockUI();
    }



// Sweet Alert

//Insertar en el HTML
<script src="https://cdn.jsdelivr.net/npm/sweetalert2@11.5.2/dist/sweetalert2.all.min.js" integrity="sha256-wLk4yXmqQvDv8x5C501KgoVtR2yHYUpOKspL/KpR+/8=" crossorigin="anonymous"></script>

    let MessageSweetAlert = (icon, title, text, timer = null, showConfirmButton = true) => {
        Swal.fire({
            icon: `${icon}`,
            title: `${title}`,
            text: `${text}`,
            timer: timer,
            showConfirmButton: showConfirmButton
        })
    };


// Agrandar Modal sweet Alert
<style>
    .swal2-popup {
        font-size: 2rem !important;
    }
</style>


// Eliminar Duplicados de un arreglo
function removeDuplicates(arr) {
    return arr.filter((item,
        index) => arr.indexOf(item) === index);
}

```


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