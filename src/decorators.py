import logging

# Setup basic config for logging
logging.basicConfig(filename="actions.log", 
                    level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Our decorator
def action_logger(func):
    # *args any number of positional arguments as a tuple
    # **kwargs any number of keyword arguments as a dictionary
    def wrapper(*args, **kwargs):

        user = args[0]

        logging.info(f"User: {user} | Action: {func.__name__}")
        return func(*args, **kwargs)
    
    return wrapper


@action_logger
def upload_document(user, filename):
    print(f"{user} uploaded {filename}")

@action_logger
def delete_document(user, filename):
    print(f"{user} deleted {filename}")

upload_document("John", "report.pdf")
upload_document("Sarah", "notes.pdf")
delete_document("Alex", "old_report.pdf")