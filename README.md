# Advent-of-Code-2023

My goal for this year is to earn 25 of 50 possible stars. Seems reasonable? 

## Things I've learned about my coding:
* I don't like clutter. For Day 3, I put the `get_lines` function utilities.py file to import. Much better than the copy-paste solution from Days 1 and 2.
* When I first started AoC in 2020, Python (and thinking like a coder) was as much of a challenge as the actual challenges. Now I am more fluent and the coding feels more fluid, so I can spend more time on the mathematical puzzle part of the challenge. Sometimes.
* Less about my own coding and more of an observation about AoC: as the month continues, Part 1 can almost always be solved with brute force, but Part 2 requires a mathematically elegant solution.

## Stars earned (as of 12/9): 14

## Day 09: Mirage Maintenance
* Part 1 sample run works; input run gives me a number that is too big. Debugging is a hassle. Will have to get back to it.

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


