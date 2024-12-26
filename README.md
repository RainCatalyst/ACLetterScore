# Animal Crossing Letter Scoring

This is a simple project that tries to generate a letter that gets a maximum possible score as per [Animal Crossing letter system](!https://jamchamb.net/projects/animal-crossing-letters) article by [Jamchamb](!https://github.com/jamchamb).

I use a simple genetic algorithm to maximize the score for a 162 character letter.
 

## Best letter
One of the best letter I've gotten after running it for a while is this:
```
..A...A...A...A...A ...A..A...A..A..A.A...A...A...A ...
A.A...A...A...A..A..A...A ...A...A...A...A..A..A...A...
A...A. .A..A...A...A..A...A ...A...A.A...A..A...AA .
```
Which scores a total of **1120 points**.

*Note that there are no newlines in the original string.*
## Usage
The project has no extra dependencies. You can just run:
```bash
python ./main.py
```