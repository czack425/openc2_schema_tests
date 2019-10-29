"""
Load all test cases
"""
import glob
import os
import unittest


file_dir = os.path.dirname(os.path.realpath(__file__))


def create_test_suite(pattern: str = "*_tests.py"):
    pattern = pattern if pattern.endswith(".py") else f"{pattern}.py"
    test_files = glob.glob(os.path.join(file_dir, pattern))
    module_strings = [f"use_cases.{f.replace(file_dir, '')[1:-3]}" for f in test_files]
    suites = unittest.defaultTestLoader.loadTestsFromNames(module_strings)

    return unittest.TestSuite(suites)
