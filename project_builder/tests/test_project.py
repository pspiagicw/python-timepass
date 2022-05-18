import unittest
import os
from project_builder.main import create_project
from project_builder.main import create_readme
from project_builder.main import create_todo
from project_builder.main import get_data_file_location

class TestProjectBuilder(unittest.TestCase):


  def test_project_creation(self)->None:
    """ This checks if the directory is created"""
    author_name = "Example Author"
    project_name = "Example_Project"
    create_project((author_name , project_name))
    get_data_file_location()
    self.assertTrue(os.path.isdir(os.path.join('.',project_name)))




  def test_readme_creation(self)->None:
    """This checks if a readme is created"""
    author_name = "Example Author"
    project_name = "Example_Project"
    create_readme((author_name,project_name))
    print(os.path.join(os.path.abspath('.'),'/' + project_name + '/REAME.md'))
    self.assertTrue(os.path.isfile(os.path.join('.',project_name + '/README.md')))




  def test_todo_creation(self)->None:
    """This checks if a readme is created"""
    author_name = "Example Author"
    project_name = "Example_Project"
    create_todo((author_name,project_name))
    self.assertTrue(os.path.isfile(os.path.join('.',project_name + '/TODO.md')))
if __name__ == '__main__':
  unittest.main()








