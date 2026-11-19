from django import forms
from .models import Dueno, Mascota, Consulta


class DuenoForm(forms.ModelForm):
    class Meta:
        model = Dueno
        fields = ["nombre", "telefono", "correo"]


class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ["dueno", "nombre", "especie", "edad"]


class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ["mascota", "motivo", "fecha", "costo"]
        widgets = {
            "fecha": forms.DateInput(attrs={"type": "date"}),
        }