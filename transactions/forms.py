from django import forms
from django.forms import formset_factory
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
from inventory.models import Stock




class Sleepingpartnerform(forms.ModelForm):
    name= forms.CharField(max_length=100,
                           widget= forms.TextInput
                           (attrs={'class':'form-control',
				   'id':'some_id'}))
    mobile_number= forms.IntegerField(
                           widget= forms.TextInput
                           (attrs={'class':'form-control',
				   'id':'some_id'}))

    address=forms.CharField(max_length=100,
                           widget= forms.TextInput
                           (attrs={'class':'form-control',
				   'id':'some_id'}))
    investment= forms.IntegerField(
                           widget= forms.TextInput
                           (attrs={'class':'form-control',
				   'id':'some_id'}))
    PartnerPorfit= forms.IntegerField(
                           widget= forms.TextInput
                           (attrs={'class':'form-control',
				   'id':'some_id'}))
    
    CompanyPorfit= forms.IntegerField(
                           widget= forms.TextInput
                           (attrs={'class':'form-control',
				   'id':'some_id'}))
    paid= forms.BooleanField(
       
       )
                          
   

    class Meta:
        model=SleepingPartners
        fields=['name','mobile_number','address','investment','PartnerPorfit','CompanyPorfit','paid']


class Creditform(forms.ModelForm):
    supplier= forms.CharField()
    total= forms.IntegerField(
                           widget= forms.TextInput
                           (attrs={'class':'form-control',
				   'id':'some_id'}))

    paid=forms.IntegerField(
                           widget= forms.TextInput
                           (attrs={'class':'form-control',
				   'id':'some_id'}))
    remaing= forms.IntegerField(
                           widget= forms.TextInput
                           (attrs={'class':'form-control',
				   'id':'some_id'}))
    
    class Meta:
        model=CreditBook
        fields=['supplier','total','paid','remaing',]

class laboursform(forms.ModelForm):
    name= forms.CharField(max_length=100,
                           widget= forms.TextInput
                           (attrs={'class':'form-control',
				   'id':'some_id'}))
    mobile_number= forms.IntegerField(
                           widget= forms.TextInput
                           (attrs={'class':'form-control',
				   'id':'some_id'}))

    address=forms.CharField(max_length=100,
                           widget= forms.TextInput
                           (attrs={'class':'form-control',
				   'id':'some_id'}))
    wages= forms.IntegerField(
                           widget= forms.TextInput
                           (attrs={'class':'form-control',
				   'id':'some_id'}))

    paid= forms.BooleanField(
       
       )
                          
   

    class Meta:
        model=Labours
        fields=['name','mobile_number','address','wages','paid']
class Employeeform(forms.ModelForm):
    name= forms.CharField(max_length=100,
                           widget= forms.TextInput
                           (attrs={'class':'form-control',
				   'id':'some_id'}))
    mobile_number= forms.IntegerField(
                           widget= forms.TextInput
                           (attrs={'class':'form-control',
				   'id':'some_id'}))

    address=forms.CharField(max_length=100,
                           widget= forms.TextInput
                           (attrs={'class':'form-control',
				   'id':'some_id'}))
    salary= forms.IntegerField(
                           widget= forms.TextInput
                           (attrs={'class':'form-control',
				   'id':'some_id'}))

    paid= forms.BooleanField(
       
       )
                          
   

    class Meta:
        model=Employee
        fields=['name','mobile_number','address','salary','paid']
class expenseform(forms.ModelForm):
    salary= forms.IntegerField(
                           widget= forms.TextInput
                           (attrs={'class':'form-control',
				   'id':'some_id'}))
    kitchen= forms.IntegerField(
                           widget= forms.TextInput
                           (attrs={'class':'form-control',
				   'id':'some_id'}))
    maintenance= forms.IntegerField(
                           widget= forms.TextInput
                           (attrs={'class':'form-control',
				   'id':'some_id'}))
    utilitybills=forms.IntegerField(
                           widget= forms.TextInput
                           (attrs={'class':'form-control',
				   'id':'some_id'}))
    internetbills=forms.IntegerField(
                           widget= forms.TextInput
                           (attrs={'class':'form-control',
				   'id':'some_id'}))
    gasbill=forms.IntegerField(
                           widget= forms.TextInput
                           (attrs={'class':'form-control',
				   'id':'some_id'}))
    waterbills=forms.IntegerField(
                           widget= forms.TextInput
                           (attrs={'class':'form-control',
				   'id':'some_id'}))
    electricitybill=forms.IntegerField(
                           widget= forms.TextInput
                           (attrs={'class':'form-control',
				   'id':'some_id'}))

    class Meta:
        model=Expense
        fields=['salary','kitchen','maintenance','utilitybills','internetbills','gasbill','waterbills','electricitybill']
