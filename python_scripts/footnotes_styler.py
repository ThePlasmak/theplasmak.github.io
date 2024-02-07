import pyperclip


def add_span_class(text, excluded_words, class_name="transparent-text"):
    """
    Wrap each word in a span with a specified class, excluding certain words, while preserving newlines.

    :param text: The text to be processed.
    :param excluded_words: List of words to exclude from wrapping.
    :param class_name: The CSS class name to be applied.
    :return: The processed text with spans added.
    """
    # Splitting the text into lines and then words
    lines = text.split("\n")
    processed_lines = []

    for line in lines:
        words = line.split()
        processed_words = []

        for word in words:
            # Check if the word is in the excluded list
            if word in excluded_words:
                processed_words.append(word)
            else:
                # Wrap the word in a span with the specified class
                processed_word = f'<span class="{class_name}">{word}</span>'
                processed_words.append(processed_word)

        # Join the processed words back into a string and add to the lines
        processed_lines.append(" ".join(processed_words))

    # Join the processed lines back into a string with newlines
    return "\n".join(processed_lines)


text = """by Sarah Mak"""

excluded_words = ["John", "Lasseter.", "Disney", "Disney's"]

# Applying the function
processed_text = add_span_class(text, excluded_words)

pyperclip.copy(processed_text)
print(processed_text)
