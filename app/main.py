class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: dict) -> None:
    person_list = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        if "wife" in person and person["wife"]:
            person_instance = Person.people[person["name"]]
            person_instance.wife = Person.people[person["wife"]]
        elif "husband" in person and person["husband"]:
            person_instance = Person.people[person["name"]]
            person_instance.husband = Person.people[person["husband"]]

    return person_list