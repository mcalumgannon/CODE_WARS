def change_case(phrase, target_case):
    # Check if the target_case is valid
    if target_case not in ['camel', 'snake', 'kebab']:
        return None

    # Handle the empty string
    if not phrase:
        return ''
    
    # Checks for uppercase in string
    def has_uppercase(string):
        for char in string:
            if char.isupper():
                return True
        return False

    
    # Check if the phrase is valid using function

    if '-' in phrase and '_' in phrase:    
        return None

    if any(character in '-_' for character in phrase) and has_uppercase(phrase):
        return None

    # Helper function to check if a characteracter is a valid word boundary
    def is_word_boundary(character):
        return character == '_' or character == '-'

    new_phrase = []
    is_new_word = True
    is_first_word = True

    for character in phrase:
        # Ensure that the phrase starts with a lowercase letter
        if is_new_word and character.isupper():
            new_phrase.append(character.lower())
            is_new_word == False

        if is_word_boundary(character):
            is_new_word = True
            if target_case == 'camel':
                continue  # Skip word boundaries for camelCase
            new_phrase.append('_' if target_case == 'snake' else '-')
        else:
            if target_case == 'kebab':
                new_phrase.append('-' + character.lower() if character.isupper() else character)
            elif target_case == 'snake':
                new_phrase.append('_' + character.lower() if character.isupper() else character)
            else:
                new_phrase.append(character.upper() if is_new_word and not is_first_word else character)
            is_new_word = False
            is_first_word = False

    return ''.join(new_phrase)
