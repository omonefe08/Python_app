from django.test import TestCase

# Create your tests here.
# devops/conftest.py
import pytest
import os
import django

# Configure Django settings before tests run
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'devops.settings')
django.setup()