from setuptools import setup, find_packages

def read(filename):
    with open(filename) as f:
        return f.read()

setup(name = "rich-text",
      version = "0.1",
      description = "A format for representing rich text documents and changes.",
      long_description=read('README.md'),

      author = "Zosia Wisniowolska",
      author_email = "wisniowolska@gmail.com",
      url = "http://www.killerapps.pl",

      license = "MIT",

      packages=find_packages(),
      install_requires=["diff-match-patch", ])
