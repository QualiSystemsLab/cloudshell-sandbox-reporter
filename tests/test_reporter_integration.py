"""
Test Against live sandbox
"""
import time

import constants
import pytest

from cloudshell.helpers.sandbox_reporter.reporter import SandboxReporter


@pytest.fixture(scope="session")
def sandbox_id(admin_session, empty_blueprint) -> str:
    start_response = admin_session.CreateImmediateTopologyReservation(
        reservationName="Reporter Test Regression", owner="admin", durationInMinutes=15, topologyFullPath=empty_blueprint
    )
    print("Started sandbox")
    sandbox_id = start_response.Reservation.Id
    time.sleep(5)
    yield sandbox_id
    admin_session.EndReservation(sandbox_id)
    print("Ended sandbox")


def test_reporter(admin_session, sandbox_id, logger):
    reporter = SandboxReporter(admin_session, sandbox_id, logger)
    reporter.warning_header("This is a dramatic header")
    reporter.info("reporter INFO message")
    time.sleep(2)
    reporter.debug("reporter DEBUG message")
    time.sleep(2)
    reporter.error("reporter ERROR message")
    time.sleep(2)
    reporter.warning("reporter WARNING message")
    time.sleep(2)
    reporter.console.anchor_tag_print("https://google.com", "I'm a hyperlink. Click me!")
    reporter.critical("reporter CRITICAL message")
    # time.sleep(2)
    # reporter.exception("reporter EXCEPTION message")
    time.sleep(2)
    reporter.success("reporter SUCCESS message")
    time.sleep(10)
