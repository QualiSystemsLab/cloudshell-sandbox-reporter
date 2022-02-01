"""
create .env file in tests directory with following keys:
CLOUDSHELL_ADMIN_USER=admin
CLOUDSHELL_ADMIN_PASSWORD=admin
CLOUDSHELL_SERVER=localhost
CLOUDSHELL_DOMAIN=Global
"""

import os

from dotenv import load_dotenv

load_dotenv()

# server credentials from .env
CLOUDSHELL_ADMIN_USER = os.environ.get("CLOUDSHELL_ADMIN_USER")
CLOUDSHELL_ADMIN_PASSWORD = os.environ.get("CLOUDSHELL_ADMIN_PASSWORD")
CLOUDSHELL_SERVER = os.environ.get("CLOUDSHELL_SERVER")
CLOUDSHELL_DOMAIN = os.environ.get("CLOUDSHELL_DOMAIN")
