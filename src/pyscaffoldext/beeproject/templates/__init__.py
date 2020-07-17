# -*- coding: utf-8 -*-
import string
from pkg_resources import resource_string

from .. import __version__ as beeproject_version


def get_template(name):
    """Retrieve the template by name

    Args:
        name: name of template

    Returns:
        :obj:`string.Template`: template
    """
    file_name = "{name}.template".format(name=name)
    data = resource_string("pyscaffoldext.beeproject.templates", file_name)
    return string.Template(data.decode("UTF-8"))


def gitignore_all(opts):
    """gitignore file that ignores just everything

    Ignore everything except of this gitignore file.

    Args:
        opts (dict): given options, see :obj:`create_project` for
            an extensive list.

    Returns:
        str: file content as string
    """
    template = get_template("gitignore_all")
    return template.safe_substitute(opts)


def gitignore_data(opts):
    """gitignore file that ignores almost everything

    Ignore everything except of gitignore also in sub directories.

    Args:
        opts (dict): given options, see :obj:`create_project` for
            an extensive list.

    Returns:
        str: file content as string
    """
    template = get_template("gitignore_data")
    return template.safe_substitute(opts)


def environment_yaml(opts):
    """Environment.yaml with some basic libraries

    Args:
        opts (dict): given options, see :obj:`create_project` for
            an extensive list.

    Returns:
        str: file content as string
    """
    template = get_template("environment_yaml")
    return template.safe_substitute(opts)


def readme_md(opts):
    """Adds a basic README.md

    Args:
        opts (dict): given options, see :obj:`create_project` for
            an extensive list.

    Returns:
        str: file content as string
    """
    template = get_template("readme_md")
    opts['pkg'] = opts['package'].ljust(19)
    opts['beeproject_version'] = beeproject_version
    return template.safe_substitute(opts)


def template_ipynb(opts):
    """Adds a template Jupyter notebook

    Args:
        opts (dict): given options, see :obj:`create_project` for
            an extensive list.

    Returns:
        str: file content as string
    """
    template = get_template("template_ipynb")
    return template.safe_substitute(opts)


def train_model_py(opts):
    """Adds a template python experiment

    Args:
        opts (dict): given options, see :obj:`create_project` for
            an extensive list.

    Returns:
        str: file content as string
    """
    template = get_template("train_model_py")
    return template.safe_substitute(opts)


## custom ##
def project_config(opts):
    """Template of project_config.yaml

    Args:
        opts: mapping parameters as dictionary

    Returns:
        str: file content as string
    """
    template = get_template("project_config")
    return template.safe_substitute(opts)


def run_project_main(opts):
    """Template of run_project_main.py

    Args:
        opts: mapping parameters as dictionary

    Returns:
        str: file content as string
    """
    template = get_template("run_project_main")
    return template.safe_substitute(opts)


def package_readme(opts):
    """Template of README.md

    Args:
        opts: mapping parameters as dictionary

    Returns:
        str: file content as string
    """
    template = get_template("package_readme")
    return template.safe_substitute(opts)


def manage(opts):
    """Template of manage.py

    Args:
        opts: mapping parameters as dictionary

    Returns:
        str: file content as string
    """
    template = get_template("manage")
    return template.safe_substitute(opts)


def settings(opts):
    """Template of settings.py

    Args:
        opts: mapping parameters as dictionary

    Returns:
        str: file content as string
    """
    template = get_template("settings")
    return template.safe_substitute(opts)


def submanage(opts):
    """Template of manage.py within submodule

    Args:
        opts: mapping parameters as dictionary

    Returns:
        str: file content as string
    """
    template = get_template("submanage")
    return template.safe_substitute(opts)


def subsettings(opts):
    """Template of settings.py

    Args:
        opts: mapping parameters as dictionary

    Returns:
        str: file content as string
    """
    template = get_template("subsettings")
    return template.safe_substitute(opts)


def init(opts):
    """Template of __init__.py

    Args:
        opts: mapping parameters as dictionary

    Returns:
        str: file content as string
    """
    if opts["package"] == opts["project"]:
        opts["distribution"] = "__name__"
    else:
        opts["distribution"] = "'{}'".format(opts["project"])
    template = get_template("__init__")
    return template.substitute(opts)


def sphinx_conf(opts):
    """Template of conf.py
    Args:
        opts: mapping parameters as dictionary
    Returns:
        str: file content as string
    """
    template = get_template("sphinx_conf")
    return template.substitute(opts)


def project_init(opts):
    """Template of project __init__.py

    Args:
        opts: mapping parameters as dictionary

    Returns:
        str: file content as string
    """
    if opts["package"] == opts["project"]:
        opts["distribution"] = "__name__"
    else:
        opts["distribution"] = "'{}'".format(opts["project"])
    template = get_template("project_init_py")
    return template.substitute(opts)


def project_logger(opts):
    """Template of conf.py
    Args:
        opts: mapping parameters as dictionary
    Returns:
        str: file content as string
    """
    template = get_template("logger")
    return template.substitute(opts)


def supervisor_ini(opts):
    """Template of supervisor ini file
    Args:
        opts: mapping parameters as dictionary
    Returns:
        str: file content as string
    """
    template = get_template("supervisor_ini")
    return template.substitute(opts)
