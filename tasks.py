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
    ctx.run('coverage run --branch -m pytest', pty=True)

@task(coverage)
def coverage_report(ctx):
    ctx.run('coverage html', pty=True)
