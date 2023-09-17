echo "releasing kdistiller"

python -m build
twine check dist/*

mv /app/bin/release/.pypirc $HOME/.pypirc

twine upload -r pypi dist/*
