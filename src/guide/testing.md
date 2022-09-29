# Tipos de prueba 

---

```C#
        [TestMethod]
        public void TestSesionesPorSeccionId()
        {
            long seccionId = 81965;

            List<Planificacion_SesionViewModel> data = BusinessPlanificacion.GetSesiones(seccionId);
            Assert.IsNotNull(data);
        }

        [TestMethod]
        public void TestCrearSesion()
        {
            Planificacion_SesionViewModel sesion = new Planificacion_SesionViewModel()
            {
            SeccionId = 81965,
            HorarioSeccionId = 146443,
            FechaHoraInicio = new DateTime(2022,07,08,15,00,00),
            FechaHoraTermino = new DateTime(2022,07,08,19,30,00)
            };

            long Id = DataPlanificacion.CrearSesion(sesion,1);
            Assert.IsTrue(Id > 0);
        }
```

