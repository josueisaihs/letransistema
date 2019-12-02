from django import forms
from django.core.exceptions import NON_FIELD_ERRORS
from .models import *
from django.utils.translation import gettext_lazy as _

__author__ = "Josue Isai Hernandez Sanchez"
__email__ = "josueisaihs@gmail.com"


class TeacherPersonalInformationForm(forms.ModelForm):
    class Meta:
        model = TeacherPersonalInformation

        fields = ["name", "lastname", "gender", "numberidentification", "nacionality", "pasaport", "street", "city", "state",
                    "cellphone", "phone", "email", "image", "degree", "title"]

        widgets = {
            "name": forms.TextInput(attrs={
                'class': 'w3-input  w3-border w3-validate w3-round es-shadow',
                'placeholder': 'José María',
                'autocomplete': 'off',
            }),
            "lastname": forms.TextInput(attrs={
                'class': 'w3-input  w3-border w3-validate w3-round es-shadow',
                'placeholder': 'Pérez Pérez',
                'autocomplete': 'off',
            }),
            "numberidentification": forms.TextInput(attrs={
                'class': 'w3-input w3-border  w3-border w3-validate w3-round es-shadow',
                'placeholder': 'Número de Carnet',
                'pattern': '[0-9]{11}',
                'minlength': 11,
                'maxlength': 11,
                'autocomplete': 'off',
            }),
            "gender": forms.Select(attrs={
                                    'class': 'w3-select w3-border w3-validate w3-round es-shadow'
            }),
            "street": forms.TextInput(attrs={
                'class': 'w3-input  w3-border w3-validate w3-round es-shadow',
                'placeholder': '23 Nº 328 entre L y M',
                'autocomplete': 'off',
            }),
            "city": forms.TextInput(attrs={
                'class': 'w3-input  w3-border w3-validate w3-round es-shadow',
                'placeholder': 'Plaza de la Revolución',
                'autocomplete': 'off',
            }),
            "state": forms.TextInput(attrs={
                'class': 'w3-input w3-border w3-validate w3-round es-shadow',
                'placeholder': 'La Habana',
                'value': 'La Habana',
                'autocomplete': 'off',
            }),
            "cellphone": forms.TextInput(attrs={
                'class': 'w3-input w3-border w3-validate w3-round es-shadow',
                'type': 'phone',
                'placeholder': '53891457',
                'autocomplete': 'off',
            }),
            "phone": forms.TextInput(attrs={
                'class': 'w3-input w3-border w3-validate w3-round es-shadow',
                'type': 'phone',
                'placeholder': '77662418',
                'autocomplete': 'off',
            }),
            "email": forms.EmailInput(attrs={
                'class': 'w3-input w3-border w3-validate w3-round es-shadow',
                'type': 'email',
                'placeholder': 'joseperezperez@example.com',
                'autocomplete': 'off',
            }),
            "image": forms.FileInput(attrs={
                'accept': 'image/*'
            }),
            "nacionality": forms.TextInput(attrs={
                'class': 'w3-input w3-border w3-validate w3-round es-shadow',
                'placeholder': 'cubana',
                'autocomplete': 'off',
            }),
            "pasaport": forms.TextInput(attrs={
                'class': 'w3-input w3-border w3-validate w3-round es-shadow',
                'placeholder': 'Número de Pasaporte',
                'autocomplete': 'off',
            },),
            "degree": forms.Select(attrs={
                                    'class': 'w3-select w3-border w3-validate w3-round es-shadow'
            }),
            "title": forms.TextInput(attrs={
                'class': 'w3-input w3-border w3-validate w3-round es-shadow',
                'placeholder': 'Título del Profesor',
                'autocomplete': 'off',
            })
        }

        labels = {
            "name": _("Nombre"),
            "lastname": _("Apellidos"),
            "gender": _("Género"),
            "numberidentification": _("CI"),
            "street": _("Calle"),
            "city": _("Municipio"),
            "state": _("Provincia"),
            "cellphone": _("Móvil"),
            "phone": _("Teléfono"),
            "email": _("E-mail"),
            "image": _("Foto Perfil"),
            "nacionality": _("Nacionalidad"),
            "pasaport": _("Pasaporte"),
            "degree": _("Grado Científico"),
            "title": _("Título"),
        }

        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "Este profesor ya existe.",
            }
        }
