import requests
import PyPDF2
from io import BytesIO


class DataSource:
    """
    Base class for data sources that downloads data and converts it to text
    """

    def __init__(self, source):
        self.source = source

    def fetch_data(self):
        raise NotImplementedError("Subclasses should implement this method")


class PDFDataSource(DataSource):
    """
    Downloads data from a PDF file URL and converts it to text
    """

    def __init__(self, source):
        super().__init__(source)

    def fetch_data(self):
        response = requests.get(self.source)
        with BytesIO(response.content) as data:
            reader = PyPDF2.PdfReader(data)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
        return text


# # example usage
# pdf_data_source = PDFDataSource(
#     "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf")
# text = pdf_data_source.fetch_data()
# print(text)
