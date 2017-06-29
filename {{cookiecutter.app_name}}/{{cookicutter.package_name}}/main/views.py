# -*- coding: utf-8 -*-
"""Views for the main package of {cookiecutter.app_name}

.. module:: views
    :platform: Unix
    :synopsis: Views for the main package.
.. moduleauthor:: {cookiecutter.author_name} <{cookiecutter.email}>
"""
from flask import render_template
from . import main

@main.route('/')
def index():
    return render_template('index.html')


