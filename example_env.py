import os

from dotenv import load_dotenv

load_dotenv()

# print(os.environ["SECRET2"])
print(os.environ.get("SECRET2"))
