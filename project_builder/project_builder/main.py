import os
import string
import pkg_resources 

readme_file = None
todo_file = None
def main() -> None:
    """ This is the main function of the program"""
    name, project_name = get_project_info_from_user()
    data = (project_name, name)
    get_data_file_location()
    create_project(data)
    create_readme(data)
    create_todo(data)

def get_data_file_location()->None:
    global readme_file
    global todo_file
    readme_file = pkg_resources.resource_filename('data','readme_template.md')
    todo_file = pkg_resources.resource_filename('data','todo_template.md')



def get_project_info_from_user() -> (str, str):
    """ This gets the user input and then returns them as tuple
    returns
    name -> Name of author
    project_name -> Name of Project
    """
    author_name = input('Give your name>')
    project_name = input('Give the project_name>')
    if ' ' in project_name:
        print('Project Name contains space')
        raise Error('Project Name cannot contain spaces.')
    return project_name, author_name


def create_project(data: 'tuple') -> None:
    """ This creates a directory by the name of project """
    author_name, project_name = data
    print('Creating Directory')
    os.mkdir(os.path.abspath(os.path.join(os.path.abspath('.'), project_name)))


def create_readme(data: 'tuple') -> None:
    """ This creates a empty readme and then substitute for the author name and project name"""
    global readme_file
    author_name, project_name = data
    contents = None
    with open(readme_file, 'r') as readme_template:
        contents = string.Template(readme_template.read())
    with open(project_name + '/README.md', 'w') as readme:
        readme.write(
            contents.substitute(author_name=author_name,
                                project_name=project_name))


def create_todo(data: 'tuple') -> None:
    """ This creates a todo file in the project directory"""
    global todo_file
    author_name, project_name = data
    contents = None
    with open(todo_file, 'r') as todo_template:
        contents = string.Template(todo_template.read())
    with open(project_name + '/TODO.md', 'w') as todo:
        todo.write(
            contents.substitute(author_name=author_name,
                                project_name=project_name))
