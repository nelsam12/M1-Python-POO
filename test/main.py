import os
from datetime import datetime

def test_cron():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    log_file = os.path.join(base_dir, "cron_test.log")

    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"Cron executed at {datetime.now()}\n")