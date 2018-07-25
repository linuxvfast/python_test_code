import os
try:
    import configparser
except ImportError:
    import ConfigParser as configparser

import jinja2


NAMES = ["server_a_host", "server_a_port", "server_b_host",
"server_b_port", "server_c_host", "server_c_port"]


def render(tpl_path, **kwargs):
    path, filename = os.path.split(tpl_path)
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(path or './')
    ).get_template(filename).render(**kwargs)


def parser_vars_into_globals(filename):
    parser = configparser.ConfigParser()
    parser.read(filename)

    for name in NAMES:
        globals()[name] = parser.get('DEFAULT', name)


def main():
    parser_vars_into_globals('base.cfg')
    with open('service1.xml', 'w') as f:
        f.write(render('service_template.xml', **globals()))

    with open('service2.xml', 'w') as f:
        f.write(render('services_template2.xml', **globals()))


if __name__ == '__main__':
    main()