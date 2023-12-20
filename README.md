# Advent-of-Code-2023

My goal for this year is to earn 25 of 50 possible stars. Seems reasonable? 

## Things I've learned about my coding:
* I don't like clutter. For Day 3, I put the `get_lines` function utilities.py file to import. Much better than the copy-paste solution from Days 1 and 2.
* When I first started AoC in 2020, Python (and thinking like a coder) was as much of a challenge as the actual challenges. Now I am more fluent and the coding feels more fluid, so I can spend more time on the mathematical puzzle part of the challenge. Sometimes.
* Less about my own coding and more of an observation about AoC: as the month continues, Part 1 can almost always be solved with brute force, but Part 2 requires a mathematically elegant solution.

## Stars earned (as of 12/19): 24

## Day 19: 🌟 Aplenty
* Oh my stars, I got the Part 1 star on the first submit.
* Created classes for Workflow and Rule ... it got a little awkward (had to implement try/except block) but anyway it works. 

## Day 18: Lavaduct Lagoon
* Too many wonderful life events to have time for (or even read) today's challenge.

## Day 17: Clumsy Crucible
* I might consider this one a wash: read through the problem statement but worked on Day 16 instead. Now I have other things to do. Since I only need two more stars to meet my goal, I'm okay letting this one go for now.

## Day 16: 🌟 🌟 The Floor Will Be Lava
* Careful, careful function definitions -- I got everything else working before tackling the splitters.
* Re-used a handy, little function of compass directions from Day 10 and then again for a turn 90 degrees function. Here is the U-turn:
```
def get_180_dir(dir):
    compass = 'NESW'
    i = compass.index(dir)
    return compass[(i+2)%4]
```
* used a named tuple for the Beam
* treated functions as first class objects in a dictionary lookup in the `take_step` function
* I think this one is pretty readable.
* Solved Part 2 with brute force -- calculated energy for 440 different starting beam configurations. Not sure how else to do it.
  
## Day 15: 🌟 Lens Library
* The hardest part here was understanding the problem statement. Straightforward solve.

## Day 14: Parabolic Reflector Dish
* Started but had other things to do

## Day 13: 🌟 Point of Incidence
* Started on the 13th but ran out of time to debug
* So it turns out there can be more than one potential line of reflection! Gotta test 'em all.
* Used pandas and the transform `.T` method so one function could be used for both horizontal and vertical reflections.

## Day 12: Hot Spring
* Skipped -- to much else going on (not a bad thing!). Also it didn't look fun.

## Day 11: 🌟 🌟 Cosmic Expansion
* Part 1 is a straightforward solve, easy star
* Part 2 is an example of when not to use brute force! Gonna pull out a pen and paper and do some math.

## Day 10: 🌟 Pipe Maze
* This stymied me for a while -- what kind of data structure? How do I keep track of everything? Discussion with resident developer about treating each tile as an object got me started on the right path, pun intended.
* Biggest insight was that there was no need to keep track of every possible tile, just the tiles on the path. If I'm remembering previous years' challenges correctly, I have taken the hard way before, so this is an improvement.
* Part 1 is readable enough. Will take a break before getting to Part 2.
* ....Oh, Part 2 needs some serious thought and I just don't have it in me right now. [Visual demo](https://imgur.com/a/ukstWKO) of a solution found on reddit is nice.
* I started it anyway and I feel like it should work...but the answer is too high. I'm not sure how to debug. Not sure if I want to spend any more time.

## Day 09: 🌟 🌟 Mirage Maintenance
* Part 1 sample run works; input run gives me a number that is too big. Debugging is a hassle. Will have to get back to it.
* Debugging credit to my resident developer who noted my logical error in the assumption that all input values are positive. Got it!
* ALSO had a good discussion about how this is a good example of when to use a stack instead of a list. If I were to ever re-write this, I'd use that data structure. I'm sure there will be another opportunity in a future challenge.
* Part 2 achieved in short order...just had to look for first values instead of last values, and subtract instead of add...anyway, thank goodness because I'm ready to stop thinking about this.

## Day 08: 🌟 🌟 Haunted Wasteland
* I was almost taken in by the discussion of nodes, thinking that I would need to bring in NetworkX. But no! This does not require such a complication -- very straightforward solve. I used a dictionary of named tuples (I just love a named tuple) and a while loop. First star achieved in short order!
* My intuition about avoiding brute force to solve Part 2 was a good one here (and confirmed by resident developer). Use the least common multiple of all paths lengths to get the answer. 
* Built in `lcm` function from the `math` package doesn't take a list ... it takes an *unpacked* list! Used the `*` iterable unpacking operator. So convenient!

## Day 07: 🌟 Camel Cards
* This challenge is great for practicing object oriented programming! I learned a lot! Including implementing a new-to-me dunder method, `__hash__` which gave me the tie-breaker sort for free!
* However, part 1 is taking a long time so I will wait on part 2 for another day...off in the future.
* UGH it works on the sample but gets hung up in an endless while loop for the input. I gotta go live my life. ~~Will work on it tomorrow.~~ My resident developer fixed my eternal loop. 
* Despite the Deus ex Machina, I am super proud of the class I created and all of its dunder methods. This is a big advance for me.

## Day 06: 🌟 🌟 Wait for It
* Ah, finally a day where the parsing is easy, and so is the problem! Part 1 with brute force. Just waiting for the other shoe to drop.
* About that other shoe...a little algebra goes a very long way. No need to do billions of calculations! The roots of a binomial are all we need, plus a little massaging to get integer values.

## Day 05: 🌟 If You Give a Seed a Fertilizer
* Again, the hardest part was parsing! I was having a tough time getting the processing to move on to the next category once the location changed. I did some gymnastics to make it work. Not so pretty.
* For part 2, brute force is not going to work. I need to think about how to solve it. I'll have to return (some day) when I have time.

## Day 04: 🌟 🌟 Scratch Cards
* First star is straightforward: used lots of built-in Python capabilities with string parsing and list comprehensions
* Second star had the potential to be a real PITA, but I slowed down and figured out exactly the algorithm -- thankfully there was no need for recursion, just normal ol', nested for loops.

## Day 03: 🌟 🌟 Gear Ratios
* I remember similar problems in past years where we had to check values "around" other values in an array. This year my solution feels more natural than in the past -- my implementation is less baroque, more straightforward. Perhaps I've matured as a programmer.
* Off by one errors...sigh
* My original thought was to parse the lines into a dataframe but reconsidered. Used regex and named tuples in the solution.
* The named tuple in part 1 came in handy for part 2. I figured out my algorithm while I was on a walk. I hope my solution is readable to future me.

## Day 02: 🌟 🌟 Cube Conundrum

* The most challenging aspect was parsing the input.
* Daily use of pandas made this a straightforward solve to earn both stars

## Day 01: 🌟 🌟 Trebuchet

* Ugh slicing strings! I'm sure there is a prettier way to accomplish this. Finally got the second star. 
* I ran into parsing trouble, ~~but I'm not sure what the solution is (yet). Will probably come back to it. Will think on it.~~


