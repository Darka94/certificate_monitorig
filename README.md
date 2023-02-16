# certificate_monitorig
#Monitoreo_de_certificado_digitales
 
        
      El fin de este script es recorrer todos los archivos o un directorio especifico en busca de certificados digitales y enviar una alerta a los 15 días de su vencimiento y un día antes.
      sus usos pueden ser variados, espero que sea de utilidad.
      
      TIPS:
      
      Puedes ejecutar este scrpit de Python como un cronjob en tu sistema Linux para que se ejecute automáticamente cada 24 horas. Para hacer esto, puedes agregar una nueva línea a tu archivo crontab (crontab -e) con el siguiente comando:

0 0 * * * /usr/bin/python3 /ruta/a/tu/script.py
