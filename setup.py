from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT='-e .'

def get_requirements(filepath:str) -> List[str]:
    '''
    this function will return list of requirements
    '''

    requirements = []

    with open('requirements.txt','r') as file:
        requirements = file.readlines()
        requirements=[req.replace('\n',' ')for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements
setup(
    name='mlproject',
    version='0.0.1',
    author='Vishwa',
    author_email='vishwaparmar.124@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
