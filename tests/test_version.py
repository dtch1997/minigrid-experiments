import unittest

import minigrid_experiments


class VersionTestCase(unittest.TestCase):
    """ Version tests """

    def test_version(self):
        """ check minigrid_experiments exposes a version attribute """
        self.assertTrue(hasattr(minigrid_experiments, "__version__"))
        self.assertIsInstance(minigrid_experiments.__version__, str)


if __name__ == "__main__":
    unittest.main()
