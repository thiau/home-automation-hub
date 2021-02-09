from server.automation_hub import AutomationHub
from dotenv import load_dotenv

load_dotenv()

AutomationHub().start()