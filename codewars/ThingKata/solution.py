class Thing:
    def __init__(self, name):
        self.name = name
        self.attributes = set()
        self.is_a = _AttributeSetter(self, True)
        self.is_not_a = _AttributeSetter(self, False)

    def __getattr__(self, attr):
        if attr.startswith('is_a_'):
            attribute = attr[5:].replace('_', ' ')
            return attribute in self.attributes
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{attr}'")

class _AttributeSetter:
    def __init__(self, thing, is_adding):
        self.thing = thing
        self.is_adding = is_adding

    def __getattr__(self, attr):
        attr_name = attr.replace('_', ' ')
        if self.is_adding:
            self.thing.attributes.add(attr_name)
        else:
            self.thing.attributes.discard(attr_name)
        return self.thing

# Example usage:
jane = Thing('Jane')
jane.is_a.person
jane.is_a.woman.is_not_a.man

print(jane.is_a_person)  # => True
print(jane.is_a_woman)   # => True
print(jane.is_a_man)     # => False
print(jane.is_a_chicken)
