from dotenv import load_dotenv
import os
load_dotenv("access.env")

DB_User=os.getenv("DB_USER")
DB_Password=os.getenv("DB_PASSWORD")
DB_Host=os.getenv("DB_HOST")
DB_Name=os.getenv("DB_NAME")
