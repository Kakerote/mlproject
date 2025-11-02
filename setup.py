from setuptools import setup, find_packages
from typing import List

HYPHEN_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
         
        if HYPHEN_DOT in requirements:
            requirements.remove(HYPHEN_DOT)
        
    return requirements

setup(
name = 'mlproject',
version = '0.1.0',
author = 'Aditya',
author_email = 'singhaditya99414@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')
)