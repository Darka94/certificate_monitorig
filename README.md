# certificate_monitorig
#Monitoreo_de_certificado_digitales

_________                __  .__  _____.__               __           
\_   ___ \  ____________/  |_|__|/ ____\__| ____ _____ _/  |_  ____   
/    \  \/_/ __ \_  __ \   __\  \   __\|  |/ ___\\__  \\   __\/ __ \  
\     \___\  ___/|  | \/|  | |  ||  |  |  \  \___ / __ \|  | \  ___/  
 \______  /\___  >__|   |__| |__||__|  |__|\___  >____  /__|  \___  > 
        \/     \/                              \/     \/          \/  
   _____                .__  __               .__                     
  /     \   ____   ____ |__|/  |_  ___________|__| ____   ____        
 /  \ /  \ /  _ \ /    \|  \   __\/  _ \_  __ \  |/ ___\ /    \       
/    Y    (  <_> )   |  \  ||  | (  <_> )  | \/  / /_/  >   |  \      
\____|__  /\____/|___|  /__||__|  \____/|__|  |__\___  /|___|  /      
        \/            \/                        /_____/      \/       
        
        
      El fin de este script es recorrer todos los archivos o un directorio especifico en busca de certificados digitales y enviar una alerta a los 15 días de su vencimiento y un día antes.
      sus usos pueden ser variados, espero que sea de utilidad.
      
      TIPS:
      
      Puedes ejecutar este scrpit de Python como un cronjob en tu sistema Linux para que se ejecute automáticamente cada 24 horas. Para hacer esto, puedes agregar una nueva línea a tu archivo crontab (crontab -e) con el siguiente comando:

0 0 * * * /usr/bin/python3 /ruta/a/tu/script.py
