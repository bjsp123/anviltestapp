import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.email
import anvil.server
from datetime import datetime
import random


@anvil.server.callable
def print_my_permissions():
  super_user = 'hwacha.2@gmail.com'
  if anvil.users.get_user() is None:
    print("Nobody is logged in.")
  elif anvil.users.get_user()['email'] == super_user:
    print(f"{super_user} is allowed to see this.")
  else:
    print("This path is for minimum-access users.")

@anvil.server.callable
def send_feedback(name, email, feedback):
  # Send yourself an email each time feedback is submitted
  anvil.email.send(to="hwacha.2@gmail.com", # Change this to your email address!
                   subject=f"Feedback from {name}",
                   text=f"""
                   
  A new person has filled out the feedback form!

  Name: {name}
  Email address: {email}
  Feedback:
  {feedback}
  """)

  app_tables.feedback.add_row(
      id=random.randrange(0,100000),
      name=name, 
      email=email, 
      logged_in_email=anvil.users.get_user(),
      feedback=feedback, 
      timestamp=datetime.now()
    )