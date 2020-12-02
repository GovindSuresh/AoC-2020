# AoC-2020

Solutions to Advent of Code 2020 problems https://adventofcode.com/

Full questions can be found on the website, I've paraphrased them below in case the website ever goes down. 

Each day's problems have been put into a separate folder. In certain cases I've provided multiple solutions (always good to practice with various approaches!)

### Day 1:

**Problem 1:**

Given a list of numbers. Find two numbers that sum to 2020 and then multiply those two numbers together.

Example 
```
1721
979
366
299
675
1456
```
In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Your puzzle answer was `538464`.

**Problem 2:**

Problem 2 involved doing the same thing, only finding combinations of 3 numbers that add up to 2020 and then finding the product.

Your puzzle answer was `278783190`.

### Day 2:

**Problem 1:**

Find all the valid passwords in the given list.

EXAMPLE
```
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
```

Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, `cdefg`, is not; it contains no instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.

How many passwords are valid according to their policies?

Your puzzle answer was `434`.

**Problem 2:**

In this scenario, each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

`1-3 a: abcde` is valid: position 1 contains a and position 3 does not.

`1-3 b: cdefg` is invalid: neither position 1 nor position 3 contains b.

`2-9 c: ccccccccc` is invalid: both position 2 and position 9 contain c.

How many passwords are valid according to the new interpretation of the policies?

Your puzzle answer was `509`.