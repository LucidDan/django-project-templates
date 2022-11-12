# django-project-templates
Django project and app templates for various styles and purposes

I build a lot of django apps for prototyping as well as clients and side projects.
These templates are an attempt to give myself a simple method to set up one of those projects, without going to the effort of building a full cookiecutter template.

Using any of these is just a matter of using the Django manage.py/djangoadmin command 'startproject' or 'startapp' with the ['--template' argument](https://docs.djangoproject.com/en/stable/ref/django-admin/#cmdoption-startapp-template)
It is recommended to use '.' as the destination directory, e.g:

```
django-admin startproject myprojectname . --template ~/django-project-templates/full-project
```

## Full Project Template

Directory: 'full-project'

This is the full project template with a 'core' app. This is designed to be used for "real" projects or MVP prototypes that need a bit more architecture to them.

There are a few design decisions particularly worth noting:

* Uses a single package for all 'local' apps to live in
* Puts tests in a separate 'tests' package, so they are easy to exclude from production deployments
* Provides a fly.toml for deploying as a fly.io application
* Provides 'core' and 'users' apps as part of the basic codebase. If auth isn't needed, 'users' can be ditched

While it avoids specifically assuming third party packages are installed, it includes code that can take advantage of
 features from:
- django-allauth
- channels (>=4.0.0)
- daphne (>=4.0.0)

It assumes your test runner is pytest. Why would you use anything else?


## Full Project App Template

This is the template for additional apps added to the full project template.

## Simple Combined Project Template

This is a cut-down template designed to be used for relatively simple projects or pure prototypes that are likely to be chucked out and rewritten.

It mostly sticks to 12-factor principles, but instead of a standard django project with multiple apps, the project and app are folded in to a single "project app".

This project is not designed to have additional apps added to it.

## Single File Project Template

What it sounds like - for extremely simple micro-projects. The entire project is one python module.
