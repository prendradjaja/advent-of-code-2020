.PHONY: run

SHELL=/bin/bash

run:
	python3 b.py in | tee >(tail -n1 | pbcopy)
