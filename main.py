def download_file():
    try:
        return open('input.txt', 'r');
    except Exception as e:
        print('File not found, get outta here')
        print(f"{e} but we'll create file anyway")
        """
            На самом деле в создании нового файла и внесение туда дефолтных параметров
            нет необходимости, да и выглядит это немного странно, но можно представить
            что на самом деле это классно что я обрабатываю ошибки. Ну, и рекурсивный
            вызов - красиво. Правда если есть ошибки с правами - плохо будет.
        """
        default_text = open('input.txt', 'w')
        default_text.write('Остап открыл митинг в приподнятом настроении, не подозревая о том, какая угроза  надвигается на пассажиров Антилопы.Он острил, рассказывал смешные дородные приключения и еврейские анекдоты, чем чрезвычайно расположил к себе публику.Конец речи он посвятил разбору давно назравшей автопроблемы.Автомобиль, - воскликнул он трубным голосом, - не роскошь, а что?')
        return download_file()

def z4v4():
    file_text = download_file()
    if file_text:
        output_file = open('output.txt', 'w')
        test = list(map(change_chars, file_text.read()))
        output_file.write(''.join(test))
        output_file.close()

def change_chars(char):
    bookmark = {'!': '?\n', '.': '?\n', '?': '!\n'};
    return bookmark[char] if bookmark.get(char) else char

z4v4()
