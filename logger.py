import logging

logging.basicConfig(
    filename="career_bot.log",
    format="%(asctime)s - %(message)s",
    level=logging.INFO,
)

def log_user_action(user_id, action):
    logging.info(f"User: {user_id}, Action: {action}")