# zip, tar, gz
# rar
# .rar
import shutil
from pathlib import Path

# впаковуємо папку в якій ми працюємо
archive_name = shutil.make_archive('backup', 'zip')

# archive_name = shutil.make_archive('backup', 'zip', Path('C:/Users/pc/Desktop/заняття/group_02-02/lesson17'))
shutil.unpack_archive(archive_name, 'new_folder')


for shortcut, description in shutil.get_archive_formats():
    print('{:<10} | {:<10}'.format(shortcut, description))

