from __future__ import print_function
# import base64
import os.path
import os
import paramiko
import logging
import smtplib,email,ssl
# from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# from google.auth.transport.requests import Request
# from google.oauth2.credentials import Credentials
# from google_auth_oauthlib.flow import InstalledAppFlow
from dotenv import load_dotenv
load_dotenv()
# SCOPES = ['https://mail.google.com/']



logging.basicConfig(filename="target_Server_disk_utilization.log",format="%(asctime)s - %(levelname)s - %(message)s",filemode="w")

# smtpObj = smtplib.SMTP('smtp.gmail.com',587) 
# smtpObj.ehlo()
# smtpObj.starttls()
# smtpObj.login('rk.abhishek.ram@gmail.com',)
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

smtp_server = 'smtp.gmail.com'
smtp_port = 587 # TLS port
email_sender = "rk.abhishek.ram@gmail.com"
email_password = os.environ.get("EMAIL_PASSWORD")
email_recipient = "ramk4387@gmail.com"

msg = MIMEMultipart()
msg['From'] = email_sender
msg['To'] = email_recipient
msg['subject'] = "Log File for server disk utilization"

body = """
Please refer to the attached log file for more info.

Regards,
ABHISHEK KUMAR
"""

msg.attach(MIMEText(body, "plain"))



logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
def get_disk_utilization(server_ip, username, password):
    """Gets disk utilization information on the target server."""
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(server_ip, username=username, password=password)
    except paramiko.AuthenticationException as auth_error:
        print(f"Authentication failed: {auth_error}")
        logger.exception(f"Exception occured: {auth_error}")
        return None
    except paramiko.SSHException as ssh_error:
        print(f"SSH connection error: {ssh_error}")
        logger.exception(f"Exception occured: {ssh_error}")
        return None
    else:
        logger.info("Successfully connected to the target server!!")

    try:
        # Run the 'df' command to get disk utilization
        command = "df -h"  # -h option for human-readable output
        stdin, stdout, stderr = ssh.exec_command(command)
        output = stdout.read().decode()

        # Split the output into lines and extract relevant information
        lines = output.strip().split('\n')

        # The first line contains column headers, so skip it
        lines = lines[1:]

        disk_utilization = []

        for line in lines:
            # Split each line into columns (fields)
            columns = line.split()

            # Extract relevant information (e.g., Filesystem, Size, Used, Avail, Use%)
            filesystem = columns[0]
            size = columns[1]
            used = columns[2]
            available = columns[3]
            use_percentage = columns[4]

            # Append the information to the disk_utilization list
            disk_utilization.append({
                "Filesystem": filesystem,
                "Size": size,
                "Used": used,
                "Available": available,
                "Use%": use_percentage,
            })

        

    except Exception as e:
        print(f"Error retrieving disk utilization: {e}")
        logger.exception(f"Exception occured while finding disk utlilization : {e}")
        return None
    else:
        logger.info("Successfully accumulated all the disk utlization")
        return disk_utilization
    finally:
        logger.info("Closing ssh connection")
        ssh.close()


def send_mail(recipient):
    file_path = "./target_Server_disk_utilization.log"
    with open(file_path, "rb") as attachment:
        line = MIMEApplication(attachment.read(), Name=os.path.basename(file_path))
        line['Content-Disposition'] = f'attachment; filename={os.path.basename(file_path)}'
        msg.attach(line)

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    print(email_password)
    server.login(email_sender, email_password)

    server.sendmail(email_sender, recipient, msg.as_string())
    print("Mail sent")
    server.quit()



if __name__ == "__main__":
    server_ip = "servera"
    username = "student"
    password = "student"

    disk_info = get_disk_utilization(server_ip, username, password)
    send_mail(email_recipient)
    if disk_info:
        for item in disk_info:
            print(item)
    else:
        print("Unable to retrieve disk utilization.")
    
    