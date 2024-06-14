from setuptools import find_packages,setup
from typing import List

# HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements =[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements= [req.replace("\n","") for req in requirements if not req.startswith('-e')]
    
    return requirements

setup(
    name='my_package',
  version='0.1',
  description='An end-to-end ml project template',
  author='Hari',
  author_email='hspv@gmail.com',
  packages=find_packages(),
  install_requires=get_requirements('requirements.txt')
)