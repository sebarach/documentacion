# Javascript Basic 

---
-  **Variables**

```javascript
var = dato; // no usar var
const = dato// variable que no va a cambiar
let = dato; // esta variable puede cambiarse o modificarse en el tiempo
```

-  **Arrow Function**

```javascript
const MyFUncion = () => {console.log("Hello World !")};
const MyFUncion2 = (a,b) => {console.log(`La suma es ${1 + 3}`)};
MyFUncion();
MyFUncion2();
```

-  **Operador Ternario**

```javascript
let name = 'sebastian';
let age = 31;
const result = age > 30 ? `Mayor de edad` : `Menor de edad`;
console.log(result); // Mayor de edad
```

-  **Destructuring**

1- Objetos

```javascript
const persona = {
    nombre:"sebastian",
    edad:35,
    titulos:{
        Profesion:"Ingeniero",
        Bobby:"Devops"
    }
}

const ImprimirPersona = ({nombre,edad,rango='Ing',titulos:{Profesion,Bobby}}) =>{
console.log(nombre,edad,rango,Profesion,Bobby);
}

```

2- Arreglos

```javascript
const cervezas = ['escudo','cristal','heienken'];
const [,c2] = cervezas;
console.log(c2)//cristal, con una coma le indico que la posision 1 no la quiero y me traiga la 2


const arreglos = () => [123,'asd']

const arr = arreglos(); 
console.log(arr)//[ 123, 'asd' ]1

const [numeros,letras] = arreglos();// se destructura por posision del arreglo
console.log(numeros,letras)//123 asd


```



-  **spread operator**

```javascript
const persona = {nombre:'seba',edad : 31}
let nombre = 'seba cambiado';
const persona2 = {...persona,nombre}//copia a persona pero le cambia el nombre
console.log(persona2);//nombre: "seba cambiado", edad: 31}
```

-  **map**

```javascript
//Crea otro arreglo apartir de un objeto o arreglo anterior
let arreglo = ["seba","diego","cristobla","felipe"];
let sample = arreglo.map((argumento) =>
{
return argumento + " Sepulveda";// se agrega sepulveda a cada argumento
})
```


-  **Template String**
```javascript
const nombre = 'Sebastian';
let apellido = 'sepulveda';
let a = 15;
let b = 10;

console.log(`${nombre} ${apellido}`); // Sebastian Sepulveda
console.log(`Suma de a y b es  : ${a+b}`); // 25
```



-  **Import y Export y funciones comunes de arreglo**
```javascript
//Suponiendo que este arreglo esta en otro archivo
 const heroes = [
    {
        id: 1,
        name: 'Batman',
        owner: 'DC'
    },
    {
        id: 2,
        name: 'Spiderman',
        owner: 'Marvel'
    },
    {
        id: 3,
        name: 'Superman',
        owner: 'DC'
    },
    {
        id: 4,
        name: 'Flash',
        owner: 'DC'
    },
    {
        id: 5,
        name: 'Wolverine',
        owner: 'Marvel'
    },
];

export const marcas = ['Marvel','DC'];

export default heroes; // si se quiere exportar otra variable, en el archivo que la recibe se debe destructurar



import heroes,{marcas} from  '../heroes' //ruta del archivo , puede ser con extension .js opcional

// find recibe una funcion como argumento (callback)
const obtenerHeroePorId = (id)=>{
  return heroes.find((heroes) => heroes.id === id ); 
console.log(obtenerHeroePorId(1));// { id: 1, name: 'Batman', owner: 'DC' }
}

// filter trae en un arreglo todo lo que se cumpla en el predicado
const obtenerHeroesPorDueno = (dueno) => heroes.filter((heroes) => heroes.owner === dueno);
console.log(obtenerHeroesPorDueno('Marvel'));// [{ id: 2, name: 'Spiderman', owner: 'Marvel' }, { id: 5, name: 'Wolverine', owner: 'Marvel' }]

```


-  **Fetch**
```javascript

// pequen app para mostrar un gif en el html basico

const API_KEY = 'hQQNQmsoqDdvATqAs5A8G9D7hiS5YVnI';
const respuesta = fetch(`https://api.giphy.com/v1/gifs/random?api_key=${API_KEY}`);

respuesta
        .then(resp=> resp.json())
        .then(({data}) => {
            const url  = data.images.original.url
            const imagen = document.createElement('img');
            imagen.src = url;

            document.body.appendChild(imagen);

        })
        .catch(console.warn);
```

-  **Async y await**
```javascript

// el await espera que se resuelva la promesa ysigue con su ejucion

const getImage = async() =>{
    const API_KEY = 'hQQNQmsoqDdvATqAs5A8G9D7hiS5YVnI';
    const respuesta = await fetch(`https://api.giphy.com/v1/gifs/random?api_key=${API_KEY}`);
    const {data} = await respuesta.json();
    return data;
};

```