# form used to select a supplier
class SelectSupplierForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['supplier'].queryset = Supplier.objects.filter(is_deleted=False)
        self.fields['supplier'].widget.attrs.update({'class': 'textinput form-control'})
    class Meta:
        model = PurchaseBill
        fields = ['supplier']

# form used to render a single stock item form
class PurchaseItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['stock'].queryset = Stock.objects.filter(is_deleted=False)
        self.fields['stock'].widget.attrs.update({'class': 'textinput form-control setprice stock', 'required': 'true'})
        self.fields['quantity'].widget.attrs.update({'class': 'textinput form-control setprice quantity', 'min': '0', 'required': 'true'})
        self.fields['weight'].widget.attrs.update({'class': 'textinput form-control setprice weight',  'required': 'true'})
        self.fields['perprice'].widget.attrs.update({'class': 'textinput form-control setprice price', 'min': '0', 'required': 'true'})
        
    class Meta:
        model = PurchaseItem
        fields = ['stock', 'quantity', 'perprice','weight']

# formset used to render multiple 'PurchaseItemForm'
PurchaseItemFormset = formset_factory(PurchaseItemForm, extra=1)

# form used to accept the other details for purchase bill
class PurchaseDetailsForm(forms.ModelForm):
    class Meta:
        model = PurchaseBillDetails
        fields = ['eway','veh', 'destination', 'po', 'cgst', 'sgst', 'igst', 'cess', 'tcs', 'total']


# form used for supplier
class SupplierForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'textinput form-control', 'pattern' : '[a-zA-Z\s]{1,50}', 'title' : 'Alphabets and Spaces only'})
        self.fields['phone'].widget.attrs.update({'class': 'textinput form-control', 'maxlength': '10', 'pattern' : '[0-9]{10}', 'title' : 'Numbers only'})
        self.fields['email'].widget.attrs.update({'class': 'textinput form-control'})
       
    class Meta:
        model = Supplier
        fields = ['name', 'phone', 'address', 'email',]
        widgets = {
            'address' : forms.Textarea(
                attrs = {
                    'class' : 'textinput form-control',
                    'rows'  : '4'
                }
            )
        }


# form used to get customer details
class SaleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'textinput form-control', 'pattern' : '[a-zA-Z\s]{1,50}', 'title' : 'Alphabets and Spaces only', 'required': 'true'})
        self.fields['phone'].widget.attrs.update({'class': 'textinput form-control', 'maxlength': '10', 'pattern' : '[0-9]{10}', 'title' : 'Numbers only', 'required': 'true'})
        self.fields['email'].widget.attrs.update({'class': 'textinput form-control'})
       
    class Meta:
        model = SaleBill
        fields = ['name', 'phone', 'address', 'email', ]
        widgets = {
            'address' : forms.Textarea(
                attrs = {
                    'class' : 'textinput form-control',
                    'rows'  : '4'
                }
            )
        }

# form used to render a single stock item form
class SaleItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['stock'].queryset = Stock.objects.filter(is_deleted=False)
        self.fields['stock'].widget.attrs.update({'class': 'textinput form-control setprice stock', 'required': 'true'})
        self.fields['quantity'].widget.attrs.update({'class': 'textinput form-control setprice quantity', 'min': '0', 'required': 'true'})
        self.fields['perprice'].widget.attrs.update({'class': 'textinput form-control setprice price', 'min': '0', 'required': 'true'})
        self.fields['weight'].widget.attrs.update({'class': 'textinput form-control setprice weight',  })
       
        
    class Meta:
        model = SaleItem
        fields = ['stock', 'quantity', 'perprice','weight']

# formset used to render multiple 'SaleItemForm'
SaleItemFormset = formset_factory(SaleItemForm, extra=1)

# form used to accept the other details for sales bill
class SaleDetailsForm(forms.ModelForm):
    class Meta:
        model = SaleBillDetails
        fields = ['eway','veh', 'destination', 'po', 'cgst', 'sgst', 'igst', 'cess', 'tcs', 'total']
