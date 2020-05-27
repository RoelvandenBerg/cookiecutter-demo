# cookiecutter-demo
Introduction

Usage, etc.


## Installation

We can be installed with:

```bash
pip install cookiecutter-demo
```


(TODO: after the first release has been made)


## Development installation of this project itself

We're installed with [pipenv](https://docs.pipenv.org/), a handy wrapper
around pip and virtualenv. Install that first with `pip install pipenv`. Then run:

```bash
PIPENV_VENV_IN_PROJECT=1 pipenv install --python 3.8 --dev
```

In case you do not have python 3.8 on your machine, install python using 
[pyenv](https://github.com/pyenv/pyenv) and try the previous command again.

There will be a script you can run like this::

```bash
pipenv run cookiecutter-demo
```

It runs the `main()` function in `cookiecutter-demo/scripts.py`,
adjust that if necessary. The script is configured in `setup.py` (see
`entry_points`).

In order to get nicely formatted python files without having to spend manual
work on it, run the following command periodically:

```bash
pipenv run black cookiecutter_demo
```

Run the tests regularly. This also checks with pyflakes, black and it reports
coverage. Pure luxury:

```bash
pipenv run pytest
```

If you need a new dependency (like `requests`), add it in `setup.py` in
`install_requires`. Afterwards, run install again to actually install your
dependency:

```bash
pipenv install --dev
```

## Releasing 
Pipenv installs zest.releaser which allows you to release the package to a git(hub) repo. It has a 
`fullrelease` command that asks you a few questions, which you all respond to with `<enter>`:

```bash
pipenv run fullrelease
```


## Steps to do after generating with cookiecutter

- Add a new project on https://github.com/PDOK/ with the same name. Set
  visibility to "public" and do not generate a license or readme.

  Note: "public" means "don't put customer data or sample data with real
  persons' addresses on github"!

- Follow the steps you then see (from "git init" to "git push origin master")
  and your code will be online.

- Go to
  https://github.com/PDOK/cookiecutter-demo/settings/collaboration
  and add the teams with write access (you might have to ask someone with
  admin rights to do it).

- Once you installed with pipenv, add Pipfile.lock to git: `git add Pipfile.lock` and commit it to your repo. 

- Update this readme. Use [markdown](https://commonmark.org/) as the format.

- Ask Roel for a review.

- Remove this section as you've done it all :-)
