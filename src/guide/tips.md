# C# Varios


**Listas y Colecciones**

1- Addrange
-Permite agregar colecciones a una lista

```csharp
List<int> ListaNumeros = new List<int> {1,2,3,4,5,6,7,8,9,10};
List<int> ListaNumerosTest = new List<int>();

ListaNumerosTest.AddRange(ListaNumeros);


//Foreach shorthand
List<int> MultiplicadorX2 = new List<int>();
ListaNumerosTest.ForEach(x => MultiplicadorX2.Add(x * 2));


List<Usuario> USERS = new List<Usuario>();
USERS.Add(new Usuario() { Nombre = "Sebastian", Edad = 32 });
USERS.Add(new Usuario() { Nombre = "Diego", Edad = 31 });
USERS.Add(new Usuario() { Nombre = "Cristobal", Edad = 23 });
USERS.Add(new Usuario() { Nombre = "Felipe", Edad = 35 });


USERS.ForEach(x => Console.WriteLine(x.Nombre));
```



- Libreria De Clases
 
 . Los archivos dll son el codigo complilado(Con el build listo)



- Cadena de conexion para sql server autenticacion de windows

-  **Resumen API NET 6**

```js
{
  "Logging": {
    "LogLevel": {
      "Default": "Information",
      "Microsoft.AspNetCore": "Warning"
    }
  },
  "AllowedHosts": "*",
  "ConnectionStrings": {
    "SQLMS": "Data Source=NB-PR-SSEPULVED\\SQLEXPRESS;Initial Catalog=Autos;Integrated Security=True"
  }
}
```


- SP SQL TEMPATE

```SQL
USE [OmegaDB]
GO
/****** Object:  StoredProcedure [dbo].[spAsistencia_Crea_Sesion]    Script Date: 26-10-2022 14:11:29 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

-- =============================================
-- Author:		
-- Create date: 
-- Description:	
-- =============================================

ALTER procedure [dbo].[spAsistencia_Crea_Sesion]
(
	@variablesEntrada int
)
as 
declare 
	@masVariables		bigint,
begin 
	begin try

			select 

			from 

			where 
				

	end try
	begin catch
		print error_message()
	

		if @@trancount > 0
			begin 
				
			end 
	end catch
end 
```

