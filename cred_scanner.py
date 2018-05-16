import os
import re
import sys
import click

@click.command()
@click.option('--path', default='.', help='Path other than the local directory to scan')
@click.option('--secret', is_flag=True, help='Also look for Secret Key patterns. This may result in many false matches due to the nature of secret keys.')
def scan(path, secret):
    fail = False
    for dirname, dirnames, filenames in os.walk(path):
        # print path to all subdirectories first.
        for subdirname in dirnames:
            print(os.path.join(dirname, subdirname))

        # print path to all filenames.
        for filename in filenames:
            click.echo(os.path.join(dirname, filename))
            f = open(os.path.join(dirname, filename))
            if secret:
                pattern = re.compile('(?<![A-Z0-9])[A-Z0-9]{20}(?![A-Z0-9])|(?<![A-Za-z0-9/+=])[A-Za-z0-9/+=]{40}(?![A-Za-z0-9/+=])')
            else:
                pattern = re.compile('(?<![A-Z0-9])[A-Z0-9]{20}(?![A-Z0-9])')
            try:
                for i, line in enumerate(f):
                    for match in re.finditer(pattern, line):
                        click.secho('Found AWS Access Key in ' + os.path.join(dirname, filename,), fg='red')
                        fail = True
            except UnicodeDecodeError:
                click.secho("Can't scan file due to type: " + os.path.join(dirname, filename), fg='red')
                pass
    if fail == True:
        sys.exit(1)
if __name__ == "__main__":
    scan()