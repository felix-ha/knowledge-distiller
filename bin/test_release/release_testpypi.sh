echo "releasing kdistiller"

python -m build
twine check dist/*

mv /app/bin/test_release/.pypirc $HOME/.pypirc

twine upload -r testpypi dist/*
