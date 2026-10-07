import logging
from src.factory_pattern import create_user

def action_logger(func):
    # *args any number of positional arguments as a tuple
    # **kwargs any number of keyword arguments as a dictionary
    def wrapper(user, *args, **kwargs):
        logging.info(f"User: {user.name} ({type(user).__name__}) | Action: {func.__name__}")
        return func(user, *args, **kwargs)
    
    return wrapper


@action_logger
def upload_document(user, filename):
    print(f"{user.name} uploaded {filename}")

@action_logger
def delete_document(user, filename):
    print(f"{user.name} deleted {filename}")

if __name__ == "__main__":
    logging.basicConfig(filename="actions.log", 
                    level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

    john = create_user("admin", "John")
    sarah = create_user("guest", "Sarah")

    upload_document(john, "report.pdf")
    delete_document(sarah, "old_report.pdf")



