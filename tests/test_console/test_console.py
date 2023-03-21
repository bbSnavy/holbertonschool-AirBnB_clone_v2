#!/usr/bin/python3
""" """
import unittest
import subprocess


class test_console(unittest.TestCase):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = 'Console'
    
    def setUp(self):
        """ """
        pass

    def tearDown(self):
        pass

    def test_help(self):
        p = subprocess.Popen(
            ['python3', 'console.py'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)

        out, err = p.communicate(b'help\n')
        self.assertEqual(err, b'')
        self.assertIsNotNone(out)

        out = out.decode()
        self.assertTrue(out.startswith('(hbnb)'))
        self.assertIn('Documented commands (type help <topic>):', out)
        