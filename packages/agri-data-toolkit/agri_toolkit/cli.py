import click
from rich.console import Console

console = Console()

@click.group()
def main():
    """Agri-Data Toolkit: Data Factory CLI"""
    pass

@main.command()
@click.option('--limit', default=5, help='Number of fields to download')
@click.option('--random', is_flag=True, help='Select random locations')
def download(limit, random):
    """Download field boundaries (Mission: First Harvest)"""
    from agri_toolkit.boundaries.client import BoundaryClient
    
    console.print(f"[bold green]Harvesting data...[/bold green] (Limit: {limit}, Random: {random})")
    
    try:
        client = BoundaryClient()
        gdf, path = client.fetch_boundaries(limit=limit, random=random)
        
        console.print(f"[bold blue]✅ Downloaded {len(gdf)} fields to:[/bold blue] {path}")
        console.print(gdf.head())
        
        # Verify 3 Heavy Lifters
        console.print("\n[bold]🔍 Data Inspection:[/bold]")
        console.print(f"   - Type: {type(gdf)}")
        console.print(f"   - CRS: {gdf.crs}")
        console.print(f"   - Total Acres: {gdf['acres'].sum():.2f}")
        
    except Exception as e:
        console.print(f"[bold red]❌ Error:[/bold red] {e}")

if __name__ == '__main__':
    main()
