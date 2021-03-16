echo "Test"
pytest -v ./test/*.py
pytest -v -n 5 ./test/*.py
pytest -v --driver=firefox ./test/*.py
pytest -v -n 5 --driver=firefox ./test/*.py
echo "End Test"

#pytest -v -n 5 --headless=True --count=3 --html=report.html ./test/*.py
