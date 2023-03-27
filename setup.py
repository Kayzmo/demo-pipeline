from setuptools import setup, find_packages

setup(name="census-income",
      version="0.1",
      author="Kayzmo",
      author_email="kayzmo@gmail.com",
      packages=find_packages(),
      install_requires=["pandas","numpy","flask"]
      )