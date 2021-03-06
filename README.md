# Simple Password Cracker
*Notice: Password lists in data contain offensive passwords*

![build](https://travis-ci.org/michaellyons786/simple-password-cracker.svg?branch=master)

I wrote the simple password cracker as a tool to run an experiment on "haystacking", the practice of padding passwords to get low-entropy length added to a password. The purpose of this tool is *not* to crack passwords or to show the haystacking is bad practice. Rather, it's to show that simply adding padding to bad passwords doesn't make you safer. I hope to add a few more password analysis tools in my free time to illustrate complex concepts, such as password entropy, in simple terms. **Please**, if you notice any theoretical inaccuracies, bugs in my code, or have any suggestions, let me know! 

I have added the final project from my group project into the project directory. Since the end of my security class, I have made several improvements to the original code used to run the experiment.

## How It Works
There are no highfalutin heuristics at work here: the program simply checks combinations of left and right paddings and a password and finishes when it guesses correctly. If you feed it a password list that is too big (10k works okay), the program will take too long. If you feed it a pad list that is too big (around 5 works okay), then the program will take too long. A padding must all be the same character and can vary from no padding at all to 10 characters. The left and right padding can be constituted from different characters.

## Example 
![arguments](https://github.com/michaellyons786/simple-password-cracker/blob/master/data/arguments.png)
![finish](https://github.com/michaellyons786/simple-password-cracker/blob/master/data/finish.png)

### References
[Password lists](https://github.com/danielmiessler/SecLists)
