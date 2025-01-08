from django import forms
from .models import IARRecords

class IARRecordsForm(forms.ModelForm):
    class Meta:
        model = IARRecords
        fields = [
            'no',
            'iar_number',
            'iar_date',
            'supplier',
            'particulars',
            'amount',
            'date_received_in_coa',
            'delay_duration_in_days',
            'date_encoded',
            'remarks',
        ]

        labels = {
            'no': 'No',
            'iar_number': 'IAR Number',
            'iar_date': 'IAR Date',
            'supplier': 'Supplier',
            'particulars': 'Particualrs',
            'amount': 'Amount',
            'date_received_in_coa': 'Date Received (COA)',
            'delay_duration_in_days': 'Delay Duration (Days)',
            'date_encoded': 'Date Encoded',
            'remarks': 'Remarks',
        }

        widgets = {
            'iar_date': forms.DateInput(attrs={'type':'date'}),
            'date_received_in_coa': forms.DateInput(attrs={'type':'date'}),
            'date_encoded': forms.DateInput(attrs={'type':'date'}),
        }