from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name= "processador_imagens",
    version = "0.0.1",
    author= "Adilson Miguel",
    author_email= "miguelvladimir79@gmail.com",
    name= "processador_imagens",
    version = "0.0.1",
    packages= find_packages(),

)
      