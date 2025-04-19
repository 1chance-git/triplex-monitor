import datetime

LOG_PATH = "logs/growth_log.txt"

def log_growth_event(description):
    """Append a growth event with timestamp."""
    timestamp = datetime.datetime.now().isoformat()
    with open(LOG_PATH, "a") as file:
        file.write(f"[{timestamp}] GROWTH: {description}\n")

def read_growth_events():
    """Read all growth events."""
    with open(LOG_PATH, "r") as file:
        return file.readlines()
