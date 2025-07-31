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
    description="Um gerador de imagens, que procuara por diferenças",
    long_description=page_description,
    long_description_content_type= "text/markdown",
    url= "https://github.com/MiguelTheHound/Gerador-de-imagem",
    packages= find_packages(),
    install_requires ="requirements",
    python_requires = '>= 3.8' 
)
      