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
dw - delete to start of next word
de - delete to end of next word
db - delete to start of current or previous word
dc - delete whitespaces or entire word at cursor
sw - swap word at cursor with next word
sb - swap word at cursor with previous word
v - view editor content
q - quit program"""



def get_word_bounds(text, position):
    if not text or position < 0 or position >= len(text): return None
    left = right = position
    is_alphanumeric = True if text[position].isalnum() else False

    while left > 0 and text[left - 1].isalnum() == is_alphanumeric:
        left -= 1
    while right < len(text) - 1 and text[right + 1].isalnum() == is_alphanumeric:
        right += 1

    return left, right



def moveto_next_word(text, position):
    if position + 1 >= len(text) or not text: return position

    while position < len(text) and text[position].isalnum():
        position += 1

    while position < len(text) and not text[position].isalnum():
        position += 1

    return position if position < len(text) else len(text)-1

def moveto_previous_word(text, position):
    if position == 0 or not text: return 0

    prev_words_pos = [word.start() for word in re.finditer(r"\b\w", text[:position])]
    return prev_words_pos[-1] if prev_words_pos else 0

def moveto_end_of_word(text, position):
    if position + 1 >= len(text) or not text: return position

    current_word = re.search(r"\w+\b", text[position + 1:])
    return position + current_word.end() if current_word else len(text)-1



def insert_before_cursor(text, position, new_text):
    return text[:position] + new_text + text[position:]

def append_after_cursor(text, position, new_text):
    if not text: return new_text, len(new_text) - 1
    return text[:position + 1] + new_text + text[position + 1:], position + len(new_text)

def insert_at_beginning(text, new_text):
    return new_text + text, 0

def append_at_end(text, new_text):
    return text + new_text, len(text) + len(new_text) - 1



def delete_on_cursor(text, position):
    if not text: return "", 0
    if len(text) - 1 == position: return text[:position], max(0, position - 1)
    return text[:position] + text[position + 1:], position

def delete_before_cursor(text, position):
    if not text: return "", 0
    if position == 0: return text, 0
    return text[:position - 1] + text[position:], position - 1

def delete_next_word(text, current_position, next_word_pos):
    if not text: return "", 0
    if next_word_pos >= len(text) - 1: return text[:current_position], current_position
    else: return text[:current_position] + text[next_word_pos:], current_position

def delete_end_word(text, current_position, end_word_pos):
    if not text: return "", 0
    if end_word_pos >= len(text) - 1: return text[:current_position], current_position
    else: return text[:current_position] + text[end_word_pos + 1], current_position

def delete_prev_word(text, current_position, prev_word_pos):
    if not text: return "", 0
    if current_position <= prev_word_pos: return text, prev_word_pos
    else: return text[:prev_word_pos] + text[current_position + 1:], prev_word_pos

def delete_at_cursor(text, position):
    if not text: return "", 0

    start_of_word, end_of_word = get_word_bounds(text, position)
    new_text = text[:start_of_word] + text[end_of_word + 1:]
    deleted_len = end_of_word - start_of_word + 1

    if position > end_of_word: position -= deleted_len
    elif start_of_word <= position <= end_of_word: position = start_of_word
    return new_text, max(0, min(position, len(new_text) - 1))



def swap_next_word(text, position):
    if not (bounds := get_word_bounds(text, position)): return text, position
    left1, right1 = bounds

    next_pos = right1 + 1
    while next_pos < len(text) and not text[next_pos].isalnum():
        next_pos += 1

    if not (next_word := get_word_bounds(text, next_pos)): return text, position
    left2, right2 = next_word

    new_text = text[:left1] + text[left2:right2 + 1] + text[right1 + 1:left2] + text[left1:right1 + 1] + text[right2 + 1:]
    return new_text, left2 + (position - left1)

def swap_prev_word(text, position):
    if not (bounds := get_word_bounds(text, position)): return text, position
    left1, right1 = bounds

    prev_pos = left1 - 1
    while prev_pos >= 0 and not text[prev_pos].isalnum():
        prev_pos -= 1

    if not (prev_word := get_word_bounds(text, prev_pos)): return text, position
    left2, right2 = prev_word

    new_text = text[:left2] + text[left1:right1 + 1] + text[right2 + 1:left1] + text[left2:right2 + 1] + text[right1 + 1:]
    return new_text, left2 + (position - left1)



def print_content(text, position, cursor_on):
    if cursor_on and text:
        print(f"{text[:position]}\033[42m{text[position]}\033[0m{text[position + 1:]}")
    else:
        print(text)



while True:
    prompt = input(">")

    insert_cmds = ["i", "a", "I", "A"]

    if not prompt:
        continue

    if len(prompt) == 1 and prompt[0] in insert_cmds: #invalid parameters for i,a,I,A
        continue

    match prompt[0]:
        case "i":
            content = insert_before_cursor(content, cursor_pos, prompt[1:])

        case "a":
            content, cursor_pos = append_after_cursor(content, cursor_pos, prompt[1:])

        case "I":
            content, cursor_pos = insert_at_beginning(content, prompt[1:])

        case "A":
            content, cursor_pos = append_at_end(content, prompt[1:])

    match prompt:
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
            cursor_pos = max(0, len(content) - 1)

        case "w":
            cursor_pos = moveto_next_word(content, cursor_pos)

        case "b":
            cursor_pos = moveto_previous_word(content, cursor_pos)

        case "e":
            cursor_pos = moveto_end_of_word(content, cursor_pos)

        case "x":
            content, cursor_pos = delete_on_cursor(content, cursor_pos)

        case "X":
            content, cursor_pos = delete_before_cursor(content, cursor_pos)

        case "dw":
            content, cursor_pos = delete_next_word(content, cursor_pos, moveto_next_word(content, cursor_pos))

        case "de":
            content, cursor_pos = delete_end_word(content, cursor_pos, moveto_end_of_word(content, cursor_pos))

        case "db":
            content, cursor_pos = delete_prev_word(content, cursor_pos, moveto_previous_word(content, cursor_pos))

        case "dc":
            content, cursor_pos = delete_at_cursor(content, cursor_pos)

        case "sw":
            if 0 <= cursor_pos < len(content) and content[cursor_pos].isalnum():
                content, cursor_pos = swap_next_word(content, cursor_pos)
            else:
                pass

        case "sb":
            if 0 <= cursor_pos < len(content) and content[cursor_pos].isalnum():
                content, cursor_pos = swap_prev_word(content, cursor_pos)
            else:
                pass

        case "v":
            pass

        case "q":
            break

        case _:
            if prompt[0] not in insert_cmds:
                continue

    cursor_pos = max(0, min(cursor_pos, len(content) - 1)) #prevent position from going out of bounds
    print_content(content, cursor_pos, cursor_active)