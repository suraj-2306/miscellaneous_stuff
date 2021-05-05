#! /usr/bin/python3
import smtplib
from email.message import EmailMessage
import requests
from datetime import date
import json
today = date.today()

district_id = 265
# This is for Bangalore Urban, Look up covid api's for your district

def get_vaccine_details():
    date = today.strftime("%d-%m-%Y")
    url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=%s&date=%s" % (
        district_id, date)
    r = requests.get(url)
    vaccine_write = open('vaccine.json', 'w')
    json.dump(r.json(), vaccine_write)
    vaccine_write.close()

def read_vaccine_details():
    message = []
    message_subpart = []
    vaccine_read = open('vaccine.json', 'r')
    vacc_data = json.load(vaccine_read)
    for i in vacc_data['centers']:
        for j in i['sessions']:
            if(18 == (j['min_age_limit'])):
                message_subpart.append(i['name'])
                message_subpart.append(i['address'])
                message_subpart.append(i['pincode'])
                message_subpart.append(j['vaccine'])
                message_subpart.append('\n')
                message.append(message_subpart)
    return message

def send_email_gmail(subject, message, destination):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('XXXXXXXX@gmail.com', 'XXXXXXXXXXXXXX')
    # the first argument is the mail id you intend to send from
    # the second parameter is the App password you created
    # for setting up the app password, check out README section

    msg = EmailMessage()

    message = f'{message}\n'
    msg.set_content(message)
    msg['Subject'] = subject
    msg['From'] = 'XXXXXXXX@gmail.com '
    msg['To'] = destination
    server.send_message(msg)

def main():
    get_vaccine_details()
    message = read_vaccine_details()
    subject = 'A slot in your city has been opened'
    destination = 'your_destination@gmail.com'
    value = ""
    for j in message:
        value = ' '.join([str(i) for i in j])
    if value!="" :
        message = value
        send_email_gmail(subject, message, destination)

if __name__ == "__main__":
    main()
