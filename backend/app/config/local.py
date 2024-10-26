import os
from pathlib import Path

DEBUG = True

FREE_ACCOUNT_USERNAME = "free_account"

ADMIN_USERNAME = "dairoot"
ADMIN_PASSWORD = "dairoot"
CHATGPT_GATEWAY_URL = "https://dairoot.serv00.net"
# CHATGPT_GATEWAY_URL = "http://127.0.0.1:8787"

BASE_DIR = Path(__file__).resolve().parent.parent
log_file_path = os.path.join(BASE_DIR, os.pardir, 'logs/cron.log')

CRONJOBS = [
    ('*/1 * * * *', 'app.cron.update_token', f'>> {log_file_path}'),
]