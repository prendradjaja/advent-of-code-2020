N.B.: My solution skips the last passport. I manually added a newline to the last passport to account for this.

96/132 -- just barely on the leaderboard for part 1. Wow, that was a lot longer than the past couple days!

I got tripped up in a few places:

* Didn't know I can't do set.remove on a nonexistent item in Python -- just cost me a few seconds
* I wasn't that prepared for the sheer length of this compared to the previous problems -- really easy to mess up simple things like getting variable names wrong or forgetting that I need to care about declaring functions before using them when a problem takes ten minutes instead of three, since I can no longer hold all those things in my head.
   * At one point, to save time, I abbreviated the variable name `value` to `v` in one function but not another -- and inevitably used the wrong one in multiple places.
   * Declaring functions before using them: I think next time I'll use a `main` function :)
* [The Last Line Effect](https://www.viva64.com/en/b/0260/) in copy-paste code! Not actually the last line this time, but it's so easy to make a mistake like this one: (how fast can you spot it?)

    def h(v):
        if 'cm' in v:
            n, r = v.split('cm', maxsplit=1)
            return r == '' and 150 <= int(n) <= 193
        if 'cm' in v:
            n, r = v.split('in', maxsplit=1)
            return r == '' and 59 <= int(n) <= 76
        return False

That was the biggest (time-wise) mistake I made on part 2 -- had to try against `valid-examples.txt` and do some debugging. (You can see log calls in `b.py`!)
