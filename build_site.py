import yaml
from staticjinja import Site

def get_links():
    with open('data/links.yml') as f:
        return yaml.safe_load(f)

site = Site.make_site(
    outpath='build',
    contexts=[
        ('links.html', lambda: {'links': get_links()}),
    ],
)
site.render()
