#!/usr/bin/python3
"""Function to indent text"""


def text_indentation(text):
    """Replace ., ?, and : with \n\n
    Raises: TypeError if text is not a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    paragraphs = []  # A list to store the paragraphs

    # Split the text into paragraphs based on ., ?, or :
    current_paragraph = ""
    for char in text:
        current_paragraph += char
        if char in ".?:":
            paragraphs.append(current_paragraph.strip())
            current_paragraph = ""

    # Add the last paragraph if there's any remaining text
    if current_paragraph:
        paragraphs.append(current_paragraph.strip())

    # Print the paragraphs with indentation
    for paragraph in paragraphs:
        print(paragraph + "\n")

