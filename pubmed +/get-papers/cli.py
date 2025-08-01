import typer
import pandas as pd
from papers.fetch import fetch_papers
from papers.filter import filter_authors

app = typer.Typer()

@app.command()
def get_papers_list(
    query: str,
    file: str = typer.Option(None, "--file", "-f", help="CSV file to save results"),
    debug: bool = typer.Option(False, "--debug", "-d", help="Print debug logs")
):
    typer.echo(f"Querying PubMed for: {query}")
    papers = fetch_papers(query, debug)
    filtered = filter_authors(papers)

    if not filtered:
        typer.echo("No papers found with company-affiliated authors.")
        return

    if file:
        df = pd.DataFrame(filtered)
        df.to_csv(file, index=False)
        typer.echo(f" Results saved to {file}")
    else:
        for paper in filtered:
            typer.echo("\n Paper:")
            for key, value in paper.items():
                typer.echo(f"{key}: {value}")

if __name__ == "__main__":
    app()
