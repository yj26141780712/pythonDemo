from utils import word_to_pdf
import pathlib


def main():
    main_path = pathlib.Path.cwd()
    file_path = pathlib.PurePath.joinpath(main_path.parent, 'files')
    doc_file = pathlib.PurePath.joinpath(file_path, '模板.docx')
    pdf_file = pathlib.PurePath.joinpath(file_path, '模板.pdf')
    print(doc_file)
    print(pdf_file)
    word_to_pdf.osToPdf(doc_file, file_path)


if __name__ == '__main__':
    main()
