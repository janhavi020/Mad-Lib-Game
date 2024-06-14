import random
story_templates = [
    """
    Once upon a time in a {adjective} land, there lived a {noun1} named {name}.
    {name} loved to {verb1} every day. One day, a {adjective2} {noun2} appeared
    and asked {name} to join them in a quest to find the {adjective3} {noun3}.
    They {verb2} together and had the most {adjective4} adventure ever.
    """,
    """
    In a {adjective} forest, there was a {noun1} named {name}. 
    {name} liked to {verb1} while the {adjective2} {noun2} watched.
    One day, they decided to explore a {adjective3} {noun3} nearby. 
    They {verb2} all the way and had a {adjective4} time.
    """,
    """
    On a {adjective} day, {name} the {noun1} decided to {verb1}.
    While {verb1}, {name} found a {adjective2} {noun2}.
    The {noun2} told {name} about a {adjective3} {noun3}.
    They {verb2} together and discovered it was the most {adjective4} thing ever.
    """
]

story_template = random.choice(story_templates)
print("Enter the words to complete the story")


def get_user_input():
    user_inputs = {
        "adjective": input("Enter an adjective: "),
        "noun1": input("Enter a noun: "),
        "name": input("Enter a name: "),
        "verb1": input("Enter a verb: "),
        "adjective2": input("Enter another adjective: "),
        "noun2": input("Enter another noun: "),
        "adjective3": input("Enter another adjective: "),
        "noun3": input("Enter another noun: "),
        "verb2": input("Enter another verb: "),
        "adjective4": input("Enter another adjective: ")
    }
    return user_inputs


def create_story(template, user_inputs):
    story = template.format(
        adjective=user_inputs["adjective"],
        noun1=user_inputs["noun1"],
        name=user_inputs["name"],
        verb1=user_inputs["verb1"],
        adjective2=user_inputs["adjective2"],
        noun2=user_inputs["noun2"],
        adjective3=user_inputs["adjective3"],
        noun3=user_inputs["noun3"],
        verb2=user_inputs["verb2"],
        adjective4=user_inputs["adjective4"]
    )
    return story


user_inputs = get_user_input()
completed_story = create_story(story_template, user_inputs)
print("Your completed story:")
print(completed_story)
