
from django.contrib.auth import get_user_model
from autenticacion.models import AccountManager

# Get the user model
User = get_user_model()

# Instantiate an instance of AccountManager
account_manager = AccountManager()

# Call the create_user method
user = account_manager.create_user(email='s@g.com', username='super')