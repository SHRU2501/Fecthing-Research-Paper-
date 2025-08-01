import requests
from typing import List, Dict

def fetch_papers(query: str, debug: bool = False) -> List[Dict]:
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": 50  # Fetch up to 50 papers
    }

    response = requests.get(base_url, params=params)
    if debug:
        print("Search Response:", response.text)

    data = response.json()
    id_list = data.get("esearchresult", {}).get("idlist", [])

    # Now fetch detailed info for each ID
    summary_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
    paper_details = []
    for pmid in id_list:
        details = requests.get(summary_url, params={
            "db": "pubmed",
            "id": pmid,
            "retmode": "json"
        }).json()
        paper_data = details.get("result", {}).get(pmid, {})
        
        paper_details.append({
            "PubmedID": pmid,
            "Title": paper_data.get("title", ""),
            "Publication Date": paper_data.get("pubdate", ""),
            "Authors": paper_data.get("authors", [])
        })

    return paper_details
