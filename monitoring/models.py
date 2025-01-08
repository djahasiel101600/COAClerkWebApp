from django.db import models

# cols: IAR
# no, iar_number, iar_date, supplier, particulars, amount, date_received_in_coa, delay_duration_in_days, date_encoded, remarks

# cols: PO
# no, po_number, supplier_name, amount, particulars, date_of_delivery, delivery_term, po_govt_contract_date, date_signed_by_the_supplier, date_received_in_coa, number_of_days_delayed, remarks

# Create your models here.
class IARRecords(models.Model):
    no = models.IntegerField()
    iar_number = models.CharField(max_length=16)
    iar_date = models.DateField()
    supplier = models.CharField(max_length=255)
    particulars = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_received_in_coa = models.DateField ()
    delay_duration_in_days = models.IntegerField()
    date_encoded = models.DateField()
    remarks = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class PORecords(models.Model):
    no = models.IntegerField()
    po_number = models.CharField(max_length=16)
    supplier_name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    particulars = models.CharField(max_length=255)
    date_of_delivery = models.DateField()
    delivery_term = models.CharField(max_length=50)
    po_govt_contract_date = models.DateField()
    date_signed_by_the_supplier = models.DateField()
    date_received_in_coa = models.DateField()
    number_of_days_delayed = models.IntegerField()
    remarks = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    