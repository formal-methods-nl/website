import yaml
from staticjinja import Site

def load_yaml(name):
    with open(f'data/{name}.yml') as f:
        return yaml.safe_load(f)

context = {
    'teaching': load_yaml('teaching'),
    'seminars': load_yaml('seminars'),
}

site = Site.make_site(
    outpath='build',
    contexts=[
        ('.*', lambda: {**context, **load_yaml('constants')}),
    ],
)
site.render()
