import requests

def z5v4():
    downloaded_text = request_service('http://fan.lib.ru/t/tolchinskij_b_a/periandr.shtml')

    if downloaded_text:
        total_chars_count = to_count_chars(downloaded_text)
        return parse_counted_items(total_chars_count)


# Сервис в ковычках (:
def request_service(url):
    try:
        response = requests.get(url)
        text_start = response.text.index("&nbsp;&nbsp; Периандр") + len("&nbsp;&nbsp; ")
        text_end = response.text.index("не завоюет?\n") + len("не завоюет?")
        return response.text[text_start:text_end]
    except:
        print('Тут должна быть обработка ошибок')
        return None


def to_count_chars(downloaded_text):
    whitelist = {'.': 0, ',': 0, '!': 0, '?': 0, '--': 0, '-': 0}
    index = 0
    for fakedChar in downloaded_text:
        if index != len(downloaded_text):
            char = downloaded_text[index]

            if (char in whitelist or downloaded_text[index:index + 2] in whitelist):
                actual_char = downloaded_text[index:index + 2] if downloaded_text[
                                                                  index:index + 2] in whitelist else char
                whitelist[actual_char] += 1

            index += 2 if downloaded_text[index:index + 2] in whitelist else 1
    return whitelist

def parse_counted_items(chars_count):
    parsed_chars_count = {}
    for char in chars_count:
        total_count = chars_count[char]
        parsed_chars_count[total_count] = parsed_chars_count[total_count] if total_count in parsed_chars_count else ''

        parsed_chars_count[total_count] += f"{char} "

    return parsed_chars_count

print(z5v4())