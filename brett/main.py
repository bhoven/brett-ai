import typer

app = typer.Typer()
from brett.actions.combat import combat_action
from brett.utilities.cli import option


@app.command()
def combat(
        franchise1: option(str, "Franchise 1") = None,
        character1: option(str, "Character 1") = None,
        franchise2: option(str, "Franchise 2") = None,
        character2: option(str, "Character 2") = None,
        sw: option(str, "Star Wars Character") = None,
        got: option(str, "Game of Thrones Character") = None,
        marvel: option(str, "Marvel Character") = None,
        dc: option(str, "DC Character") = None,
):
    if not franchise1 and not character1:
        franchise1, character1 = get_character_and_franchise(sw, got, marvel, dc)
    if not franchise2 and not character2:
        franchise2, character2 = get_character_and_franchise(sw, got, marvel, dc, 1)

    combat_action(franchise1, character1, franchise2, character2)

def get_character_and_franchise(sw, got, marvel, dc, i=0):
    character_list = []
    if sw:
        character_list.append(("Star Wars", sw))
    if got:
        character_list.append(("Game of Thrones", got))
    if marvel:
        character_list.append(("Marvel", marvel))
    if dc:
        character_list.append(("DC", dc))

    return character_list[i]

if __name__ == "__main__":
    app()