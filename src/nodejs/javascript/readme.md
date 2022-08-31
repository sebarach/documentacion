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

```javascript
const persona = {
  nombre:'seba',
  edad : 31
}
const {nombre} = persona;
console.log(nombre);//seba
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