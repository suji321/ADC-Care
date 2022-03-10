
import django_filters
from clinic.models import*

class BillFilter(django_filters.FilterSet):
    class Meta:
        model=BillInfo
        fields='__all__'
        exclude=['patient']

class MedhisFilter(django_filters.FilterSet):
    class Meta:
        model=MedicalHistory
        fields='__all__'
        exclude=['patient']

class SchFilter(django_filters.FilterSet):
    class Meta:
        model=Schedule
        fields='__all__'
        exclude=['patient']

class PrescriptionFilter(django_filters.FilterSet):
    class Meta:
        model=Prescription
        fields='__all__'
        exclude=['patient']
