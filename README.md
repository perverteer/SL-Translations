This is the translation repository for Sisterly Lust. Please create a GitHub account to start contributing translations. If your language isn't listed in the repository, please contact me via [Discord](https://discord.gg/CG7h8EC) so I can set everything up for you.

# How to use GitHub?
After creating your GitHub account you can work on the files in this repository.

Simply navigate to the language of your choice and open one of the .rpy files and click on the pencil icon on the top-right bar. This will open GitHub's online editor where you can make the changes you want. After you're finished you can click "Propose changes" to save your work.

Once your finished editing all of the files you need to bundle up all of the changes as a pull request. Click the green button called "Create pull request". A form will appear allowing you to detail your changes, once everything has been filled out you can create the pull request and it will appear in the list of pending requests.

The pending requests will be reviewed once I'm able. Until that time you can alter your pull request if you want to make any changes.

After I've reviewed your request it will be officially merged into the repository. The translation will then be included in the game and your contributions will be mentioned in the credits of the game.

# How to translate?
This game is written in [Ren'Py](https://www.renpy.org) and translating is relatively simple. There are two types of translation blocks, the first is the most common:

```python
# game/episode000.rpy:01
translate german episode000_c0c093d4:

    # narrator "It was a dark and stormy night."
    narrator ""
```
The first line denotes the location of the translation in the original game code. The line with the hash (#) in front is the original English dialogue. The translation would in this case go between the empty quotes. And looks like the following:
```python
# game/episode000.rpy:01
translate german episode000_c0c093d4:

    # narrator "It was a dark and stormy night."
    narrator "Es war eine dunkle und stürmige Nacht"
```
A different translation block is this one:
```python
translate german strings:

    # game/script.rpy:00
    old "Stormy Night"
    new ""
```
The translation:
```python
translate german strings:

    # game/script.rpy:00
    old "Stormy Night"
    new "Stürmige Nacht"
```
## Ren'Py markup
Ren'Py has several tags to mark up text, to make it bold or italic for example. This would make a word italic:
```python
    narrator "It was {i}a dark and stormy{/i} night."
```
The engine also allows for variables to be used in text, these need to be wrapped in square braces:
```python
    narrator "Es war eine dunkle und stürmige Nacht, wouldn't you say [p_name]."
```
In this case `[p_name]` will be replaced with whatever variable has been set.

Another tag that is used often in the game is `{w}` which denotes a pause in dialogue.

## Quotes and special characters
Please note that double quotes used inside the existing quotes need to be escaped. This line will cause an error:
```python
    narrator "Es war "eine dunkle" und stürmige Nacht"
```
Because it should be escaped like this:
```python
    narrator "Es war \"eine dunkle\" und stürmige Nacht"
```
There are other characters like these (a percentage sign, %, for example) which also need to be escaped like shown above.

If you have any further questions let me know via [Discord](https://discord.gg/CG7h8EC).