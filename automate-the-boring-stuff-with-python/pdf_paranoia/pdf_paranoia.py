# pdf_paranoia.py

from pathlib import Path

from PyPDF2 import PdfFileReader, PdfFileWriter


def is_encrypted(filename: str) -> None:
    with open(filename, "rb") as file:
        pdf_reader = PdfFileReader(file)
        return pdf_reader.isEncrypted


def encrypt_pdf(filename: str, password: str) -> str | None:
    pdf_reader = PdfFileReader(filename, "rb")
    pdf_writer = PdfFileWriter()

    if not is_encrypted(filename):
        for page_number in range(pdf_reader.numPages):
            pdf_writer.addPage(pdf_reader.getPage(page_number))
    if is_encrypted(filename):
        return f"{filename} is already encrypted."

    # encrypt the file with the provided password
    pdf_writer.encrypt(password)

    # open a new file with a new name
    encrypted_name = f"{filename.split('.')[0]}_encrypted.pdf"
    result_pdf = open(encrypted_name, "wb")

    # write and close the new file
    pdf_writer.write(result_pdf)
    result_pdf.close()

    # open encrypted file
    new_pdf_reader = PdfFileReader(
        str(Path(filename).parents[0] / encrypted_name), "rb"
    )
    # try to uncrypt and delete the file
    try:
        new_pdf_reader.decrypt(password)
        new_pdf_reader.getPage(0)
        Path(filename).unlink()
        print(f"{filename} deleted.")
    except:
        print(f"{filename} not found.")


def decrypt_pdf(filename: str, password: str, name_count: int) -> str | None:
    if is_encrypted(filename):
        pdf_reader = PdfFileReader(filename, "rb")
        pdf_writer = PdfFileWriter()

        try:
            pdf_reader.decrypt(password)
            pdf_reader.getPage(0)

            for page_number in range(pdf_reader.numPages):
                pdf_writer.addPage(pdf_reader.getPage(page_number))

            # get path from current folder and declare decrypted name
            path = Path(filename).parents[0] / f"pdf_{name_count}.pdf"

            # open, write and close file
            result_pdf = open(path, "wb")
            pdf_writer.write(result_pdf)
            result_pdf.close()
        except:
            print(f"Wrong password for {filename}.")


if __name__ == "__main__":
    password = "swordfish"
    path = Path(__file__).parent.resolve()

    # encrypt and delete original pdf
    for pdf in path.rglob(f"*.pdf"):
        encrypt_pdf(str(pdf), password)

    # decrypt pdf
    name_count = 1
    for pdf in path.rglob(f"*.pdf"):
        decrypt_pdf(str(pdf), password, name_count)
        name_count += 1
