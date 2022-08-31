from django.urls import path
from django.urls import re_path as url
from . import views

urlpatterns = [
    path('suppliers/', views.SupplierListView.as_view(), name='suppliers-list'),
    path('suppliers/new', views.SupplierCreateView.as_view(), name='new-supplier'),
    path('suppliers/<pk>/edit', views.SupplierUpdateView.as_view(), name='edit-supplier'),
    path('suppliers/<pk>/delete', views.SupplierDeleteView.as_view(), name='delete-supplier'),
    path('suppliers/<name>', views.SupplierView.as_view(), name='supplier'),

    path('purchases/', views.PurchaseView.as_view(), name='purchases-list'), 
    path('purchases/new', views.SelectSupplierView.as_view(), name='select-supplier'), 
    path('purchases/new/<pk>', views.PurchaseCreateView.as_view(), name='new-purchase'),    
    path('purchases/<pk>/delete', views.PurchaseDeleteView.as_view(), name='delete-purchase'),
    
    path('sales/', views.SaleView.as_view(), name='sales-list'),
    path('sales/new', views.SaleCreateView.as_view(), name='new-sale'),
    
    
    path('expenses/', views.ExpensesListView.as_view(), name='expenses-list'),
    path('expenses/new', views.ExpensesCreateView, name='new-expenses'),
    path('credit/', views.CreditListView.as_view(), name='credit-list'),
    path('credit/new', views.CreditCreateView, name='new-credit'),
    path('labours/', views.LaboursListView.as_view(), name='labours-list'),
    path('labours/new', views.LaboursCreateView, name='new-labours'),

    path('employee/', views.EmployeeListView.as_view(), name='employee-list'),
    path('employee/new', views.EmployeeCreateView, name='new-employee'),
    path('sleepingpartner/', views.SleepingPartnerView, name='sleepingpartner-list'),
    path('sleepingpartner/new', views.SleepingPartnerCreateView, name='new-sleepingpartner'),
    path('sales/<pk>/delete', views.SaleDeleteView.as_view(), name='delete-sale'),

    path("purchases/<billno>", views.PurchaseBillView.as_view(), name="purchase-bill"),
    path("sales/<billno>", views.SaleBillView.as_view(), name="sale-bill"),
]