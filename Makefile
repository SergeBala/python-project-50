install:
	poetry install

gendiff:
	poetry run gendiff

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	pip install --user dist/*.whl

re:
	echo "\033[1;35m...Building and installing...\033[0m"
	make build
	make package-install

lint:
	poetry run flake8 gendiff

.PHONY : install gendiff build publish package-install lint re