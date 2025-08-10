import smtplib
import os
from dotenv import load_dotenv
load_dotenv()
from Amazon_Prize_Tracker.ScrappingFile import getPrice
price = getPrice()
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")  
SENDER_EMAIL = "sans151004@gmail.com"
RECEIVER_EMAIL = "pandeydewansh66@gmail.com"

subject = "Product price Notification"
body = f"The current Instant Pot price is ${price}"
message = f"Subject: {subject}\n\n{body}"

try:   
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls() 
    server.login(SENDER_EMAIL, EMAIL_PASSWORD)
    server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, message)
    server.quit()
    print(" Email sent successfully!")
except Exception as e:
    print(f" Error in sending email: {e}")
