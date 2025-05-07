from openai import AzureOpenAI


def combat_action(franchise1="Game of Thrones",
                  character1="Tyrion Lannister",
                  franchise2="Star Wars",
                  character2="Cassian Andor"):
    """
    Describe combat scenarios using fictional characters.
    """
    client = AzureOpenAI()

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an in popular film franchises, for example Marvel, DC, Star Wars and Game of Thrones."},
            {"role": "user", "content": f"Tell me who would win in a fictional fight between "
                                        f"the character {character1} from the franchise {franchise1} and "
                                        f"the character {character2} from the franchise {franchise2}. "
                                        f"Take into account the characters' physical strengths, powers and intellectual strengths."
                                        f"Identify each character's top 3 strengths in combat."
                                        f"Identify one weakness for each character."
                                        f"Assume that both characters have time to prepare and are aware of who their opponent is."
                                        f"If a character has appeared as different versions in multiple media, use the version in the media that is the most popular (e.g. movies vs comics)."
                                        f"If the 2 characters are usually depicted in similar environments, assume that environment will serve as the combat environment."
                                        f"If the 2 characters are usually depicted in very different environments, assume that the combat environment will be a moderately large outdoor space."
                                        f"Each character will be allowed to use the tools they are most often depicted with, otherwise they will be limited to the tools available in the combat environment."
                                        f"You can equivocate but you must identify the most likely victor."},
        ],
    )

    print(completion.choices[0].message.content)