# My solutions to [Advent of Code](https://adventofcode.com) 2020

## Me (elsewhere on the internet)

- [The leaderboard](https://adventofcode.com/2020/leaderboard)
- [YouTube](https://www.youtube.com/channel/UCFXfWAIJPc2b-wDn2YhfvyQ): Some screen recordings
- [Reddit](https://www.reddit.com/user/prendradjaja): Some more thoughts on various problems on /r/adventofcode

## Directory structure

Most directories have:

- `a.py`, `b.py` for parts 1 and 2

Some directories have:

- `aclean.py` or `bclean.py` for cleaned-up solutions that do not change the core idea
- `a2.py` or `b2.py` for alternate approaches
- `s.py` or `solution.py` if parts 1 and 2 make sense to combine into one file

The root directory has:

- My starter files, including
    - `s.py`: Main solution file
    - `in`: To be replaced with the problem's input
    - and a few more Python files with some reusable helpers
- `make-seed-dir.sh`, which creates a new directory and copies my starter files
