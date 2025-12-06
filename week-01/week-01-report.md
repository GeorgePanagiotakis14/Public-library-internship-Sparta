web server python php


## gia python

δημιουργία φακέλου Project_Folder στο path C:\


δημιουργία αρχείου app.py ολα τα αρχεία και αποθηκευση στον παραπανω φάκελο, περνάς τον κώδικα python


δημιουργία φακέλου στον ιδιο φακελο με όνομα templates και μέσα σε αυτόν δημιουργία αρχείου με όνομα index.html όλα τα αρχεία κώδικας html



εγκατασταση flask -> cmd  -> install flask set FLASK_APP=app.py


κατεβασμα vs code, extension python, code app.py και τρέχεις είτε στο terminal python app.py 
είτε στο cmd pc ->  cd C:\Users... στο path του φάκελου και τέλος: python app.py. 


εμφανιση http:... ανοιγεις browser και εμφανιση μηνυματων


**να αλλάξω τα μηνυματα του κώδικα! 


## gia php

https://windows.php.net/download/  install php

δημιουργία φακελου PHP στο path C:\php, extract all files there


στον ίδιο φάκελο δημιουργείς αρχείο index.php all files με τον κώδικα php


extension php on visual code


στο cmd -> cd C:\... ekei pou einai o fakelos 

παιρνεις το localhost και το περνάς στον browser και εμφανιζει τα μηνύματα




## MySQLDB
για την αποθηκευση των δεδομένων των βιβλίων 

steps:
site: https://dev.mysql.com/downloads/installer/   install last


open file, select: full, steps: next, execute in order to be installed products


create your account and finish the installation


## Apache, without XAMPP and WAMP

Steps for web server:

site: https://www.apachelounge.com/download/ and install the appropriate one


new file -> path C:\Apache24  and extract all files from download there


sto path: C:\Apache24\conf\httpd.conf open last file, make sure the line: Define SRVROOT "/Apache24" deixnei: Define SRVROOT "c:/Apache24" and make sure that the lines below are exist without #:

  LoadModule php_module "c:/php/php8apache2_4.dll"

  AddType application/x-httpd-php .php


  PHPIniDir "C:/php"

and save the file



cmd as admin -> write: 

cd C:\Apache24\bin
httpd.exe -k install, service is installed



in the same terminal write: httpd.exe -k start


browser -> give localhost and then if it is ok appears the message: "It works!"

(php and Apache24 in the same path C:\)





Τέλος, πέρα από το κομμάτι της πληροφορικής, εργαστήκαμε σε excel με στόχο την καταμέτρηση των βιβλίων και την καλύτερη οργάνωση-ταξινόμηση των βιβλίων της βιβλιθήκης και RFID για  την γρήγορη αναζήτηση όποιου βιβλίου. Τι είναι το RFID?
