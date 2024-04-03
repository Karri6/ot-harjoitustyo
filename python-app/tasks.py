"""
Invoke file to start, test and get the coverage report of the tests.
"""

from invoke import task

@task
def start(c):
    c.run("python src/main.py")

@task
def test(c):
    c.run("pytest")

@task
def coverage_report(c):
    c.run("coverage run -m pytest")
    c.run("coverage html")
    