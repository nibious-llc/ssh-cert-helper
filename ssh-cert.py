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
	sshDir = str(Path.home()) + "/.ssh/"
	for file in os.listdir(sshDir):
		if fnmatch.fnmatch(file, '*-cert.pub'):
			with open(sshDir + file, 'r') as f:
				results.append({ 'file': file, 'contents': f.readline().split(" ")[1].strip()}) # Get just the key part
	return results

def getListOfCurrentLoadedCertificates():
	p = subprocess.Popen(['ssh-add', '-L'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	stdout, stderr = p.communicate()
	result = []
	for s in [ x for x in str(stdout).split('\\n')  if "cert" in x]:
		result.append(s.split(" ")[1].strip()) # get just the key part
	return result

def main():
	""" Main entry point of the app """
	certs = getListOfCertificates()
	loadedCerts = getListOfCurrentLoadedCertificates()
	for pubkey in certs: 
		if pubkey['contents'] not in loadedCerts:
			os.system(f"ssh-add ~/.ssh/{pubkey['file'][:-9]}")


if __name__ == "__main__":
	main()