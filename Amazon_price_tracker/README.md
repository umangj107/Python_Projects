# AMAZON PRICE TRACKER

### This small project helps trach price of your desired product on amazon and alerts you via email and text message when the price of the product goes beyond your set limit.

The project is built using python an Selenium.<br><br>
**Twilio** api is used to send text message notifications and **smtplib** is used to send email notifications.

 ---

**In order to run this project, you have to fulfill the following prerequisites:**

   1. Generate a free api key from [twilio](https://www.twilio.com)

   2. Get your Twilio SID, auth-token, virtual number and verified number from Twilio and fill in the respective fields in [notification_manager.py](notification_manager.py)         file.

   3. For email notifications, fill in your source and destination email addresses in the respective fields in the [notification_manager.py](notification_manager.py) file.

   4. Fill in your login email and password in line 28 of [notification_manager.py](notification_manager.py) file to create login connection.

   5. Get the link of your desired product in **RPB_AMAZON_URL** and your desired price for that product in **RPB_DESIRED_PRICE** fields in [main.py](main.py) file. Also make         sure you customize the message to be sent according to your requirements.

   6. Make sure all required packages are installed.

<p> After making sure the above prerequisites are fulfilled, you are all set to run your project and host it somewhere to get regular updates.</p>

---

For any further queries, write to  ```umangj107@gmail.com```
