import requests


def check_server_status(ip_or_path: str):
    """Method for checking if server is up and running."""
    try:
        a = requests.get(ip_or_path)
        if a.status_code == 200:
            return True
        else:
            return False
    except Exception:
        return False
