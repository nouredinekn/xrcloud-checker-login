
# XRCloud Login Checker

## Overview
This script is a login checker for XRCloud, designed to verify a list of username and password combinations using proxy rotation for enhanced anonymity. It utilizes various hashing and encoding methods to prepare requests for the XRCloud API.

## Features
- **Proxy Support**: Automatically rotates through a list of proxies to hide the origin of the requests.
- **UUID Generation**: Creates unique UUIDs for each login attempt.
- **Base64 Encoding**: Encodes passwords using Base64 before sending requests.
- **MD5 Hashing**: Appends an MD5 hash to parameters for request validation.
- **Results Logging**: Logs successful logins to a text file.

## Requirements
- Python 3.x
- `requests` library
- `tkinter` for file dialog

## Installation
To set up the environment and install the required packages, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Install Dependencies**:
   Make sure you have Python and pip installed, then run:
   ```bash
   pip install requests
   ```

## Usage
1. **Prepare Your Combo List**: Create a text file containing username and password combinations in the format:
   ```
   username1:password1
   username2:password2
   ```

2. **Run the Script**:
   Execute the script using Python:
   ```bash
   python xrcloud_checker.py
   ```

3. **Select Your Combo File**: When prompted, select the text file you created.

4. **Monitor Output**: The script will output results to the console, indicating whether the login was successful or not. Successful attempts will be logged to `xrcloud-hits.txt`.

## Code Explanation
- **Proxy Rotation**: The script uses a list of proxies defined in the `proxies` array and rotates through them with the help of `itertools.cycle`.
  
- **UUID Generation**: The `generate_uuid()` function generates unique UUIDs based on the current timestamp and random values.

- **Encoding and Hashing**: Passwords are encoded in Base64, and an MD5 hash is appended to the request parameters to ensure integrity.

- **Login Check**: The `check()` function handles the login process, checking for successful login responses from the server.

## Logging
Successful logins, along with relevant user information, are stored in `xrcloud-hits.txt` for further analysis.

## Disclaimer
This script is intended for educational purposes only. Ensure you have permission to test the usernames and passwords you are using. Unauthorized access to accounts is illegal and unethical.

## Author
[Nouredine_kn]
