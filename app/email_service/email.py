from flask import Blueprint, render_template, request
import smtplib
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

email = Blueprint('email_service', __name__)

key_vault_name = "km5137blogcapstone"
key_vault_uri = f"https://{key_vault_name}.vault.azure.net/"

credential = DefaultAzureCredential()
client = SecretClient(vault_url=key_vault_uri, credential=credential)

SMTP_SERVER = "smtp.ukr.net"
SMTP_PORT = 465
SMTP_KEY = client.get_secret("smtpSecret").value
SMTP_USER = client.get_secret("smtpUser").value

def send_email(**kwargs):
    header = f'From: <{SMTP_USER}>\n' \
             f'To: {SMTP_USER}\n' \
             'Subject: test_email\n\n' \

    body = "\n".join([f"{key}:{value}" for key, value in kwargs.items()])

    with smtplib.SMTP_SSL(host=SMTP_SERVER, port=SMTP_PORT) as smtp:
        smtp.login(user=SMTP_USER, password=SMTP_KEY)
        smtp.sendmail(from_addr=SMTP_USER, to_addrs=SMTP_USER, msg=header + body)

# Adjust the route to avoid conflict with the main blueprint
@email.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        return render_template("contact.html")
    else:
        notification = "Successfully sent you message"
        send_email(**request.form)
        return render_template("contact.html", title=notification)