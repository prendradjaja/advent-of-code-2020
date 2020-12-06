.PHONY: run

SHELL=/bin/bash

run:
	python3 s.py in | tee >(tail -n1 | pbcopy)
