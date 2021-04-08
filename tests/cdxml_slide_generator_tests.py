import unittest
from pycdxml.cdxml_slide_generator import TextProperty, CDXMLSlideGenerator
import filecmp
from pathlib import Path
import logging



logger = logging.getLogger('pycdxml.cdxml_slide_generator')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)


class CdxmlSlideGeneratorTest(unittest.TestCase):

    FILES = ['files/standard_test.cdxml', 'files/magnesium_citrate.cdxml', 'files/reference_style.cdxml']

    def test_basic_slide(self):

        sg = CDXMLSlideGenerator(style="ACS 1996", number_of_properties=2)
        slide = sg.generate_slide(self.test_structures, self.properties)

    def setUp(self):
        self.test_structures = []
        self.properties = []
        for idx, f in enumerate(self.FILES):
            with open(f, 'r') as file:
                cdxml = file.read()
                self.test_structures.append(cdxml)
                props = [TextProperty('ID', idx, color='#3f6eba'), TextProperty('Name', "Molecule " + str(idx), show_name=True)]
                self.properties.append(props)

    def tearDown(self):
        # Delete all files generated by tests
        for p in Path("files").glob("*_out.*"):
            p.unlink()


if __name__ == '__main__':
    unittest.main()