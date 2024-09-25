# recipeat

[![Python 3.11+ supported](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/release/python-3110/)
[![python style: black](https://img.shields.io/badge/python%20style-black-000000.svg?style=flat-square)](https://github.com/ambv/black)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v1.json)](https://github.com/charliermarsh/ruff)
[![uses nix](https://img.shields.io/badge/uses-nix-%237EBAE4)](https://nixos.org/)

Recipeat is designed to make managing and cooking all your favorite recipes easier. Scrape and save all your favorite recipes so you never lose them. Add the ingredient quantities directly into the instruction steps so you don't have to scroll back and forth while cooking.

## requirements

- nix, direnv, nix-direnv (see below, this will set up all the tools you need as well as the entire python environment)

## launch
* Clone the repository to your local machine
* Use poetry for environment management
* Ensure the site_id in setting.py is set to 2 for your local machine
* Run ```runserver``` to start the application