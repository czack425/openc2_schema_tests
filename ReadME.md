
# Schema UnitTests

## Install
- Run `pip install -r requirements.txt`
- Edit the `test_schemas.py` script accordingly
	- Add _your_ GitHubAPI Token for additional schema tests from [Brian Berliner](https://github.com/bberliner/openc2-json-schema)
	- Add additional schemas in the `schemas` dictionary
	- Additional message validation
		- Test cases from Oasis (collection of use cases from OpenC2 implementors/partners/etc)
		- Dynamic message validation from json files
			- Files are placed in `use_cases/file_tests/...` as to the message contents
			- Ex) a good command is placed in `use_cases/file_tests/commands/good/command.json`


## Notes:
- Use cases
    - General - [Oasis](https://github.com/oasis-tcs/openc2-usecases)
	    - Some cases updated for adherence to schema changes
    - Additional, not included = [Brian Berliner](https://github.com/bberliner/openc2-json-schema)