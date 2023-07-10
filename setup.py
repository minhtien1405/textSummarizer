import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


__version__ = "0.0.0"

REPO_NAME = "textSummarizer"
AUTHOR_USER_NAME = "minhtien1405"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "hoangleminhtien@gmail.com"

setuptools.setup(
  name = REPO_NAME,
  version = __version__,
  author = AUTHOR_USER_NAME,
  author_email = AUTHOR_EMAIL,
  description = "Text Summarizer",
  long_description = long_description,
  long_description_content_type = "text/markdown",
  url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
  package_dir={"": "src"},
  packages = setuptools.find_packages(where="src"),
)