# <> fin TeacherPersonalInformationForm


class StudentPersonalInformationForm(forms.ModelForm):
    class Meta:
        model = StudentPersonalInformation

        fields = ["name", "lastname", "gender", "numberidentification", "nacionality", "street", "city", "state",
                    "cellphone", "phone", "email", "image", "degree", "title", "ocupation"]

        widgets = {
            "name": forms.TextInput(attrs={
                'class': 'w3-input  w3-border w3-validate w3-round es-shadow',
                'placeholder': 'José María',
                'autocomplete': "off",
            }),
            "lastname": forms.TextInput(attrs={
                'class': 'w3-input  w3-border w3-validate w3-round es-shadow',
                'placeholder': 'Pérez Pérez',
                'autocomplete': "off",
            }),
            "numberidentification": forms.TextInput(attrs={
                'class': 'w3-input w3-border  w3-border w3-validate w3-round es-shadow',
                'placeholder': 'Número de Carnet',
                'pattern': '[0-9]{11}',
                'minlength': 11,
                'maxlength': 11,
                'autocomplete': "off",
            }),
            "gender": forms.Select(attrs={
                                    'class': 'w3-select w3-border w3-validate w3-round es-shadow'
            }),
            "street": forms.TextInput(attrs={
                'class': 'w3-input  w3-border w3-validate w3-round es-shadow',
                'placeholder': '23 Nº 328 entre L y M',
                'autocomplete': "off",
            }),
            "city": forms.TextInput(attrs={
                'class': 'w3-input  w3-border w3-validate w3-round es-shadow',
                'placeholder': 'Plaza de la Revolución',
                'autocomplete': "off",
            }),
            "state": forms.TextInput(attrs={
                'class': 'w3-input w3-border w3-validate w3-round es-shadow',
                'placeholder': 'La Habana',
                'value': 'La Habana',
                'autocomplete': "off",
            }),
            "cellphone": forms.TextInput(attrs={
                'class': 'w3-input w3-border w3-validate w3-round es-shadow',
                'type': 'phone',
                'placeholder': '53891457',
                'autocomplete': "off",
            }),
            "phone": forms.TextInput(attrs={
                'class': 'w3-input w3-border w3-validate w3-round es-shadow',
                'type': 'phone',
                'placeholder': '77662418',
                'autocomplete': "off",
            }),
            "email": forms.EmailInput(attrs={
                'class': 'w3-input w3-border w3-validate w3-round es-shadow',
                'type': 'email',
                'placeholder': 'joseperezperez@example.com',
                'autocomplete': "off",
            }),
            "image": forms.FileInput(attrs={
                'accept': 'image/*'
            }),
            "nacionality": forms.TextInput(attrs={
                'class': 'w3-input w3-border w3-validate w3-round es-shadow',
                'placeholder': 'cubana',
                'autocomplete': "off",
            }),
            "degree": forms.Select(attrs={
                                    'class': 'w3-select w3-border w3-validate w3-round es-shadow'
            }),
            "title": forms.TextInput(attrs={
                'class': 'w3-input w3-border w3-validate w3-round es-shadow',
                'placeholder': 'Título del Estudiante',
                'autocomplete': "off",
            }),
            "ocupation": forms.Select(attrs={
                'class': 'w3-select w3-border w3-validate w3-round es-shadow'
            }),
        }

        labels = {
            "name": _("Nombre"),
            "lastname": _("Apellidos"),
            "gender": _("Género"),
            "numberidentification": _("CI"),
            "street": _("Calle"),
            "city": _("Municipio"),
            "state": _("Provincia"),
            "cellphone": _("Móvil"),
            "phone": _("Teléfono"),
            "email": _("E-mail"),
            "image": _("Foto Perfil"),
            "nacionality": _("Nacionalidad"),
            "degree": _("Grado Científico"),
            "title": _("Título"),
            "ocupation": _("Ocupación")
        }

        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "Este estudiante ya existe.",
            }
        }
