# PLP Python Week 3 Assignment

## Description
This repository contains two Python scripts demonstrating conditional logic, loops, basic math operations, and error debugging.

## Files
* `grade_reporter.py`: Reads a list of student test scores, assigns letter grades (A, B, C, F), counts passes and failures, and calculates the overall rounded average score.
* `bug_hunt.py`: A fixed Python script that calculates the sum of numbers from 1 to 5, featuring explicit `# BUG:` comment documentation for three resolved syntax, logic, and type errors.

## Reflection Questions

**Which bug in Part B was hardest to find?**
The off-by-one logic bug (`while count < 5`) was the hardest to find because Python executed the code without raising any syntax or runtime errors. 

**How did you know something was wrong when there was no error message?**
I knew something was wrong because the prompt specified that the expected result for adding numbers 1 to 5 was `15`, but the code printed `10`. By tracing the loop iteration values manually (`1 + 2 + 3 + 4`), it became clear that the loop exited prematurely before adding `5`.
