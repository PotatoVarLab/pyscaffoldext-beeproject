# -*- coding: utf-8 -*-
import argparse

from pyscaffold.api import Extension, helpers
from pyscaffold.extensions.no_skeleton import NoSkeleton
from pyscaffold.extensions.pre_commit import PreCommit

from pyscaffoldext.markdown.extension import MarkDown

from . import templates


class IncludeExtensions(argparse.Action):
    """Activate other extensions
    """

    def __call__(self, parser, namespace, values, option_string=None):
        extensions = [
            NoSkeleton('no_skeleton'),
            PreCommit('pre_commit'),
            BeeProject('beeproject')
        ]
        namespace.extensions.extend(extensions)


class BeeProject(Extension):
    """Template for data-science projects
    """

    def augment_cli(self, parser):
        """Augments the command-line interface parser

        A command line argument ``--FLAG`` where FLAG=``self.name`` is added
        which appends ``self.activate`` to the list of extensions. As help
        text the docstring of the extension class is used.
        In most cases this method does not need to be overwritten.

        Args:
            parser: current parser object
        """
        help = self.__doc__[0].lower() + self.__doc__[1:]

        parser.add_argument(
            self.flag,
            help=help,
            nargs=0,
            dest="extensions",
            action=IncludeExtensions)
        return self

    def activate(self, actions):
        actions = self.register(
            actions,
            add_beeproject,
            after='define_structure'
        )
        actions = self.register(
            actions,
            remove_file,
            after='add_beeproject'
        )
        # actions = self.register(
        #     actions,
        #     replace_readme,
        #     after='add_beeproject'
        # )
        return actions


def add_beeproject(struct, opts):
    """Adds basic module for custom extension

    Args:
        struct (dict): project representation as (possibly) nested
            :obj:`dict`.
        opts (dict): given options, see :obj:`create_project` for
            an extensive list.

    Returns:
        struct, opts: updated project representation and options
    """
    gitignore_all = templates.gitignore_all(opts)

    path = [opts["project"], ".gitignore"]
    struct = helpers.ensure(struct, path,
                            gitignore_all,
                            helpers.NO_OVERWRITE)
    
    path = [opts["project"], "data", ".gitignore"]
    struct = helpers.ensure(struct, path,
                            templates.gitignore_data(opts),
                            helpers.NO_OVERWRITE)

    path = [opts["project"], "notebooks", "template.ipynb"]
    template_ipynb = templates.template_ipynb(opts)
    struct = helpers.ensure(struct, path,
                            template_ipynb,
                            helpers.NO_OVERWRITE)

    path = [opts["project"], "models", ".gitignore"]
    struct = helpers.ensure(struct, path,
                            "",
                            helpers.NO_OVERWRITE)

    #### custom package ####
    # path = [opts["project"], "src", opts['package'],  "__init__.py"]
    # init = templates.init(opts)
    # struct = helpers.ensure(struct, path,
    #                         init,
    #                         helpers.NO_OVERWRITE) 

    path = [opts["project"], "src", opts["package"], "README.md"]
    project_readmd = templates.package_readme(opts)
    struct = helpers.ensure(struct, path,
                            project_readmd,
                            helpers.NO_OVERWRITE)

    path = [opts["project"], "src", opts["package"], "requirements.txt"]
    struct = helpers.ensure(struct, path)

    path = [opts["project"], "src", opts["package"], "run_temp_pkg.py"]
    run_project_main = templates.run_project_main(opts)
    struct = helpers.ensure(struct, path,
                            run_project_main,
                            helpers.NO_OVERWRITE)
    
    path = [opts["project"], "src", opts["package"], "supervisor_temp_pkg.ini"]
    supervisor_ini = templates.supervisor_ini(opts)
    struct = helpers.ensure(struct, path,
                            supervisor_ini,
                            helpers.NO_OVERWRITE)

    path = [opts["project"], "src", opts['package'], 'temp_pkg',  "__init__.py"]
    init = templates.project_init(opts)
    struct = helpers.ensure(struct, path,
                            init,
                            helpers.NO_OVERWRITE)
    
    path = [opts["project"], "src", opts["package"], ".env.example"]
    struct = helpers.ensure(struct, path)

    path = [opts["project"], "src", opts["package"], 'temp_pkg', "settings.py"]
    settings = templates.settings(opts)
    struct = helpers.ensure(struct, path,
                            settings,
                            helpers.NO_OVERWRITE)

    path = [opts["project"], "src", opts["package"], 'temp_pkg', "manage.py"]
    project_manage = templates.manage(opts)
    struct = helpers.ensure(struct, path,
                            project_manage,
                            helpers.NO_OVERWRITE)

    path = [opts["project"], "src", opts["package"], 'temp_pkg', "_log.py"]
    log = templates.project_logger(opts)
    struct = helpers.ensure(struct, path,
                            log,
                            helpers.NO_OVERWRITE)

    path = [opts["project"], "src", opts["package"],
            'temp_pkg', "submodule", "__init__.py"]
    init = templates.init(opts)
    struct = helpers.ensure(struct, path,
                            init,
                            helpers.NO_OVERWRITE)

    path = [opts["project"], "src", opts["package"],
            'temp_pkg', "submodule", "settings.py"]
    subsettings = templates.subsettings(opts)
    struct = helpers.ensure(struct, path,
                            subsettings,
                            helpers.NO_OVERWRITE)

    path = [opts["project"], "src", opts["package"],
            'temp_pkg', "submodule", "manage.py"]
    submanage = templates.submanage(opts)
    struct = helpers.ensure(struct, path,
                            submanage,
                            helpers.NO_OVERWRITE)

    return struct, opts


def remove_file(struct, opts):
    """Remove a file from the project tree representation if existent by our own

    Args:
        struct (dict): project representation as (possibly) nested
            :obj:`dict`.
        opts (dict): given options, see :obj:`create_project` for
            an extensive list.

    Returns:
        struct, opts: updated project representation and options
    """
    # file_path = [opts['project'], "requirements.txt"]
    # struct = helpers.reject(struct, file_path)
    # file_path = [opts['project'], "environment.yaml"]
    # struct = helpers.reject(struct, file_path)

    file_path = [opts['project'], "setup.cfg"]
    struct = helpers.reject(struct, file_path)
    file_path = [opts['project'], "setup.py"]
    struct = helpers.reject(struct, file_path)

    file_path = [opts['project'], "src", opts["package"], "__init__.py"]
    struct = helpers.reject(struct, file_path)

    file_path = [opts['project'], "docs", "conf.py"]
    struct = helpers.reject(struct, file_path)
    docs_conf = templates.sphinx_conf(opts)
    struct = helpers.ensure(struct, file_path, docs_conf, helpers.NO_OVERWRITE)

    return struct, opts


def replace_readme(struct, opts):
    """Replace the readme.md of the markdown extension by our own

    Args:
        struct (dict): project representation as (possibly) nested
            :obj:`dict`.
        opts (dict): given options, see :obj:`create_project` for
            an extensive list.

    Returns:
        struct, opts: updated project representation and options
    """
    # let the markdown extension do its job first
    struct, opts = MarkDown('markdown').markdown(struct, opts)

    file_path = [opts['project'], "README.md"]
    struct = helpers.reject(struct, file_path)
    readme = templates.readme_md(opts)
    struct = helpers.ensure(struct, file_path, readme, helpers.NO_OVERWRITE)
    return struct, opts
