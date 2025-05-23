import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

from dotenv import load_dotenv
import os

load_dotenv()
sender_email = os.getenv('EMAIL_USER')
password = os.getenv('EMAIL_PASSWORD')

def send_email(subject, html, to_email):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    
    message = MIMEMultipart('alternative')
    message['Subject'] = subject
    message['From'] = sender_email
    message['To'] = to_email

    part = MIMEText(html, 'html')
    message.attach(part)

    fp = open('./src/header_2025.png', 'rb')
    imageHeader = MIMEImage(fp.read())
    fp.close()

    imageHeader.add_header('Content-ID', '<HeaderImage>')
    message.attach(imageHeader)

    fp = open('./src/cotas_2025.png', 'rb')
    imageCotas = MIMEImage(fp.read())
    fp.close()

    imageCotas.add_header('Content-ID', '<CotasImage>')
    message.attach(imageCotas)

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, to_email, message.as_string())

with open('index.html', 'r') as file:
    html = file.read()

subject = 'XIV Semana da Computação IME - USP'
to_email = 'jonathascastilho@usp.br'
# to_email = 'hr@griaule.com'

print(f"Você enviará o email para '{to_email}'")
confirmation = input("Digite 'Y' para confirmar o envio ou 'N' para cancelar: ")

if confirmation.upper() == 'Y':
    print("Enviando...")
    send_email(subject, html, to_email)
    print(f"Email enviado com sucesso para {to_email}")
else:
    print("Envio de email cancelado.")

