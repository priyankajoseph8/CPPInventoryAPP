# file: custom_utils.py

from transactions.models import PurchaseBill, Supplier

def create_purchase_bill(supplier_pk):
    supplier = Supplier.objects.get(pk=supplier_pk)
    bill = PurchaseBill.objects.create(supplier=supplier)
    return bill
