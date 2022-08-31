from django.contrib import admin
from .models import (
    CreditBook,
    Employee,
    Expense,
    Labours,
    SleepingPartners,
    Supplier, 
    PurchaseBill, 
    PurchaseItem,
    PurchaseBillDetails, 
    SaleBill, 
    SaleItem,
    SaleBillDetails
)

admin.site.register(Supplier)
admin.site.register(PurchaseBill)
admin.site.register(PurchaseItem)
admin.site.register(PurchaseBillDetails)
admin.site.register(SaleBill)
admin.site.register(SaleItem)
admin.site.register(SaleBillDetails)
admin.site.register(Expense)
admin.site.register(Employee)
admin.site.register(SleepingPartners)

admin.site.register(Labours)
admin.site.register(CreditBook)