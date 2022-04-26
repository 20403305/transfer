# # Install dotenv via:
# pip3 install python-dotenv

# Load .env file using:
from dotenv import load_dotenv
load_dotenv()

# Use the variable with:
import os
print(os.getenv("VERSION"))



import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.', '.env')
load_dotenv(dotenv_path=env_path)

my_env_var = os.getenv('MYSQL_USERNAME')
print(my_env_var)



