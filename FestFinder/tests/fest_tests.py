import os
import festfinder
import unittest
import tempfile

class festfinderTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, festfinder.app.conffig['DATABASE'] = tempfile.mkstemp()
        festfinder.app.testing = True
        self.app = festfinder.app.test_client()
        with festfinder.app.app_context():
            festfinder.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(festfinder.app.config['DATABASE'])

if __name__ == '__main__':
    unittest.main()
class FestfinderTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, festfinder.app.config['DATABASE'] = tempfile.mkstemp()
        festfinder.app.testing = True
        self.app = festfinder.app.test_client()
        with festfinder.app.test_client():
            festfinder.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(festfinder.app.config['DATABASE'])

    def test_empty_db(self):
        rv= self.app.get('/')
        assert b'No entries' in rv.data
