from ._anvil_designer import Form1Template
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    if anvil.users.get_user() is None:
      self.logout.text="Login"
      self.title_label.text = "Not logged in"
    else:
      self.logout.text="Logout"
      self.title_label.text = "Logged in as: " + anvil.users.get_user()['email']
      
    

  def submit_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    # Set 'name' to the text in the 'name_box'
    name = self.name_box.text
    # Set 'email' to the text in the 'email_box'
    email = self.eem_box.text
    # Set 'feedback' to the text in the 'feedback_box'
    feedback = self.feedback_box.text

    anvil.server.call('send_feedback', name, email, feedback)
    Notification("Feedback sent")
    self.name_box.text=""
    self.eem_box.text=""
    self.feedback_box.text=""

  def logout_click(self, **event_args):
    if anvil.users.get_user() is None:
      anvil.users.login_with_form()
    else:
      anvil.users.logout()
      
    open_form('Form1')

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Form2')

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Form1')


