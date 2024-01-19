# To set a global fixture need to create a python file in the name "conftest.py"
# Create function to access from any other python file so we need to add "@pytest.fixture()" before the function

import pytest
@pytest.fixture()
def number():
    no = 100
    return no
