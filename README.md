# Simple Password Cracker
*Notice: Password lists in data contain offensive passwords*
I wrote the simple password cracker as a tool to run an experiment on "haystacking", the practice of padding passwords to get low-entropy length added to a password. The purpose of this tool is *not* to crack passwords or to show the haystacking is bad practice. Rather, it's to show that simply adding padding to bad passwords doesn't make you safer. 

## How It Works
There are no highfalutin heuristics at work here: the program simply checks combinations of left and right paddings and a password and finishes when it guesses correctly. If you feed it a password list that is too big (10k works okay), the program will take too long. If you feed it a pad list that is too big (around 5 works okay), then the program will take too long. A padding must all be the same character and can vary from no padding at all to 10 characters. The left and right padding can be constituted from different characters.

## Example


### References
Password lists, https://github.com/danielmiessler/SecLists
