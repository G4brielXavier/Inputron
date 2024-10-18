![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Inputron)
![GitHub Repo stars](https://img.shields.io/github/stars/G4brielXavier/Inputron)


### Installing

```bash

pip install Inputron

```

### Using

```python

from Inputron import Inputron

inputron = Inputron()
```

### Inputron Library

<details>
    <summary>Inputron.Message</summary>

    Message(msg: str, title:str = "", space:bool = False, iserror:bool = False)

    Create better outputs messages, alerts with this function. 
        
    Arguments:
        <h5>msg</h5> {<code>String</code>} Set your message here.
        <h5>title</h5> {<code>String</code>} The Message Title. [Optional]
        <h5>space</h5> {<code>Bool</code>} If has space or not. [Optional] default=False
        <h5>iserror</h5> {<code>Bool</code>} If the message is to sinalize a error or not. [Optional] default=False
        <h5>alert</h5> {<code>Bool</code>} If True, add a Warn or Error after of title. [Optional] default=True
        <h5>separate</h5> {<code>String</code>} It's the separator among title and msg. [Optional] default="-"

</details>

<details>
    <summary>Inputron.Loading</summary>

    Loading(msg: str = "Loading", msgComplete: str = "Complete", speed: float = 0.1, repeatTimes: int = 10, icon: list = ["...", "°..", ".°.", "..°"])

    Create a loader in format of terminal, manage and the Icon.
        
    Arguments:
        <h5>msg</h5> {<code>String</code>} Set here your text to show while is loading.
        <h5>msgComplete</h5> {<code>String</code>} It is message that will be shown. [Optional]
        <h5>speed</h5> {<code>Float</code>} It is interval in each rotated. [Optional] default=0.1
        <h5>repeatTimes</h5> {<code>Int</code>} It is amount of time that the icon spins. [Optional] default=10
        <h5>icon</h5> {<code>List</code>} It is the icon strings, change to other if you want. [Optional] default=["...", "°..", ".°.", "..°"]

</details>

<details>
    <summary>Inputron.Ask</summary>

    Ask(ask:str, space:bool = True, isInt:bool = False, isFloat:bool = False, spaceleft:bool = True, beforesignal:str = ">", aftersignal:str = ":")

    Use this function to ask some information of user.
        
    Arguments:
        <h5>ask</h5> {<code>String</code>} It is your ask 
        <h5>space</h5> {<code>Bool</code>} If your asks will have spaces on top of below. [Optional] default=True
        <h5>isInt</h5> {<code>Bool</code>} If you want that be returned in Integer format. [Optional] default=False
        <h5>isFloat</h5> {<code>Bool</code>} If you want that be returned in Floating format. [Optional] default=False
        <h5>spaceleft</h5> {<code>Bool</code>} if you want that have a space in left side of ask. [Optional] default=True
        <h5>beforesignal</h5> {<code>String</code>} It's the signal before of ask. [Optional] default=">"
        <h5>aftersignal</h5> {<code>String</code>} It's the signal after of ask. [Optional] default=":"

</details>

<details>
    <summary>Inputron.YN</summary>

    YN(ask:str, title:str = 'Question', space:bool = True)

    Use this function to obtain two answer, Yes or No, you can change the options.
        
    Arguments:
        <h5>ask</h5> {<code>String</code>} It is your ask.
        <h5>title</h5> {<code>String</code>} It is the title of question. [Optional] default='Question'
        <h5>space</h5> {<code>Bool</code>} If your asks will have spaces on top or below. [Optional] default=True

    Return:
        Boolean: True to Yes and False to No.

</details>

<details>
    <summary>Inputron.QuestionOption</summary>

    QuestionOption(ask:str, title:str = 'Question', space:bool = True, options=["Option 1", "Option 2", "Option 3", "Option 4"])

    Use this function to obtain two answer, Yes or No, you can change the options.
        
    Arguments:
        <h5>ask</h5> {<code>String</code>} It is your ask.
        <h5>title</h5> {<code>String</code>} It is the title of question. [Optional] default='Question'
        <h5>space</h5> {<code>Bool</code>} If your asks will have spaces on top or below. [Optional] default=True
        <h5>options</h5> {<code>List</code>} It's your options. [Optional] default=["Option 1", "Option 2", "Option 3", "Option 4"]

    Return:
        String: It's return the option chosen.

</details>

<details>
    <summary>Inputron.AVG</summary>

    AVG(content:list, binsCalc:int = 4, isInt:bool = False, isFloat:bool = True, isStr:bool = False)

    Use this function to calc Average of numbers to Grades.
        
    Arguments:
        <h5>content</h5> {<code>List</code>} This is the list of numbers that will be used to calc.
        <h5>binsCalc</h5> {<code>Int</code>} It is the divider of calc. [Optional] default=4
        <h5>isInt</h5> {<code>Bool</code>} If the return is in integer format. [Optional] default=False
        <h5>isFloat</h5> {<code>Bool</code>} If the return is in floating format. [Optional] default=True
        <h5>isStr</h5> {<code>Bool</code>} If the return is in string format. [Optional] default=False

</details>



### Contributing

1. Do a fork of Repository.

2. Create a branch to your feature 
    `git checkout -b features/feature_name`

3. Do commits of your changes
    `git commit -am 'feature name'`

4. Send to the branch
    `git push origin features/feature_name`

5. Open a Pull Request 

# License

<p>This project is licensed under the MIT License.</p>







