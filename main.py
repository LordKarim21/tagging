import os
import eyed3
import transliterate

FIND_DIRECTORY = r'C:\Users\User\PycharmProjects\tagging\Test'


def walk(directory):
    for root, dirs, files in os.walk(directory):
        for name in files:
            set_tegs(os.path.join(root, name))


def set_tegs(file):
    name = os.path.basename(file).split('.')[0]
    audio_file = eyed3.load(file)
    if not audio_file.tag:
        audio_file.initTag()
    if not audio_file.tag.album:
        audio_file.tag.album = 'Other'
    audio_file.tag.title = transliterate.translit(name, language_code='ru', reversed=True)


if __name__ == '__main__':
    walk(FIND_DIRECTORY)
