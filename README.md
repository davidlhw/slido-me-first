# Slido Vote Me

A simple vote bot for the audience interaction tool Slido (sli.do) made in Python.

## Installation

Clone the project:
```bash
git clone https://github.com/DavidLHW/slido-me-first.git
```

Install dependencies:
```shell
python -m pip install -r requirements.txt
```
    
This project runs on Python version >= 3.7.6.

## Usage
To use the bot, you need the following:
*   Url to the Slido event
*   Question id
*   Number of vote to add

### Running the bot

Simply copy the following to a terminal:

```
python vote.py -u <url> -q <question> -v <vote count>
```

### Getting the required data
1.  Url to the Slido event

    This will be the same url that is sent to you by the presenter.

2.  Question to raise

    This will be the question you wish to raise and add the votes to.

> Note:
>
> There is no limit to number of votes that you can add but the time taken to execute
> will scale linearly.
    

<br>

Have fun watching your questions get noticed!
