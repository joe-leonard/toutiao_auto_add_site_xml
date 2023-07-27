from site_post import site_post_function
from xml_post import xml_post_function
import logging



def main():
    # Set up logging configuration
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', filename='app.log')
    print("Welcome to the 头条站长平台工具 (toutiao) Tool!")

    while True:
        print("\nSelect an option:")
        print("1. Execute site_post_function")
        print("2. Execute xml_post_function")
        print("3. Exit")
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            # Step 1: Get the required input from the user (e.g., cookie_string)
            cookie_string = input("Please enter the cookie string: ")

            # Get the path to the site_options_file from the user
            site_options_file = input("Please enter the path to the site options file: ")

            # Step 2: Execute site_post_function from site_post.py
            site_post_function(cookie_string, site_options_file)
            output = site_post_function(cookie_string, site_options_file)
            print(output)

        elif choice == '2':
            # Step 1: Get the required input from the user (e.g., cookie_string)
            cookie_string = input("Please enter the cookie string: ")

            # Get the path to the options_file from the user
            options_file = input("Please enter the path to the options file: ")

            # Step 3: Execute xml_post_function from xml_post.py (passing the options file as well)
            xml_post_function(cookie_string, options_file)
            output = xml_post_function(cookie_string, options_file)
            print(output)

        elif choice == '3':
            print("Exiting the Automation Tool. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter either 1, 2, or 3.")

if __name__ == "__main__":
    main()
