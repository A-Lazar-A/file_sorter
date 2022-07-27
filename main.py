import click
import os
import shutil
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

    """
    click.echo(text2art('File Sorter'))
    if not os.path.exists(path):
        click.echo(f'No such directory: {path}')
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
                shutil.move(path + '/' + file, path + '/' + extension)
            else:
                os.makedirs(path + '/' + extension)
                shutil.move(path + '/' + file, path + '/' + extension)
        elif os.path.exists(path + '/' + new_folder):
            shutil.move(path + '/' + file, path + '/' + new_folder)
        else:
            os.makedirs(path + '/' + new_folder)
            shutil.move(path + '/' + file, path + '/' + new_folder)


if __name__ == '__main__':
    file_sorter()
