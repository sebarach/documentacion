# Retornos de Endpoints

---

```C#
        // GET: api/<TestController>
        [HttpGet]
        public ActionResult<IEnumerable<Blog>> Get()
        {
            var blogs = blogRepository.GetBlogs();
            return Ok(blogs);
        }
```
-


```C#

//netwosonft json
        [HttpPost]
        public JsonResult Secciones(string seccionId)
        {
            String jsonResult = String.Empty;

            var lstSeccion = DataEncuestaDocente.ObtieneSeccionEncuestaDocente(seccionId);

            try
            {
                jsonResult = JsonConvert.SerializeObject(new { status = "ok", data = lstSeccion });
            }
            catch (Exception ex)
            {
                jsonResult = JsonConvert.SerializeObject(new
                {
                    status = "error",
                    data = "Error al Intentar Obtener la lista - " + ex.Message
                });
            }
            return Json(jsonResult, JsonRequestBehavior.DenyGet);
        }
```
