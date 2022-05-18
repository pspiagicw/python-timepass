import setuptools


setuptools.setup(
    name = "Project Builder",
    version = "0.1",
    author = "pspiagicw",
    entry_points = {
        'console_scripts':[
            'project_builder = project_builder.main:main'
        ],
    },
    author_email = "pspiagicw@gmail.com",
    description = "A project builder for my python projects",
    url = "https://github.com/pspiagicw/project_builder",
    packages = setuptools.find_packages(),
    python_requires = '>= 3.5',
    )
