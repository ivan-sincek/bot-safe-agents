#!/usr/bin/env python3

import os, random

DEFAULT_USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"

def get_all():
	tmp = []
	file = os.path.join(os.path.abspath(os.path.split(__file__)[0]), "user_agents.txt")
	if os.path.isfile(file) and os.access(file, os.R_OK) and os.stat(file).st_size > 0:
		with open(file, "r", encoding = "UTF-8") as stream:
			for line in stream:
				line = line.strip()
				if line:
					tmp.append(line)
	return tmp if tmp else [DEFAULT_USER_AGENT]

def get_random():
	tmp = get_all()
	return tmp[random.randint(0, len(tmp) - 1)]
