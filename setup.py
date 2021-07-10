from setuptools import setup

with open ("README.MD", "r") as fh:
      long_description = fh.read()

setup(name='tesla',
      version='1.0',
      description = 'Example package for Turing college exercise.',
      py_modules=['factory'],
      package_dir = {'': 'src'},

      classifiers = {}, #searchability stuff

      long_description = long_description,
      long_description_content_type="text/markdown",

      install_requires = [], #dependencies for running package

      extras_require = { #dependencies for developing package
            "dev": [
                  "pytest>=3.7",
                  ],
      },

      url = "",
      author = "Daumantas Lipskis",
      author_email = "",
      
      )