""" PkgLib - a company-centric packaging and testing library
"""
import os
import config

# Organisation configuration, this is updated when calling
#     pkglib.setuptools.setup(my_config)

CONFIG = config.OrganisationConfig(
    pypi_url='http://pypi.python.org',
    pypi_variant=None,
    namespaces=['acme'],
    namespace_separator='.',
    third_party_build_prefix='acme',
    email_suffix='acme.example',
    dev_build_number='0.0',
    platform_packages=[],
    installer_search_path=[],
    default_platform_package=None,
    deploy_path=os.path.expandvars('${HOME}/pydeploy/packages'),
    deploy_bin=os.path.expandvars('${HOME}/pydeploy/bin'),
    vcs='svn',
    virtualenv_executable='virtualenv',
    sphinx_theme='pkglib.sphinx.default_theme',
    sphinx_theme_package=None,
    graph_easy=None,
    test_egg_namespace="acmetests",
    test_linter="flake8",
    test_linter_package="flake8",
    test_dirname="tests",
    jenkins_url=None,
)