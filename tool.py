import click
import toml


@click.command()
@click.option('--url', prompt='RPC endpoint', help='URI to the RPC endpoint')

def init(url):

    

    config = f"""

    # This is a OLI Box TOML config file.
    title = "OLI BOX Config"

    [web3_provider]
    url = {url}

    """
    parsed_config = toml.loads(config)
    formatted_config = toml.dumps(parsed_config)

    

    f = open('config.toml', 'w')
    f.write(formatted_config)
    f.close()

init()
