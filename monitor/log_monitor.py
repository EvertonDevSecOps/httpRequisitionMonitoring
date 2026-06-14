from datetime import datetime

def save_log(msg):
    """
    Saves logs to a file.
    :param msg: Message to be saved.
    :return: A string containing a message to be logged.
    """
    log_file = f"logs/monitoring_{datetime.now().strftime('%Y-%m-%d')}.log"

    with open(log_file, 'a', encoding="utf-8") as logs:
        logs.write(msg + "\n")