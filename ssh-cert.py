#!/usr/bin/env python3
"""
Add certificates to ssh agent when using ssh
"""

import os
import subprocess
import fnmatch
from pathlib import Path

__author__ = "Owen Parkins"
__version__ = "0.1.0"
__license__ = "LGPL2.1"


def getListOfCertificates():
	results = []
	sshDir = str(Path.home()) + "/.ssh"
	for file in os.listdir(sshDir):
		if fnmatch.fnmatch(file, '*-cert.pub'):
				results.append(file)
	return results

def getListOfCurrentLoadedCertificates():
	p = subprocess.Popen(['ssh-add', '-l'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	stdout, stderr = p.communicate()
	result = []
	for s in [ x for x in str(stdout).split('\\n')  if "CERT" in x]:
		cert = os.path.basename(s.split(" ")[2])
		result.append(cert)

	return result

def main():
	""" Main entry point of the app """
	certs = getListOfCertificates()
	loadedCerts = getListOfCurrentLoadedCertificates()
	
	for priv in [ x[:-9] for x in certs]: # remove the -cert.pub from file name
		if priv not in loadedCerts:
			os.system(f"ssh-add ~/.ssh/{priv}")


if __name__ == "__main__":
	main()