# <> fin StudentPersonalInformationForm


class CourseInformationForm(forms.ModelForm):
    class Meta:
        model = CourseInformation
        fields = '__all__'
        widgets = {
            "name": forms.TextInput(attrs={
                'class': 'w3-input  w3-border w3-validate w3-round es-shadow',
                'placeholder': 'Ingles Introductorio',
                'required': True,
                'autocomplete': "off",
            }),
            "image": forms.FileInput(attrs={
                'accept': 'image/*'
            }),
            "capacity": forms.TextInput(attrs={
                'class': 'w3-input w3-border w3-validate w3-round es-shadow',
                'type': 'number',
                'min': '5',
                'max': '20',
                'step': '1',
                'required': True,
                'autocomplete': "off",
            }),
            "openregistre": forms.DateInput(attrs={
                "class": "w3-input w3-border w3-validate w3-round es-shadow",
                'required': False,
                'autocomplete': "off",
            }),
            "deadline": forms.DateInput(attrs={
                "class": "w3-input w3-border w3-validate w3-round es-shadow",
                'required': False,
                'autocomplete': "off",
            }),
            "description": forms.Textarea(attrs={
                "class": "w3-input w3-border w3-validate w3-round es-shadow",
                "required": False,
                "cols": "10",
                "rows": "3",
                'autocomplete': "off",
            }),
            "yearMin": forms.TextInput(attrs={
                'class': 'w3-input w3-border w3-validate w3-round es-shadow',
                'type': 'number',
                'min': '5',
                'max': '70',
                'step': '1',
                'required': True,
                'autocomplete': "off",
            }),
            "yearMax": forms.TextInput(attrs={
                'class': 'w3-input w3-border w3-validate w3-round es-shadow',
                'type': 'number',
                'min': '10',
                'max': '90',
                'step': '1',
                'required': True,
                'autocomplete': "off",
            }),
        }

        labels = {
            "name": _("Nombre"),
            "capacity": _("Capacidad"),
            "deadline": _("Cierre"),
            "openregistre": _("Inicio"),
            "description": _("Descripcion"),
            "yearMin": _("Edad Minima"),
            "yearMax": _("Edad Maxima")
        }

        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "Este curso ya existe.",
            }
        }
# <> fin CourseInformationForm


class GroupInformationForm(forms.ModelForm):
    class Meta:
        model = GroupInformation
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={
                'class': 'w3-input  w3-border w3-validate w3-round es-shadow',
                'placeholder': 'Grupo 1',
                'required': True,
                'autocomplete': "off",
            }),
            "course": forms.Select(attrs={
                'class': 'w3-select w3-hide'
            }),
            "teacher": forms.Select(attrs={
                'class': 'w3-select w3-hide',
                'required': True
            }),
            "edition":  forms.TextInput(attrs={
                'class': 'w3-input  w3-border w3-validate w3-round es-shadow',
                'placeholder': '2019-2020',
                'required': True,
                'autocomplete': "off",
            }),
        }

        labels = {
            "name": _("Nombre"),
            "course": _("Curso"),
            "teacher": _("Profesor"),
            "edition": _("Edicion")
        }

        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "Este curso ya existe.",
            }
        }
# <> fin GroupInformationForm


class CandidateSelectCourseForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = "__all__"
        widgets = {
            'course': forms.Select(
                attrs={
                    'class': 'w3-select',
                    'required': True
                }
            ),
            'student': forms.Select(
                attrs={
                    'class': 'w3-select',
                    'required': True
                }
            )
        }

        labels = {
            "student": _("Estudiante"),
            "course": _("Curso"),
        }
# <> fin CandidateSelectCurseForm


class StudentCandidateForm(forms.Form):
    studentCI = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'w3-text-black w3-input  w3-border w3-validate w3-round es-shadow',
                'required': True,
                'placeholder': 'Escribalo Aqui',
                'pattern': '[0-9]{11}',
                'minlength': 11,
                'maxlength': 11,
                'onkeyup': 'nextValidate(this)',
                'autocomplete': "off",
            })
    )
# <> fin StudentCandidateForm
