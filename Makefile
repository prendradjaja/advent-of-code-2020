.PHONY: run

SHELL=/bin/bash

run:
	python3 a.py in | tee >(tail -n1 | pbcopy)
