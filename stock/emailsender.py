from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import smtplib
import socket
from string import Template


def generate_alert_email(name, email, product_name, quantity):

    message = MIMEMultipart()
    message["from"] = "STOCK ALERT"
    message["to"] = email
    message["subject"] = "Stock Alert!!!"

    # ...

    # Define a simple HTML template for the email body
    low_stock_template = Template("""
    <html>
        <body>
            <h1>Stock Alert</h1>
            <p>Hello ${name},</p>
            <p>The product ${product_name} is low on stock. Only ${quantity} left.</p>
            <p>Please restock soon.</p>
        </body>
    </html>
    """)

    # Substitute the template variables with actual values
    body_part = low_stock_template.substitute({
        "name": name,
        "product_name": product_name,  # Replace with actual product name
        "quantity": quantity  # Replace with actual quantity
    })

    # Attach the HTML body to the email message
    message.attach(MIMEText(body_part, "html"))

    # ...

    try:
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
            smtp.ehlo()
            print("hello")
            smtp.starttls()  # transport layer security with this all the commands we send with server will be encrypted
            print("transporting")
            smtp.login("samipythontest@gmail.com",
                       "kbqrjimrtbstdxky")
            print("logged in")
            smtp.send_message(message)
            print("sent...")
    except socket.gaierror as ex:
        print(ex)
    except smtplib.SMTPAuthenticationError as e:
        print(e)


