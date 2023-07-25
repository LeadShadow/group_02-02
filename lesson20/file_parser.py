from pathlib import Path

JPEG_IMAGES = []
JPG_IMAGES = []
SVG_IMAGES = []
PNG_IMAGES = []

MP3_AUDIO = []
OGG_AUDIO = []
WAV_AUDIO = []
AMR_AUDIO = []

AVI_VIDEO = []
MP4_VIDEO = []
MKV_VIDEO = []
MOV_VIDEO = []

DOC_DOCUMENTS = []
DOCX_DOCUMENTS = []
PPTX_DOCUMENTS = []
XLSX_DOCUMENTS = []
TXT_DOCUMENTS = []
PDF_DOCUMENTS = []
CSV_DOCUMENTS = []

OTHER = []
ARCHIVES = []
FOLDERS = []
EXTENSIONS = set()
UNKNOWN = set()


REGISTER_EXTENSIONS = {
    'JPEG': JPEG_IMAGES,
    'JPG': JPG_IMAGES,
    'SVG': SVG_IMAGES,
    'PNG': PNG_IMAGES,
    'MP3': MP3_AUDIO,
    'OGG': OGG_AUDIO,
    'WAV': WAV_AUDIO,
    'AMR': AMR_AUDIO,
    'GZ': ARCHIVES,
    'TAR': ARCHIVES,
    'ZIP': ARCHIVES,
    'MP4': MP4_VIDEO,
    'AVI': AVI_VIDEO,
    'MKV': MKV_VIDEO,
    'MOV': MOV_VIDEO,
    'DOC': DOC_DOCUMENTS,
    'DOCX': DOCX_DOCUMENTS,
    'PPTX': PPTX_DOCUMENTS,
    'TXT': TXT_DOCUMENTS,
    'PDF': PDF_DOCUMENTS,
    'XLSX': XLSX_DOCUMENTS,
    'CSV': CSV_DOCUMENTS
}

# test.txt -> 'TXT'
def get_extensions(filename: str) -> str:
    return Path(filename).suffix[1:].upper()  # .jpg -> [1:] -> jpg


def scan(folder: Path) -> None:  # /user/DESKTOP/ХЛАМ /user/DESKTOP/ХЛАМ/test
    for item in folder.iterdir():
        # якщо це папка,то додаємо в список FOLDERS і переходимо до наступного елементу
        if item.is_dir():
            # перевіряємо щоб ця папка не була тою в яку ми складаємо файли
            if item.name not in ('archives', 'video', 'audio', 'documents', 'images', 'OTHER'):
                FOLDERS.append(item)
                # скануємо вложенну папку(рекурсія)
                scan(item)
            # переходимо до наступного елементу в нашій папці
            continue

        # Пішла робота з файлом
        ext = get_extensions(item.name)  # /user/DESKTOP/ХЛАМ/test.txt -> test.txt -> 'TXT'
        fullname = folder / item.name # взяти повний шлях до файлу
        if not ext:  # якщо у файла немає розширення
            OTHER.append(fullname)
        else:
            try:
                # взяти список куди покласти повний шлях до файлу
                container = REGISTER_EXTENSIONS[ext]
                EXTENSIONS.add(ext)
                container.append(fullname)
            except KeyError:
                # якщо ми не зареєстрували розширення в REGISTER_EXTENSIONS
                UNKNOWN.add(ext)
                OTHER.append(fullname)


if __name__ == "__main__":
    folders_for_scan = input('Input directory: ')
    print(f'Start in folder {folders_for_scan}')

    scan(Path(folders_for_scan))
    print(f'Images PNG: {PNG_IMAGES}')
    print(f'Images JPG: {JPG_IMAGES}')
    print(f'Images JPEG: {JPEG_IMAGES}')
    print(f'Images SVG: {SVG_IMAGES}')

    print(f'Documents TXT: {TXT_DOCUMENTS}')
    print(f'Documents DOC: {DOC_DOCUMENTS}')
    print(f'Documents DOCX: {DOCX_DOCUMENTS}')
    print(f'Documents XLSX: {XLSX_DOCUMENTS}')


    dict1 = {
        None: 'dict'
    }

    set1 = set('hello')
    print(set1)