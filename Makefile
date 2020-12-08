.PHONY: run

SHELL=/bin/bash

run:
	python3 s.py | tee >(tail -n1 | pbcopy)
