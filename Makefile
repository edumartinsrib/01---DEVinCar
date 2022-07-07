test:
    pytest --cov-report term-missing --cov-report html --cov-branch \
           --cov projeto_x/

lint:
    @echo
    isort --diff -c .
    @echo
    blue --check --diff --color .
    @echo
    flake8 .
    @echo
    mypy .
    @echo
    bandit -r projeto_x/
    @echo
    pip-audit

format:
    isort .
    blue .
    pyupgrade --py310-plus **/*.py