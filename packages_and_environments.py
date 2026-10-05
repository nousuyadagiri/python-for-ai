"""
Packages and Environments in Python

This file explains the concepts of:
1. Virtual Environments
2. pip (Python Package Installer)
3. Requirements files (requirements.txt)
4. Package Documentation

Since these are mostly terminal/command-line concepts, they are explained
in the comments below. We also have some code to demonstrate package usage.
"""

# ==========================================
# 1. Virtual Environments (venv)
# ==========================================
# A virtual environment is an isolated space for your Python project.
# It allows you to install packages specific to this project without 
# interfering with other projects or the global Python installation.
#
# TERMINAL COMMANDS TO CREATE AND USE A VIRTUAL ENVIRONMENT:
#
# 1. Create a virtual environment named 'venv' in your current folder:
#    macOS/Linux/Windows: python3 -m venv venv
#
# 2. Activate the virtual environment (do this before installing packages):
#    macOS/Linux: source venv/bin/activate
#    Windows:     venv\Scripts\activate
#
# 3. Deactivate (when you are done working):
#    macOS/Linux/Windows: deactivate


# ==========================================
# 2. pip (Python Package Installer)
# ==========================================
# 'pip' is the tool used to install external libraries (packages) that 
# don't come built-in with Python (e.g., requests, numpy, pandas).
#
# TERMINAL COMMANDS FOR PIP:
#
# 1. Install a package:
#    pip install requests
#
# 2. Uninstall a package:
#    pip uninstall requests
#
# 3. List all installed packages in your active environment:
#    pip list
#
# 4. Search for a specific package details:
#    pip show requests


# ==========================================
# 3. Requirements files (requirements.txt)
# ==========================================
# A requirements.txt file lists all the packages and their exact versions 
# that your project needs to run. This makes it easy to share your project.
#
# TERMINAL COMMANDS FOR REQUIREMENTS:
#
# 1. Generate a requirements.txt file based on currently installed packages:
#    pip freeze > requirements.txt
#
# 2. Install all packages listed in a requirements.txt file (useful when 
#    someone else clones your project):
#    pip install -r requirements.txt


# ==========================================
# 4. Package Documentation
# ==========================================
# When using external or built-in packages, it's important to know how to 
# read their documentation. You can check the official websites (e.g., PyPI)
# or use built-in Python tools like help() and dir().

import math # Built-in package

def explore_package():
    print("--- Exploring Package Documentation ---")
    
    # Using dir() to list all available functions/variables in a module
    print("1. Using dir(math) to see what's inside the 'math' package:")
    math_attributes = dir(math)
    # Just printing the first 10 so it's not too long
    print(math_attributes[:10]) 
    print()
    
    # Using help() to read the documentation (docstring) of a specific function
    print("2. Using help() to read documentation for math.sqrt:")
    # This will print the internal documentation for the square root function
    print(math.sqrt.__doc__) 
    print()


# ==========================================
# Practical Example: Using an External Package
# ==========================================
def fetch_example():
    print("--- Using an External Package ---")
    try:
        # 'requests' is an external package. It must be installed via pip.
        import requests
        
        print("Successfully imported 'requests'!")
        response = requests.get("https://api.github.com")
        print(f"GitHub API Status Code: {response.status_code}")
    except ImportError:
        print("The 'requests' package is not installed.")
        print("To fix this, run this in your terminal: pip install requests")

if __name__ == "__main__":
    explore_package()
    fetch_example()
