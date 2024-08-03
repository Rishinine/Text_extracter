# Text Extractor

A Python tool to extract text from images anywhere on your Linux device.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
  - [Setup Virtual Environment](#setup-virtual-environment)
  - [Install Dependencies](#install-dependencies)
- [Usage](#usage)
  - [Running the Script](#running-the-script)
- [Adding to PATH](#adding-to-path)
- [Setting Up a Shortcut in GNOME](#setting-up-a-shortcut-in-gnome)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Introduction

Text Extractor is a Python-based tool that extracts text from images using OCR (Optical Character Recognition). It is designed for Linux devices.

## Installation

### Setup Virtual Environment

1. Clone the repository:
   ```sh
   git clone https://github.com/Rishinine/Text_extracter.git

2. Change to the project directory:
   ```sh
   cd Text_extracter
   
4. Create a virtual environment
   ```sh
   python -m venv venv
   
6. Activate the virtual environment
   # On Windows
   ```sh
   .\venv\Scripts\activate

  # On macOS and Linux
    ```sh source venv/bin/activate

5. Install the dependencies:
  pip install -r requirements.txt

# Usage

Running the Script
To extract text from an image, make the "extract. sh* script executable and run it:

1. Make the script executable:
  ```sh
  chmod +x extract.sh

2. Run the script:
    ```sh
    ./extract.sh

# Adding to PATH

To make the script accessible from anywhere on your terminal:

1. Add the directory containing "extract.sh* to your PATH. Open your *.bashrc", *.zshrc", or
   equivalent file:
    ```sh
    nano ~/.bashrc
2. Add the following line at the end of the file:
    ```sh
    export PATH="$PATH:/path/to/Text_extracter"
# Replace /path/to/Text_extracter with the actual path to the directory.

3. Reload your shell configuratios
  source ~/.bashrc

# Windows
1. Add the directory containing "extract.sh" to your PATH:
  - Open Control Panel.
  - Go to System and Security > System > Advanced system settings.
  - Click on Environment Variables.
  - Under System variables, find the *Path" variable and click Edit.
  - Click New and add the path to the directory containing "extract.sh™.

  - Click OK to close all dialogs.

2. Open a new Command Prompt window and verify the PATH is set by running:
   echo %PATH%

# macos

1. Add the directory containing *extract.sh" to your PATH. Open your *.bash_profile’,
  '.zshrc’, or equivalent file:
      nano ~/.bash_profile
2. Add the following line at the end of the file:
     export PATH="$PATH:/path/to/Text_extracter"
  # Replace /path/to/Text_extracter with the actual path to the directory.

3. Reload your shell configuration:
    source ~/.bash_profile


# Setting Up a Shortcut in GNOME
For GNOME users, you can set up a keyboard shortcut to run the script:

1. Open Settings and go to Keyboard.
2. Scroll down to the bottom and click on Custom Shortcuts.
3. Click the + button to add a new shortcut.
    - Name: Extract Text
    - Command: extract.sh
    - Shortcut: Press Set Shortcut and then press Alt+X.(or you can use your own)
4. Click Add.

Now, pressing Alt+X will run the extract.sh script.

# Features
# Extract text from images using OCR.
# Supports multiple image formats (JPEG, PNG, etc.).
# Outputs text to the console or a file.


# Contributing
1. Fork the repository.
2. Create a new branch:
    git checkout -b feature/your-feature-name
3.Make your changes and commit them:
  git commit -m 'Add some feature'
4.Push to the branch:
  git push origin feature/your-feature-name
5.Create a new Pull Request.

# License
This project is licensed under the MIT License - see the LICENSE file for details.

# Acknowledgements
  - Tesseract OCR
  - Pillow
  - Inspired by various OCR projects.

This `README.md` file provides comprehensive instructions for setting up and using your tool across different operating systems, including creating a virtual environment, installing dependencies, running the script, adding it to the system PATH, and setting up a keyboard shortcut in GNOME.







  
   




