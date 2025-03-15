import os
from datetime import datetime


def pytest_configure(config):
    reports_dir = "reports"
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    test_type = "general"
    for arg in config.invocation_params.args:
        if "mobile" in arg:
            test_type = "mobile"
        elif "web" in arg:
            test_type = "web"

    report_file = f"reports/{test_type}_{timestamp}.html"
    config.option.htmlpath = report_file
