import os


def osToPdf(import_file_name, output_file_path):
    print(import_file_name)
    print(output_file_path)
    print("soffice --headless --invisible --convert-to pdf:writer_pdf_Export %s --outdir %s --env:UserInstallation=file:///C:\Program Files\LibreOffice\program" %
          (import_file_name, output_file_path))
    os.system("soffice --headless --invisible --convert-to pdf:writer_pdf_Export %s --outdir %s" %
              (import_file_name, output_file_path))
