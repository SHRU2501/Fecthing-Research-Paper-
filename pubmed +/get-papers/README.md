get-papers/
├── papers/
│   ├── __init__.py       ← This file is essential!
│   ├── fetch.py
│   ├── filter.py
├── cli.py
├── README.md
├── requirements.txt

Project Overview

Features

Fetches PubMed papers via API

Filters authors affiliated with companies

Saves results to CSV or prints to console

Clean CLI interface built with Typer
Installation
```bash
pip install get-papers

pip install typer
```         
Usage
```bash
poetry run python cli.py get-papers-list "cancer treatment" --debug --file results.csv

get-papers --query "machine learning" --max-results 10 --output results.csv
```
Example
```bash
get-papers --query "machine learning" --max-results 10 --output results.csv
```     
Dependencies

Python 3.10+

Typer

pandas

requests

This command fetches papers related to "machine learning", limits the results to 10, and saves them to `results.csv`.
Contributing
We welcome contributions! Please fork the repository and submit a pull request with your changes.
License
This project is licensed under the MIT License. See the LICENSE file for details.
Contact
For any questions or issues, please open an issue on GitHub or contact the project maintainer.