# Autopush Load-Tester

The Autopush Load-Tester is an integrated tester and load-tester for the Mozilla
Services autopush project. It's intented to verify proper functioning of
autopush deployments under various load conditions.

## Getting Started

`ap-loadtester` uses PyPy 4.0.1 which can be downloaded here:
http://pypy.org/download.html

You will also need virtualenv installed on your system to setup a virtualenv for
`ap-loadtester`. Assuming you have virtualenv and have downloaded pypy, you
could then setup the loadtester for use with the following commands:

    $ tar xjvf pypy-4.0.1-linux64.tar.bz2
    $ virtualenv -p pypy-4.0.1-linux64/bin/pypy apenv
    $ source apenv/bin/activate
    $ pip install --upgrade pip

The last two commands activate the virtualenv so that running python or pip on
the shell will run the virtualenv pypy, and upgrade the installed pip to the
latest version.

You can now either install `ap-loadtester` as a [program](#program-use) to run
test scenarios you create, or if adding scenarios/code to `ap-loadtester`
continue to [Developing](#developing).

## Program Use

Install the `ap-loadtester` package:

    $ pip install ap-loadtester

Run the basic scenario against the dev server:

    $ aplt_scenario wss://autopush-dev.stage.mozaws.net/ aplt.scenarios:basic

## Developing

Checkout the code from this git repo and install the dependencies
Now install the requirements for `ap-loadtester`, and run the package setup for
the command line script to be ready:

    $ python setup.py --develop
