#!/usr/bin/python3
import os
import ssl
import datetime
import glob
import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import OpenSSL

# Configuración del correo electrónico
MAIL_FROM = 'from@server.com'
MAIL_TO = 'to@server.com'
SMTP_SERVER = 'localhost'
SMTP_PORT = 25

# Configuración del registro
LOG_FILE = 'cert_checker.log'
LOG_FORMAT '%(asctime)s %(levelname)s %(message)s'
logging.basicConfig(filename=LOG_FILE, format=LOG_FORMAT, level=logging.ERROR)

# Obtener la fecha actual
now = datetime.datetime.now()

# Buscar todos los archivos .pem en el directorio /etc y sus subdirectorios

pem_files = []
for root, dirs, files in os.walk('/'):
    for file in files:
        if file.endswith('.pem', '.crt' '.crt'):
            pem_files.extend(glob.glob(os.path.join(root, file)))


#print(f'Archivos PEM encontrados: {pem_files}')


# Leer cada archivo PEM y verificar su fecha de vencimiento
for pem_file in pem_files:
    try:
        with open(pem_file, 'r', errors='ignore') as f:
            pem_data = f.read()
        if not pem_data.startswith('-----BEGIN PRIVATE KEY-----'):
            x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, pem_data)

            #print(f'Contenido del archivo {pem_file}: {pem_data}')
            expiration_date = datetime.datetime.strptime(x509.get_notAfter().decode('ascii'), '%Y%m%d%H%M%SZ')
           # print(f'Fecha de expiración: {expiration_date}')
            days_left = (expiration_date - now).days
            # Verificar si el certificado está vencido
        # Comprobar si el certificado ha expirado
            if expiration_date < now:
                print(f'El certificado para {pem_file} ha caducado el {expiration_date}.')
                continue

            # Calcular el número de días restantes hasta la caducidad del certificado
            days_left = (expiration_date - now).days

            # Comprobar si el certificado caduca en menos de 15 días
            if days_left <= 15:
                # Enviar un correo electrónico
                message = MIMEMultipart()
                message['From'] = MAIL_FROM
                message['To'] = MAIL_TO
                message['Subject'] = f'Certificado {pem_file} caduca en {days_left} días'
                body = f'El certificado {pem_file} caduca el {expiration_date}.'
                message.attach(MIMEText(body, 'plain'))
                server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
                server.starttls()
                server.login(MAIL_FROM, MAIL_PASS)
                server.sendmail(MAIL_FROM, MAIL_TO, message.as_string())
                server.quit()

                if days_left == 1:
                    # Enviar un correo electrónico
                    message = MIMEMultipart()
                    message['From'] = MAIL_FROM
                    message['To'] = MAIL_TO
                    message['Subject'] = f'Certificado {pem_file} caduca ¡¡¡MAÑANA!!!'
                    body = f'El certificado {pem_file} caduca el {expiration_date}.'
                    message.attach(MIMEText(body, 'plain'))
                    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
                    server.starttls()
                    server.login(MAIL_FROM, MAIL_PASS)
                    server.sendmail(MAIL_FROM, MAIL_TO, message.as_string())
                    server.quit()

    except Exception as e:
        logging.error(f'Error processing {pem_file}: {e}')
