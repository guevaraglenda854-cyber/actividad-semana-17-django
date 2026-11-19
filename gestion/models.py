from django.db import models


class Dueno(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()

    def __str__(self):
        return self.nombre


class Mascota(models.Model):
    dueno = models.ForeignKey(Dueno, on_delete=models.CASCADE, related_name="mascotas")
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)
    edad = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.nombre} ({self.especie})"


class Consulta(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name="consultas")
    motivo = models.CharField(max_length=150)
    fecha = models.DateField()
    costo = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.mascota.nombre} - {self.motivo}"