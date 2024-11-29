ALLOWED_EXTENSIONS = {'xls', 'xlsx', 'csv'}

FLASH_MSGS = {
    'wrong_auth': {
        'message': 'Неправильный логин или пароль',
        'category': 'error',
    },
    'file_sent': {
        'message': 'Файл успешно отправлен',
        'category': 'success',
    },
    'data_not_valid': {
        'message': 'Данные не валидны для анализа',
        'category': 'error',
    },
    'wrong_file_format': {
        'message': 'Расширение файла не поддерживается. '
                   'Доступные форматы: xls, xlsx, или csv',
        'category': 'error',
    },
    'leads_transferred': {
        'message': 'Лиды успешно добавлены на страницу',
        'category': 'success',
    },
    'file_downloaded': {
        'message': 'Файл с лидами успешно загружен',
        'category': 'success',
    },
}
