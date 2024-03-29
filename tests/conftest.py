import logging
import sys

import pytest
from constants import *
from env_settings import *

from cloudshell.api.cloudshell_api import CloudShellAPISession

DEFAULT_FORMAT = "%(asctime)s [%(levelname)s]: %(name)s %(module)s - %(funcName)-20s %(message)s"


@pytest.fixture(scope="session")
def admin_session() -> CloudShellAPISession:
    admin_api = CloudShellAPISession(
        host=CLOUDSHELL_SERVER, username=CLOUDSHELL_ADMIN_USER, password=CLOUDSHELL_ADMIN_PASSWORD, domain=CLOUDSHELL_DOMAIN
    )
    print("Admin session started")
    return admin_api


@pytest.fixture(scope="session")
def logger() -> logging.Logger:
    logger = logging.getLogger("test-logger")
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter(DEFAULT_FORMAT)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


@pytest.fixture(scope="session")
def empty_blueprint() -> str:
    return DEFAULT_EMPTY_BLUEPRINT


@pytest.fixture(scope="session")
def dut_blueprint() -> str:
    return DUT_BLUEPRINT
