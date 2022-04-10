from invoke import task

'''starts executing application, use:
    $ poetry run invoke start'''
@task
def start(ctx):
    ctx.run('python3 src/index.py', pty=True)


'''executes tests using pytest, use:
    $ poetry run invoke test'''
@task
def test(ctx):
    ctx.run('pytest src')


'''executes coverage report, use:
    $ poetry run invoke coverage-report'''
@task
def coverage(ctx):
    ctx.run('coverage run --branch -m pytest src', pty=True)

@task(coverage)
def coverage_report(ctx):
    ctx.run('coverage html', pty=True)


'''formats code in src, use:
    $ poetry run invoke format
'''
@task
def format(ctx):
    ctx.run('autopep8 --in-place --recursive src', pty=True)

'''tests quality of code using pylint, use:
    $ poetry run invoke lint
'''
@task
def lint(ctx):
    ctx.run('pylint src')
