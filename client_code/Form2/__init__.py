from ._anvil_designer import Form2Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Form2(Form2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    if anvil.users.get_user() is None:
      self.logout.text="Login"
      self.title_label.text = "Not logged in"
    else:
      self.logout.text="Logout"
      self.title_label.text = "Logged in as: " + anvil.users.get_user()['email']

    self.repeating_panel_1.items = app_tables.feedback.search()