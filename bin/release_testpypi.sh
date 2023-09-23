#!/bin/bash

set -e

echo "releasing kdistiller"

python -m build
twine check dist/*

cp /app/bin/.pypirc $HOME/.pypirc

twine upload -r testpypi dist/*
