# Fetching Research Papers 

A Python CLI tool to fetch and filter research papers from **PubMed** and **Semantic Scholar** based on user-defined queries. Designed to assist researchers and developers in retrieving relevant scientific literature efficiently.


<img width="1000" height="344" alt="image" src="https://github.com/user-attachments/assets/e54eee4d-5425-452c-b59d-bb3f648fd7a2" />


<img width="960" height="540" alt="image" src="https://github.com/user-attachments/assets/6bdd8f6a-c5f3-4825-aed0-d0b897579560" />


##  Features

- Fetch papers using PubMed and Semantic Scholar APIs
- Filter results by keyword, year, or author
- Export metadata to JSON or CSV
- CLI tool built with **Typer**
- Modular codebase for easy extension

## Tech Stack

- Python 3.10+
- Typer (CLI)
- Requests (for API calls)
- Poetry (for dependency management)

##  Installation

```bash
# Clone the repository
git clone https://github.com/SHRU2501/Fecthing-Research-Paper-.git
cd Fecthing-Research-Paper-

# Install dependencies via Poetry
poetry install

# Run CLI tool
python main.py --query "bioinformatics" --limit 10 --source "pubmed"


Parameter	Description
--query	Keyword to search for
--source	"pubmed" or "semantic"
--limit	Number of results to fetch
--year	Filter by publication year
--author	Search papers by author name

Results are saved in:-
output.json or output.csv
Contains: Title, Abstract, Authors, Year, Journal info

This project is licensed under the MIT License.

Acknowledgments
PubMed API

Semantic Scholar API
