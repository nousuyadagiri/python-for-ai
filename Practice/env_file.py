import os
from dotenv import load_dotenv

load_dotenv()


print(f"Current directory: {os.cwd()}")


default_url = os.environ.get("DATABASE_URL", "https://nousu-ai-agent.vercel-app")
secret_key = os.environ.get("SECRET_KEY", "hsj3l2@$%jsf")

print(f"Default_url: {default_url}")
print(f"secret_key: {secret_key}")
