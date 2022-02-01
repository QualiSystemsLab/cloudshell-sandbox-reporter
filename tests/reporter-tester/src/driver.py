import time

from data_model import *  # run 'shellfoundry generate' to generate data model classes

from cloudshell.helpers.sandbox_reporter.reporter import SandboxReporter
from cloudshell.shell.core.driver_context import InitCommandContext, ResourceCommandContext
from cloudshell.shell.core.resource_driver_interface import ResourceDriverInterface
from cloudshell.shell.core.session.cloudshell_session import CloudShellSessionContext
from cloudshell.shell.core.session.logging_session import LoggingSessionContext


class ReporterTesterDriver(ResourceDriverInterface):
    def __init__(self):
        """
        ctor must be without arguments, it is created with reflection at run time
        """
        pass

    def initialize(self, context):
        """
        Initialize the driver session, this function is called everytime a new instance of the driver is created
        This is a good place to load and cache the driver configuration, initiate sessions etc.
        :param InitCommandContext context: the context the command runs on
        """
        pass

    def cleanup(self):
        """
        Destroy the driver session, this function is called everytime a driver instance is destroyed
        This is a good place to close any open sessions, finish writing to log files
        """
        pass

    def _some_business_logic(self):
        time.sleep(10)

    def cool_service_command(self, context):
        """
        :param ResourceCommandContext context:
        """
        api = CloudShellSessionContext(context).get_api()
        sandbox_id = context.reservation.reservation_id
        with LoggingSessionContext(context) as logger:
            reporter = SandboxReporter(api, sandbox_id, logger)
            reporter.info("Starting Service Command, this may take a while...")

            try:
                # simulate long running  action
                self._some_business_logic()
            except Exception as e:
                # logs error and prints in red to sandbox console
                err_msg = f"Error caught during command. {type(e).__name__}: {str(e)}"
                reporter.error(err_msg)
                raise Exception(err_msg)

        return "Service Flow SUCCESSFUL"
