# Typing

Static type checking is done using mypy.
All files are typed apart from files that are:

- Django models file (mypy doesn't like models.CharField etc).
- module/\_\_pycache\_\_/*.
- module/migrations/*.
- Test files, unless it absolutely aids the reader in understanding what is being tested.
