import smtplib
from os import path

# Set up the SMTP server and login credentials
smtp_server = 'smtp.example.com'
smtp_port = 587
smtp_username = 'tonijesse034@gmail.com'
smtp_password = '@Tuwei619'

# Set up the email content
from_address = 'tonijesse034@gmail.com.com'
to_address = 'agerjesse6@gmail.com'
subject = 'Hello from Python!'
message = 'This is a test mail.'

#create a file to the destination 'dest'
def create file(dest):
  #check if there exists as file with the same name in that exact location
  #If there is such a file, skip the creatoin step, otherwise create the file
  if not(path.isfile(dest)):  
    #the 'w' denotes that the file is open in write mode...so the author can edit it's contents
    f=open(dest,'w')
    f.write("welcome to python scripting")
    f.close()
 dest = "absolute path"
createfile(dest)
print("File created")

# Connect to the SMTP server
smtp_obj = smtplib.SMTP(smtp_server, smtp_port)
smtp_obj.ehlo()
smtp_obj.starttls()
smtp_obj.login(smtp_username, smtp_password)

# Send the email
email_content = f"Subject: {subject}\n\n{message}"
smtp_obj.sendmail(from_address, to_address, email_content)

# Disconnect from the SMTP server
smtp_obj.quit()



####################################################################
#the python oop
class Item:
    pay_rate = 0.8 #pay rate after 20% discount is given
    all = []
    def __init__ (self, name: str, price: float, quantity: int):
      #Run validations on the received arguements
      assert price >= 0, f"the price entered is not greater or equal to zero"
      assert quantity >= 0, f"the quantity entered is not greater or equal to zero"
      #assign to the self arguements
      self.name = name
      self.price = price
      self.quantity = quantity

      Item.all.append(self) 
         
    def calculate_total_price(self):
       return self.price * self.quantity
    def apply_discount(self):
      self.price = self.price * Item.pay_rate #the discount will be applied to all the instances of the class 'Item' and canot be overriden
      #self.price = self.price * self.pay_rate; this discount can be overriden if another pay rate is declared at instance level
      
Item1 = Item("Phone", 100, 5)
Item1.apply_discount()

#declaring pay_rate attribute at an instance level, that is the attribute will only be applied at that instance
Item2 = Item("Laptop", 1000, 6)
Item2.pay_rate = 0.9
Item2.apply_discount()
item3 = Item ("hard disk", 200, 2)
item4 = Item ("ssd", 280, 4)
item5 = Item("keyboard", 80, 2)

for instance in all:
  print(instance.price)




