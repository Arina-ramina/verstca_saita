import os


def get_api_key() -> str:
    """Возвращает API-ключ для SuperJob из переменных окружения."""
    env_var = os.environ
    env_var['SJ_API_KEY'] = 'v3.r.137913331.eb600f8e693ed831bd71b5cc26830745fcbffd2b.0f1003bde68956a1069ec791d792c9045bbba731'
    return os.getenv('SJ_API_KEY')