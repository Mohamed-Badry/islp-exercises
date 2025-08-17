![ISLP Solutions Logo](./images/logo.svg)


[![deploy-book](https://github.com/Mohamed-Badry/islp-solutions/actions/workflows/deploy.yml/badge.svg?branch=main&event=push)](https://github.com/Mohamed-Badry/islp-solutions/actions/workflows/deploy.yml) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Mohamed-Badry/islp-solutions/main)

# Summary 

These are my solutions to the exercises in the book **An Introduction to Statistical Learning with Python** ([ISLP](https://www.statlearning.com/)).

I attempt to tackle both conceptual and applied exercises in these notebooks.

### Read the Book

If you're reading this from github, you can explore the full Jupyter Book here: [ISLP Solutions](https://mohamed-badry.github.io/islp-solutions/)

### Notes:
- Questions that involve sketching are done using matplotlib's `xkcd` theme.
- Mathematical proofs are mostly written using mathjax inside the markdown cells by wrapping the mathjax code in `$...$` like so $\alpha^2 + \beta_0 = \gamma$, though some were updated to use LaTeX align environments to be compatible with jupyter-book.
- I typed the questions in the notebooks for chapters `2` and `3`, but it was taking too much time so I stopped doing that from chapter `4` and on.

## Usage

+ You can either read the [jupyter book](https://mohamed-badry.github.io/islp-solutions/) online, or just view the notebooks on github.

- If you're viewing it through the jupyter book, you can launch the notebooks using the rocket icon on the top right in `google colab` or `binder` to experiment with them, keep in mind that you might have to run a few `pip` installs for the missing libraries on colab.

You can also just clone the repo and run it locally

```bash
git clone https://github.com/Mohamed-Badry/islp-solutions.git
cd islp-solutions
pip install -r requirements.txt
jupyter notebook
```

or build the book with
```bash
pip install -r requirements-book.txt
jupyter-book build .
```

Note: Preferrably do both in a venv or conda environemnt.


### Credits:

A big thank you to the authors of the original book **An Introduction to Statistical Learning with Python** for making such a great learning resource free, easily accessible, and creating a great course to accompany it. 

The notebooks are rendered using the wonderful [Jupyter Book](https://github.com/jupyter-book/jupyter-book/tree/main) project.