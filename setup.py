from setuptools import find_packages,setup

HYPEN_E_DOt = '-e .'
from typing import List
def get_requirements(file_path:str)->list[str]:
    '''
    This func will retun the list pf requirements 
    '''

    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in file_obj.readlines()] #-e automatically triggers
    

        if HYPEN_E_DOt in requirements:
            requirements.remove(HYPEN_E_DOt)

    return requirements

setup(
    name= 'mlproject',
    version= '0.0.1',
    author='Prashant-arc',
    author_email= 'prashant.p00511@gmail.com',
    packages= find_packages(),
    install_requires= get_requirements('requirements.txt')
)