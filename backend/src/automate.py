"""
Playwright driver that executes operations based on a profile.
"""

import argparse
import json

from playwright.sync_api import sync_playwright


def main(profile: str):
    """
    Main processing method.

    Parameters
    ----------
    profile : str
        Name of the file containgin the JSON formatted profile.
    """

    url = "http://localhost:10003"

    # Open playwright and goto url
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)

        # Open profile file
        with open(profile, 'r') as json_file:
            # Process successful operations
            json_data = json.load(json_file)
            print("Successsful:")
            for operation_profile in json_data:
                print(operation_profile)
                for index in range(operation_profile['success']):
                    # Click on the button for an operation
                    page.get_by_text(operation_profile['operation']).click()
            
            # Click on the "Is Successful? checkbox"
            page.locator('input[type="checkbox"]').set_checked(False)
            
            # Process unsuccessful operations
            print("Failures:")
            for operation_profile in json_data:
                print(operation_profile)
                for index in range(operation_profile['failure']):
                    # Click on the button for an operation
                    page.get_by_text(operation_profile['operation']).click()

if __name__ == "__main__":

    # 1. Create an ArgumentParser object
    parser = argparse.ArgumentParser(
        description="A simple traffic generator using web automation"
    )

    # 2. Add arguments
    parser.add_argument("--profile", type=str, help="The traffic profile")

    # 3. Parse the arguments
    args = parser.parse_args()

    # 4. Invoke main method
    main(args.profile)
