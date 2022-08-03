import os
from shutil import move
import eel
from time import sleep

folder_for_extensions = {
    'video': ('mp4', 'mov', 'avi', 'mkv', 'wmv', 'mpg', 'mpeg', 'm4v', 'h264'),
    'audio': ('mp3', 'wav', 'ogg', 'flac', 'aif', 'mid', 'midi', 'wma', 'm4a'),
    'image': ('jpg', 'png', 'bmp', 'jpeg', 'svg', 'tif', 'tiff'),
    'archive': ('zip', 'rar', '7z', 'z', 'gz', 'pkg', 'deb'),
    'text': ('pdf', 'txt', 'doc', 'docx', 'rtf', 'odt'),
    'spreadsheet': ('xlsx', 'xls', 'xlsm'),
    'presentation': ('pptx', 'ppt'),
    'book': ('fb2', 'epub', 'mobi'),
    'gif': ('gif',),
}


def folder_name(extension: str) -> str:
    for folder, extensions in folder_for_extensions.items():
        if extension in extensions:
            return folder
    return 'Nope'


@eel.expose
def file_sorter(path: str) -> str:
    """
    This program sorts files in the given folder according to their extensions and then puts them to the new folders
made specifically for each type of extension.
    If an extension of file is not listed in the provided dictionary,then program makes a folder named with this
extension and puts the file into it.
    If program finds a file with no extension or a folder it does nothing.
    """

    if not os.path.exists(path):
        return '<h3>Path does not exist</h3>'

    files = os.listdir(path)
    try:
        for file in files:
            filename, extension = os.path.splitext(file)
            extension = extension[1:].lower()

            if not extension:
                continue

            new_folder = folder_name(extension)
            if new_folder == 'Nope':
                if os.path.exists(path + '/' + extension):
                    move(path + '/' + file, path + '/' + extension)
                else:
                    os.makedirs(path + '/' + extension)
                    move(path + '/' + file, path + '/' + extension)
            elif os.path.exists(path + '/' + new_folder):
                move(path + '/' + file, path + '/' + new_folder)
            else:
                os.makedirs(path + '/' + new_folder)
                move(path + '/' + file, path + '/' + new_folder)
        return '<h3>Sorting is done!</h3>'
    except Exception as e:
        return f'<h3>Error occurred:<br>{e}</h3>'


if __name__ == '__main__':
    eel.init('web')

    eel.start('main.html', size=(500, 400))

