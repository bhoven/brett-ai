# Brett's Franchise Character Combat Simulator

This app uses AI to determine who will win in a battle with your favorite franchise characters. The parameters for these 
battles are:
1. The characters will have access to their normal tools.
2. If the characters are typically depicted in a similar environment, that will be used as the combat environment, otherwise a moderately sized outdoor space is assumed.

The app will list:
1. 3 strenghts of each character.
2. 1 weakness of each character.

A victor will always be determined! No ties!

### Usage:
Base command: `poetry run python brett/main.py combat`
Options:
* `sw`: Star Wars
* `got`: Game of Thrones
* `marvel`: Marvel
* `dc`: DC
* `franchise1`: A freeform franchise for a character. Must be paired with `character1`
* `character1`: A character from `franchise1`
* `franchise2`: A freeform franchise for a character. Must be paired with `character2`
* `character2`: A character from `franchise2`

### Example:
`poetry run python brett/main.py combat --sw "Darth Vader" --dc "Superman"`

### Prerequisites
```commandline
export AZURE_OPENAI_API_KEY={YOUR_TOKEN}
export AZURE_OPENAI_ENDPOINT={YOUR_ENDPOINT}
export OPENAI_API_VERSION={API_VERSION}
```

### Install
```bash
source ~/.zshrc
python -m venv venv
source venv/bin/activate
pip install -e .
```