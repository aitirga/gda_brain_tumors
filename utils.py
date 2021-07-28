from pathlib import Path


def get_project_path():
    return Path(__file__).parent


def get_config_path():
    return get_project_path() / "./config"
