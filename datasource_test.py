import unittest
from datasource import PDFDataSource


class TestPDFDataSource(unittest.TestCase):

    def setUp(self):
        self.pdf_url = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"

    def test_fetch_data(self):
        pdf_data_source = PDFDataSource(self.pdf_url)
        text = pdf_data_source.fetch_data()
        # Verify that the text is non-empty
        self.assertTrue(text)
        # Verify that the text contains at least one word from the document
        self.assertIn("Dumm", text)


if __name__ == '__main__':
    unittest.main()
