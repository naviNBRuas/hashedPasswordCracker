# Hashed Password Cracker Tool User Manual

## Introduction

The Hashed Password Cracker Tool is a Python application designed to crack hashed passwords often used for secure storage and authentication. It utilizes various techniques such as brute force, dictionary attacks, and rainbow table lookups to attempt to reverse-engineer the original password from its hash value. The tool provides a user-friendly interface for inputting hashed passwords and employs advanced algorithms and optimization techniques to increase efficiency and speed. The project aims to assist users in recovering forgotten passwords or testing the strength of their hashed password implementations.

## Installation

To use the Hashed Password Cracker Tool, you need to install the required dependencies. Follow the steps below to install the necessary dependencies:

1. Make sure you have Python installed on your system. You can download Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Open a terminal or command prompt and navigate to the directory where you have downloaded the Hashed Password Cracker Tool files.

3. Run the following command to install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

   This command will install the required dependencies specified in the `requirements.txt` file.

## Usage

Once you have installed the dependencies, you can use the Hashed Password Cracker Tool by following these steps:

1. Open a terminal or command prompt and navigate to the directory where you have downloaded the Hashed Password Cracker Tool files.

2. Run the following command to start the application:

   ```
   python main.py
   ```

   This command will launch the user-friendly interface of the Hashed Password Cracker Tool.

3. In the application window, enter the hashed password that you want to crack in the input field.

4. Click the "Crack Password" button to initiate the cracking process.

5. The tool will attempt to crack the hashed password using various techniques such as brute force, dictionary attacks, and rainbow table lookups.

6. Once the cracking process is complete, the tool will display the result in the application window.

   - If the password is cracked using brute force, the tool will display "Password cracked using brute force".
   - If the password is cracked using a dictionary attack, the tool will display "Password cracked using dictionary attack".
   - If the password is cracked using a rainbow table lookup, the tool will display "Password cracked using rainbow table lookup".
   - If the password is not cracked, the tool will display "Password not cracked".

7. You can repeat the process with different hashed passwords by entering a new hashed password and clicking the "Crack Password" button again.

## Customization

The Hashed Password Cracker Tool provides some customization options that you can modify according to your requirements. Here are the customization options available:

- **Dictionary**: You can modify the `dictionary.txt` file to include your own set of common passwords for the dictionary attack. Each password should be on a separate line.

- **Rainbow Table**: You can modify the `rainbow_table.txt` file to include your own set of precomputed hash-password pairs for the rainbow table lookup. Each line should contain a hash value and its corresponding password, separated by a colon.

- **Password Length**: You can modify the `min_length` and `max_length` parameters in the `generate_passwords` method of the `PasswordCracker` class in the `password_cracker.py` file to specify the minimum and maximum length of passwords to be generated for the brute force attack.

- **Character Set**: You can modify the `characters` parameter in the `generate_passwords` method of the `PasswordCracker` class in the `password_cracker.py` file to specify the characters to be used for generating passwords for the brute force attack.

## Conclusion

The Hashed Password Cracker Tool is a powerful tool for cracking hashed passwords and assisting users in recovering forgotten passwords or testing the strength of their hashed password implementations. By following the installation and usage instructions provided in this manual, you can effectively use the tool and customize it according to your requirements.