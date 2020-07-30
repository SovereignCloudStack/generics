# Based on https://raw.githubusercontent.com/osism/generics/b600f5bf79f3223b79ebf464985c0505e0840798/ansible/render-template.py
import os, sys
import jinja2, yaml

with open('.information.yml') as fp:
    information = yaml.safe_load(fp)

loader = jinja2.FileSystemLoader(searchpath="")
environment = jinja2.Environment(loader=loader, keep_trailing_newline=True)

template = environment.get_template(sys.argv[1])
result = template.render({
    'name_title': information['name_title'],
    'name_path': information['name_path'],
    'name_description': information.get('name_description', information['name_path']),
    'attributions': information.get('attributions', {}),
    'appendix': information.get('appendix', '')
})

with open(sys.argv[1], "w+") as fp:
    fp.write(result)
