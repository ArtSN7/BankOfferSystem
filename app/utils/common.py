from .constants import FLASH_MSGS


def get_flash_msg_data(action: str) -> tuple[str, str]:
    data = FLASH_MSGS[action]
    return data['message'], data['category']
