import unittest
from mailstuff import generateMessage


class EmailTest(unittest.TestCase):
    def setUp(self):
        self.address = ""
        self.content = "This is the content of the message"
        self.file_types = {"foo.txt":"text/plain", "eggs.html":"text/html", "python-logo.png":"image/png"}
        self.attachments = list(self.file_types.keys())
    
    def test_generate_message(self):
        obsMsg = generateMessage(self.address, self.content, )
        self.assertEqual(obsMsg['To'], self.address)
        self.assertEqual(obsMsg.get_payload().rstrip(), self.content)
        
    def test_attach_files(self):
        obsMsg = generateMessage(self.address, self.content, self.attachments)
        obs_file_and_types = {}
        for m in obsMsg.walk():
            if m.is_multipart():
                continue
            obs_file_and_types[m.get_filename()] = m.get_content_type()
        self.assertEqual(obs_file_and_types, self.file_types)

if __name__ == "__main__":
    unittest.main()
    
