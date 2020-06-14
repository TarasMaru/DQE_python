from xml.etree.ElementTree import iterparse


def parse_and_remove(filename, path):
    path_parts = path.split('/')
    doc = iterparse(filename, ('start', 'end'))
    # Skip the root element
    next(doc)
    tag_stack = []
    elem_stack = []
    for event, elem in doc:
        if event == 'start':
            tag_stack.append(elem.tag)
            elem_stack.append(elem)
        elif event == 'end':
            if tag_stack == path_parts:
                yield elem
            try:
                tag_stack.pop()
                elem_stack.pop()
            except IndexError:
                pass


if __name__ == "__main__":

    mode = None  # if = 'n' - simple version of HW , 'y'- "complex" version of HW

    government_types = set()  # set of government types for both HW versions

    countries = parse_and_remove('mondial-3.0.xml', 'country')  # generator: produces country objects from XML

    while mode not in ['n', 'y']:
        mode = input("Should I take into account only countries with complex name (2+ words in name)? y/n | ")

    if mode == 'y':
        for country in countries:
            if " " in country.find("name").text.strip():  # check if space is present in a country name
                government_types.add(country.get('government').strip())
    else:
        for country in countries:
            government_types.add(country.get('government').strip())

    print(government_types, f'\nNumber of government types: {len(government_types)}')

