# cred_scanner
A simple command line tool for finding AWS credentials in files. Optimized for use with Jenkins and other CI systems.

I suspect there are other, better tools out there (such as [git-secrets](https://github.com/awslabs/git-secrets/blob/master/git-secrets)), but I couldn't find anything to run a quick and dirty scan that also integrates well with Jenkins.

## Usage:

To install just copy it where you want it and install the requirements:

	pip install -r ./requirements.txt

This was written in Python 3.6.

To run:

	python cred_scanner.py 

That will scan the local directory and all subdirectories. It will list the files, which ones have potential access keys, and which files can't be scanned due to the file format. cred_scanner exits with a code of 1 if it finds any potential keys.

	Usage: cred_scanner.py [OPTIONS]

	Options:
	  --path TEXT  Path other than the local directory to scan
	  --secret     Also look for Secret Key patterns. This may result in many
	               false matches due to the nature of secret keys.
	  --help       Show this message and exit.

To run as a test in Jenkins just use the command line or add it as a step to your Jenkins build. Jenkins will automatically fail the build if it sees the exit code 1.