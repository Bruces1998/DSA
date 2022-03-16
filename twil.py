# from decouple import 
from twilio.rest import Client




TWILIO_ACCOUNT_SID = 'AC39d34f184ba4d66d788897515d256fd6'
TWILIO_AUTH_TOKEN = '714031085babf75241d1e3691c8ed88e'

order_details = {
    'amount': '5kg',
    'item': 'Tomatoes',
    'date_of_delivery': '03/04/2021',
    'address': 'No 1, Ciroma Chukwuma Adekunle Street, Ikeja, Lagos'
}
user_whatsapp_number = "917028319985"
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
message = client.messages.create(
            from_='whatsapp:+14155238886',
            body='Your {} order of {} has shipped and should be delivered on {}. Details: {}'.format(
                order_details['amount'], order_details['item'], order_details['date_of_delivery'],
                order_details['address']),
            to='whatsapp:+{}'.format(user_whatsapp_number)
        )