def transfer_leads_to_sales_table() -> None:
    """
    This function should send new incoming leads
    from the processing queue to the leads table
    for processing by the sales manager.
    """
    pass


def collect_all_leads_data_from_db() -> dict:
    """
    This function collects all leads data
    from the database (leads_table) and returns it in dictionary format.
    Fields for collection (client information):
        - id (int)
        - full name (str, format: Ivanov T.J.)
        - phone number (str, format: 8 (888) 888-88-88)
        - email (str)
        - cross service (str, "кросс-услуга")
        - received lead date (date, format: DD.MM.YYYY)
        - rating (int)
    """
    pass


def get_leads_on_queue_count() -> int:
    """
    This function counts and returns the number of new leads
    waiting in the queue that have not been shown
    to the manager before.
    """
    pass


def download_all_leads_data() -> None:
    """
    This function downloads all data for the available leads
    from the leads table to the user's computer.
    """
    pass


def convert_to_dict(data) -> dict:
    """
    Converts input data to dictionary format.
    The input data can be in one of three formats: xls, xlsx, or csv.
    """
    pass


def validate_client_data(data: dict) -> bool:
    """
    Validates the input data.
    Returns True if the data is valid, otherwise returns False.
    """
    return True


def process_client_data(data: dict) -> None:
    """
    Adds new client data to the database (user_table),
    sends the client ID to the ML model.
    """
    pass

