from os import getenv
from dotenv import load_dotenv

load_dotenv()
print(getenv("TELEGR_TOKEN"))
