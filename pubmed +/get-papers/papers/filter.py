from typing import List, Dict
import re

# Example keywords to identify academic affiliations
ACADEMIC_KEYWORDS = ["university", "institute", "college", "school", "research center", "faculty", "dept", "department"]

# Heuristics to identify company-like keywords
COMPANY_KEYWORDS = ["pharma", "biotech", "inc", "ltd", "llc", "gmbh", "solutions", "labs", "therapeutics"]

def is_academic(affiliation: str) -> bool:
    return any(keyword.lower() in affiliation.lower() for keyword in ACADEMIC_KEYWORDS)

def is_company(affiliation: str) -> bool:
    return any(keyword.lower() in affiliation.lower() for keyword in COMPANY_KEYWORDS)

def filter_authors(papers: List[Dict]) -> List[Dict]:
    filtered_results = []
    for paper in papers:
        non_academic_authors = []
        company_affiliations = []

        for author in paper.get("Authors", []):
            affiliation = author.get("affiliation", "")
            name = author.get("name", "")
            
            if affiliation and not is_academic(affiliation):
                non_academic_authors.append(name)
                if is_company(affiliation):
                    company_affiliations.append(affiliation)

        if company_affiliations:
            filtered_results.append({
                "PubmedID": paper["PubmedID"],
                "Title": paper["Title"],
                "Publication Date": paper["Publication Date"],
                "Non-academic Author(s)": ", ".join(non_academic_authors),
                "Company Affiliation(s)": ", ".join(company_affiliations),
                "Corresponding Author Email": extract_email(paper)
            })
    
    return filtered_results

def extract_email(paper: Dict) -> str:
    # Placeholder function to get corresponding author's email
    return paper.get("corresponding_author_email", "")