import os
from dotenv import load_dotenv 

load_dotenv

AdminR = os.getenv('ADMIN_RTOKEN')
AdminV = os.getenv('ADMIN_VTOKEN')

Admins = [AdminR, AdminV]

Btoken = os.getenv('TOKEN')