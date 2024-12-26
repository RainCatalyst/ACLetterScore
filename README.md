# Animal Crossing Letter Scoring

This is a simple project that tries to generate a letter that gets a maximum possible score as per [Animal Crossing letter system](!https://jamchamb.net/projects/animal-crossing-letters) article by [Jamchamb](!https://github.com/jamchamb).

I use a simple genetic algorithm to maximize the score for a 162 character letter.
 

## Best letter
One of the best letter I've gotten after running it for a while is this:
```
 E!.?R??G??C?!E!?C???Ri...D..J??!L??!H!.O.!?W?..K?!?Y!N?
 !I.??F!?E???PB.!?X?!.U!?.M?!.U?!!Y!!O!?!J.?!P?.G?!Z.??T
 ..L.I?!.Sf???W!?!X???F.?.Sa!??V?X..E?.S.?O.?.W!.?P!
```
Which scores a total of **1020 points**.

*Note that there are no newlines in the original string.*
## Usage
The project has no extra dependencies. You can just run:
```bash
python ./main.py
```