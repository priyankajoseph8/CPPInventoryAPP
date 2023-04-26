from transactions.models import Supplier

def get_active_suppliers():
    return Supplier.objects.filter(is_deleted=False)