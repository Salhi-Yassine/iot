from django.core.mail import send_mail
from django.db import models
from twilio.rest import Client
from django.conf import settings
import telepot


class Temperature(models.Model):
    temp = models.FloatField(null=True)
    dt = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.temp)

    def save(self, *args, **kwargs):
        if self.temp > 40:
            # send sms
            # Set environment variables for your credentials
            # Read more at http://twil.io/secure
            account_sid = settings.MY_TWILIO_SID
            auth_token = settings.MY_TWILIO_TOKEN
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body=f'🚨 la température élevée {self.temp} °C🌡',
                from_=settings.MY_TWILIO_PHONE_NUMBER,
                to=settings.MY_PHONE_NUMBER
            )

            print(message.sid)
            # send in telegram bot
            token = settings.MY_TELEGRAM_TOKEN
            rece_id = settings.MY_TELEGRAM_ID

            bot = telepot.Bot(token)
            bot.sendMessage(rece_id, '🚨 alerter la température est au-dessus de la norme ' + str(self.temp) + '°C🌡')
            # send mail
            send_mail(
                'température dépasse la normale,' + str(self.temp),
                'anomalie dans la machine',
                settings.EMAIL_HOST_USER,
                ['boy.yassine+iot@hotmail.com'],
                fail_silently=False,
            )

        return super().save(*args, **kwargs)
