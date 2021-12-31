import smtplib
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from getpass import getpass

with open ('Final-Project/receiver_list.txt', 'r') as file:
    def lihatemail():
        no = 1
        for i in file.readlines():
            print(str(no)+". "+str(i))
            no+=1

    def Sendlampiran():
        namalampiran = 'Final-Project/lampiran.txt'
        with open(namalampiran, 'r') as f:
            attachment = MIMEApplication(f.read(), Name=basename(namalampiran))
            attachment['Content-Dispotition'] = 'attachment; namalampiran = "{}"'.format(basename(namalampiran))
            msg.attach(attachment)
            
    
    print("+------------------------+")
    namaemail = input("Masukkan alamat email anda: ")
    passemail = getpass("Password email: ")
    print("Daftar email penerima")
    lihatemail()
    print("--------------------------")
    tujuanemail= input("Masukkan tujuan email anda: ")
    print()
    subjectemail = input("Subject Email: ")
    isipesan = input("Isi Pesan: ")

    fromaddr = namaemail
    toaddr = tujuanemail
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = subjectemail
 
    body = isipesan
    msg.attach(MIMEText(body, 'plain'))
    Sendlampiran()

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, passemail)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    print("Pesan berhasil dikirim")
    server.quit()
    
