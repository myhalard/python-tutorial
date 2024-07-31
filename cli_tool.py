import click


@click.group()
def cli():
    """
    Your command line tool
    """
    click.echo("Welcome to your CLI tool")


@cli.command()
@click.option("--username", prompt=True, help="Your username")
@click.option("--password", prompt=True, hide_input=True, help="Your password")
def login(username, password):
    """
    Login subcommand
    """
    click.echo(f"Logging in with username: {username} and password: {password}")


@cli.command()
def list_buckets():
    """
    List buckets subcommand
    """
    click.echo("Your available buckets are: Documents, Videos, Pictures")


@cli.command()
@click.argument("bucket_name", required=True, type=str)
def show_bucket(bucket_name):
    """
    Show bucket subcommand
    """
    click.echo(f"Showing bucket: {bucket_name}")


@cli.command()
def logout():
    """
    Logout subcommand
    """
    click.echo("You are now disconnected")


if __name__ == "__main__":
    cli()
