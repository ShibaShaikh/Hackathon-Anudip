from django import forms
from .models import VpRmAllocation, RmCenterQuarterAllocation


class VpRmAllocationForm(forms.ModelForm):
    class Meta:
        model = VpRmAllocation
        fields = ['project', 'vertex', 'rm_user', 'target']

class RmCenterQuarterForm(forms.ModelForm):
    class Meta:
        model = RmCenterQuarterAllocation
        fields = ['project', 'vertex', 'center', 'quarter', 'target']