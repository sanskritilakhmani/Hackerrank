"""
Kevin and Stuart want to play the 'The Minion Game'.
Game Rules:
Both players are given the same string, S.
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels. 
The game ends when both players have made all possible substrings. 
Scoring
A player gets +1 point for each occurrence of the substring in the string S.
For Example:
String S = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points. 
Your task is to determine the winner of the game and their score.
Input Format
A single line of input containing the string S. 
Note: The string S will contain only uppercase letters: [A-Z].
Output Format
Print one line: the name of the winner and their score separated by a space.
If the game is a draw, print Draw.
Question Link: https://www.hackerrank.com/challenges/the-minion-game/problem
Sample Input
BANANA
Sample Output
Stuart 12
"""
1.
def minion_game(string):
    vowels = 'AEIOU'
    k,s = 0,0
    l =len(string)
    for i in range(l):
        if string[i] in vowels:
            k += (l-i)
        else:
            s += (l-i)
    if k > s:
        print("Kevin", k)
    elif k < s:
        print("Stuart", s)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
2.
