from itertools import count
from django.shortcuts import render
from django.views.generic import View, TemplateView
from inventory.models import Stock
from transactions.models import PurchaseItem, SaleBill, PurchaseBill, SaleItem, Supplier

from django.db.models.aggregates import Sum,Count,Avg
from django.db.models.functions import *
from django.utils.timezone import now
from datetime import timedelta


class HomeView(View):
    template_name = "home.html"
    def get(self, request):        
        labels = []
        data = []        
        stockqueryset = Stock.objects.filter(is_deleted=False).order_by('-quantity')
        # for i in stockqueryset:
        #     i.quantity=int(i.quantity)
        #     print(i.quantity)
        totalstock=Stock.objects.filter(is_deleted=False).count()
   
        customers= SaleBill.objects.values('phone').distinct().count()
        print(customers)

        import datetime

        cur=datetime.date.today()
     
        
        perdaypurchase= PurchaseItem.objects.filter(created_at=cur).aggregate(Sum('totalprice'))
        perdaypurchase=perdaypurchase['totalprice__sum']
        perdaysale= SaleItem.objects.filter(created_at=cur).aggregate(Sum('totalprice'))
        perdaysale=perdaysale['totalprice__sum']
    
        def profitperday(perdaypurchase,perdaysale):
            if perdaypurchase>perdaysale:
               return '🥺 Sad your are in Loss'
            else:
               return ' 😊 Wow You are in Profit'
        ppd=profitperday(perdaypurchase,perdaysale)
        totalsale=SaleItem.objects.aggregate(Sum('totalprice'))
        totalsale=totalsale['totalprice__sum']
        totalpurchase=PurchaseItem.objects.aggregate(Sum('totalprice'))
        totalpurchase=totalpurchase['totalprice__sum']
        
        def profit(totalpurchase,totalsale):
            if totalpurchase>totalsale:
               return 'Loss'
            else:
               return 'Profit'

        p=profit(totalpurchase,totalsale)
        averages=PurchaseItem.objects.aggregate(Avg('totalprice'))
        averages=averages['totalprice__avg']
        perdayaverages=PurchaseItem.objects.filter(created_at=cur,).aggregate(Avg('perprice'))
        perdayaverages=perdayaverages['perprice__avg']

      
        sale=SaleItem.objects.count()
        suppliers=Supplier.objects.count()
        print(suppliers)
        for item in stockqueryset:
            labels.append(item.name)
            data.append(item.quantity)
        sales = SaleBill.objects.order_by('-time')[:3]
        purchases = PurchaseBill.objects.order_by('-time')[:3]
        context = {
            'labels'    : labels,
            'data'      : data,
            'sales'     : sales,
            'purchases' : purchases,
            'totalsale':totalsale,
            'totalpurchase':totalpurchase,
            'totalstock':totalstock,
            'sale':sale,
            'suppliers':suppliers,
            'customers':customers,
            'p':p,
            'average':averages,
            'perdaysale':perdaysale,
            'perdaypurchase':perdaypurchase,
            'ppd':ppd,
            'perdayaverages':perdayaverages
        }
        return render(request, self.template_name, context)

class AboutView(TemplateView):
    template_name = "about.html"