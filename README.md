# Slido Vote Me

A simple vote bot for the audience interaction tool Slido (sli.do) made in Python.

## Installation

Clone the project:
```bash
git clone https://github.com/DavidLHW/slido-me-first.git
```

Install dependencies:
    python -m pip install -r requirements.txt

## Usage
To use the bot, you need the following:
*   Link to the Slido event
*   Question id
*   Number of vote to add

### Getting the required data
1.  Link to the Slido event

    This will be the same link that is sent to you by the presenter.

2.  Question id

    You'll need to access the slido page and inspect the page element to get the question id.
    
    ![cursor hovering on question](asset/event_page.jpg?raw=true)  
    <br>
    ![cursor hovering on question](asset/inspect_element_on_page.jpg?raw=true)

    Click on your question and copy the value for `data-qid` from the element (it is `48098225` in this case).

    ![copy data-qid value](asset/copy_data-qid.jpg?raw=true)

### Running the bot

Simply copy the following to a terminal:

```shell
python vote.py -u <url> -q <data-qid> -v <number of vote>
```

<br>

Have fun watching your questions get noticed!