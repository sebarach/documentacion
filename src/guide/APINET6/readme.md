# Introduccion
---

-  **Resumen API NET 6**

- Inyectar dependencia y cadena de conexion
```csharp
var builder = WebApplication.CreateBuilder(args);

builder.Services.AddControllers();
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();


var SQL = new SqlConfiguration(builder.Configuration.GetConnectionString("SQLMS"));
builder.Services.AddSingleton(SQL);
builder.Services.AddScoped<IAutoRepositorio, AutoRepositorio>();


var app = builder.Build();
```

- IactionResult puede devolver codigos de respuesta http
```csharp
[HttpGet]
public async Task<IActionResult> ObtenerAutos()
{
return Ok(await _autoRepositorio.ObtenerTodos());
}

[HttpGet("{id}")]
public async Task<IActionResult> ObtenerAutosPorId(int id)
{
return Ok(await _autoRepositorio.ObtenerAuto(id));
}

```



