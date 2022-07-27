import click
import os
from shutil import move
from art import text2art

folder_for_extensions = {
    'video': ('mp4', 'mov', 'avi', 'mkv', 'wmv', 'mpg', 'mpeg', 'm4v', 'h264'),
    'audio': ('mp3', 'wav', 'ogg', 'flac', 'aif', 'mid', 'midi', 'wma'),
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


@click.command()
@click.argument('path')
def file_sorter(path: str) -> None:
    """
    This program sorts files in the given folder according to their extensions and then puts them to the new folders
made specifically for each type of extension.
    If an extension of file is not listed in the provided dictionary,then program makes a folder named with this
extension and puts the file into it.
    If program finds a file with no extension or a folder it does nothing.
    """
    click.secho(text2art('File Sorter'))
    if not os.path.exists(path):
        click.secho(f'No such directory: {path}')
        exit(1)
    files = os.listdir(path)

    for file in files:
        filename, extension = os.path.splitext(file)
        extension = extension[1:]

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


if __name__ == '__main__':
    file_sorter()
