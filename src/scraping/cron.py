from pickletools import read_uint1
from .models import Stock, AlarmStock
from django.core.mail import EmailMessage
import requests
from django.conf import settings

def my_scheduled_job(request):
    user = request.user
    print(user)
    queryset = AlarmStock.objects.filter(user=user)
    stocks = Stock.objects.all()
    for stock in stocks:
        for alarm in queryset:
            if stock.id == alarm.stock.id:
                if alarm.buying_at <= stock.price:
                    EmailMessage(
                        'Alarm Stock Alert',
                        'Buying Opportunity',
                        settings.EMAIL_HOST_USER,
                        ['paolo9517@gmail.com'],
                    )
                if alarm.selling_at >= stock.price:
                    EmailMessage(
                        'Alarm Stock Alert',
                        'Selling Opportunity:',
                        settings.EMAIL_HOST_USER,
                        ['paolo9517@gmail.com'],
                    )
