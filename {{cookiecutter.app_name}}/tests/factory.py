# -*- coding: utf-8 -*-
"""Tests for the factory module.

Author: {cookiecutter.author_name}
"""
from unittest import TestCase
from .context import factory

class TestFactory(TestCase):
    def setUp(self):
        self.app = factory.create_app()

    def test_app_exists(self):
        self.assertFalse(self.app is None)
