# test_cloudforge.py
"""
Tests for CloudForge module.
"""

import unittest
from cloudforge import CloudForge

class TestCloudForge(unittest.TestCase):
    """Test cases for CloudForge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CloudForge()
        self.assertIsInstance(instance, CloudForge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CloudForge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
