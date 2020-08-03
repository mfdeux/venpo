import click

from .main import USER_AGENT_FILE, load_user_agents, save_data, scrape_profile


@click.command()
@click.argument('username')
@click.option('--filename', default='venmo-txn', help='Filename of which to save scraped data')
def cli(username: str, filename: str):
    """
    Extract Venmo transactions from a profile with one command


    """
    user_agents = load_user_agents(USER_AGENT_FILE)
    profile_data = scrape_profile(username, user_agents)
    click.echo(f"Extracted {len(profile_data)} transactions for username '{username}'")
    save_data(profile_data, filename)

if __name__ == '__main__':
    cli()
