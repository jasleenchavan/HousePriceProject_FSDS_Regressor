'''from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = "-e ."
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path)as file_odj:
        requirements=file_odj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements



setup(
    name="RegressorProject",
    version="0.0.1",
    author="Jasleen",
    author_email="jasleenchavan.96@gmail.com",
    install_requires=["numpy","pandas"],
    packages=find_packages()
)'''

from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name='RegressorProject',
    version='0.0.1',
    author='jasleen',
    author_email='jasleenchavan@ineuron.ai',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)