from string import Template
from datetime import datetime
from dados_email import email, senha

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

cliente = email

with open("template.html", 'r', encoding='utf-8') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime("%d/%m/%Y")
    corpo_msg = template.substitute(nome="Luiz", data=data_atual)


msg = MIMEMultipart()
msg['from'] = 'Luiz Victor'
msg['to'] = 'luizvictorba@gmail.com'
msg['subject'] = "Atenção, esse é um email de teste"

corpo = MIMEText(corpo_msg, 'html')
msg.attach(corpo)

with smtplib.SMTP(host='smtpout.secureserver.net', port=465) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(email, senha)
    smtp.send_message(msg)
    print("Email enviado com Sucesso!")

