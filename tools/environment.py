import os
import platform
import sys

from config import settings
from pages.dashboard import dashboard_page


def create_allure_environment_file():
    items = [f'{key}={value}'for key, value in settings.model_dump().items() ]
    os_info = f'{platform.system()}, {platform.release()}'
    python_version = sys.version
    items.append(os_info)
    items.append(python_version)
    properties = '\n'.join(items)
    with open(settings.allure_results_dir.joinpath('environment.properties'),'w+') as file:
        file.write(properties)