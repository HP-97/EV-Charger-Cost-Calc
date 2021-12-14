# API Notes

## Setting up Dev environment using Poetry

Run command to create virtualenv within the project path and vscode will be able to find it

```
poetry config virtualenvs.in-project true
```

If you already have created your project, you need to re-create the virtualenv to make it appear in the correct place:
```
poetry env list  # shows the name of the current environment
poetry env remove <current environment>
poetry install  # will create a new environment using your updated configuration
```