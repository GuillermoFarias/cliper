""" Base test case class """
import pytest
from core.testing.test_app import TestApp


class TestCase:
    """ Base test case class """
    app: TestApp = None

    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        """ Setup and teardown """
        self.app = TestApp()
        self.app.boot()

        # Configuración que se ejecuta antes de cada test
        print("Setting up test...")
        yield
        # Limpieza que se ejecuta después de cada test
        print("Tearing down test...")

        self.app.shutdown()
