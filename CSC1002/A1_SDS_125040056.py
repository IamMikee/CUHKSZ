import re

content = ""
cursor_pos = 0
cursor_active = True
help_text = """? - display this help info
. - toggle row cursor on and off
h - move cursor left
l - move cursor right
^ - move cursor to beginning of the line
$ - move cursor to end of the line
w - move cursor to beginning of next word
b - move cursor to beginning of current or previous word
e - move cursor to end of the word
i - insert <text> before cursor
a - append <text> after cursor
I - insert <text> from beginning
A - append <text> at the end
x - delete character at cursor
X - delete character before cursor
v - view editor content
q - quit program"""



def moveto_next_word(text, position):
    if position + 1 >= len(text) or not text: return position

    while position < len(text) and text[position].isalnum():
        position += 1

    next_word = re.search(r"\b\w", text[position:])
    return position + next_word.start() if next_word else len(text) - 1

def moveto_previous_word(text, position):
    if position == 0 or not text: return 0 #if text is empty and position already 0

    prev_words_pos = [word.start() for word in re.finditer(r"\b\w", text[:position])]
    return prev_words_pos[-1] if prev_words_pos else 0

def moveto_end_of_word(text, position):
    if position + 1 >= len(text) or not text: return position

    current_word = re.search(r"\w+\b", text[position + 1:])
    return position + current_word.end() if current_word else len(text)-1



def insert_before_cursor(text, position, new_text):
    return text[:position] + new_text + text[position:]

def append_after_cursor(text, position, new_text):
    if position == 0 and not text: return new_text, len(new_text) - 1
    return text[:position + 1] + new_text + text[position + 1:], position + len(new_text)

def insert_at_beginning(text, new_text):
    return new_text + text, 0

def append_at_end(text, new_text):
    return text + new_text, len(text) + len(new_text) - 1



def delete_on_cursor(text, position):
    if not text: return "", 0
    if len(text) - 1 == position: return text[:position], position - 1
    return text[:position] + text[position + 1:], position

def delete_before_cursor(text, position):
    if not text: return "", 0
    if position == 0: return text, 0
    return text[:position - 1] + text[position:], position - 1



def print_content(text, position, cursor_on):
    if cursor_on and text:
        print(f"{text[:position]}\033[42m{text[position]}\033[0m{text[position + 1:]}")
    else:
        print(text)



while True:
    try:
        prompt = input(">")

        if len(prompt) != 1 and prompt[0] not in ["i", "a", "I", "A"]: #failsafe for extra whitespaces
            continue

        match prompt[0]:
            case "?":
                print(help_text)
                continue

            case ".":
                cursor_active = not cursor_active

            case "h":
                if cursor_pos != 0:
                    cursor_pos -= 1

            case "l":
                if cursor_pos != len(content) - 1:
                    cursor_pos += 1

            case "^":
                cursor_pos = 0

            case "$":
                cursor_pos = len(content) - 1

            case "w":
                cursor_pos = moveto_next_word(content, cursor_pos)

            case "b":
                cursor_pos = moveto_previous_word(content, cursor_pos)

            case "e":
                cursor_pos = moveto_end_of_word(content, cursor_pos)

            case "i":
                content = insert_before_cursor(content, cursor_pos, prompt[1:])

            case "a":
                content, cursor_pos = append_after_cursor(content, cursor_pos, prompt[1:])

            case "I":
                content, cursor_pos = insert_at_beginning(content, prompt[1:])

            case "A":
                content, cursor_pos = append_at_end(content, prompt[1:])

            case "x":
                content, cursor_pos = delete_on_cursor(content, cursor_pos)

            case "X":
                content, cursor_pos = delete_before_cursor(content, cursor_pos)

            case "v":
                pass

            case "q":
                break

        print_content(content, cursor_pos, cursor_active)

    except:
        continue