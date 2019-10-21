
# Schema UnitTests

## Install
- Run `pip install -r requirements.txt` to install the required dependencies
- Add additional schemas to the `schemas` folder
	- Add the new schema to the schema dictionary in `test_schemas.py`
- Edit the `test_schemas.py` script accordingly
	- Add/Remove schemas to test
	- Add/Remove additional Profiles for testing

## Adding Profile Tests
- All files and paths are assumed to be in the `use_cases` folder

1. Copy and rename the `PROFILE_tests_Template.py` for the desired profile, removing `_Template` from the file name
	- Ex) SLPF, the file is renamed as `SLPF_tests.py`

2. Edit the `profile` variable for the desired profile name of the new profile tests file
	- Ex) SLPF, `profile = "SLPF"`

3. Edit the class name for the desired profile name
	- Ex) SLPF, `class PROFILE_UseCases(SetupTests):` changes to `class SLPF_UseCases(SetupTests):`
	- If the profile is not approved or is an approved profile with non-approved additions:
		- Edit the `unittest.skipIf` decorator as shown
		- This allows the test to __ONLY__ run when the profile (SLPF) and extensions are specified for testing
		- Ex) SLPF with non-approved profile Acme, `@unittest.skipIf(check_profiles_skip("SLPF", "Extension"), f"{profile} Profile tests not specified")`

4. Add Dynamic Cases to the `dynamic_cases` folder in the appropriate version  and profile folders
    - All names should be lowercase
	- Ex) SLPF v1.0, slpf dynamic cases should be added to `dynamic_cases/v1.0/slpf`
	
	- The profile case folder should have four folders with the corresponding test files in each
		- `dynamic_cases/VERSION/PROFILE/commands_good` -> Good Commands, should not raise an error
		- `dynamic_cases/VERSION/PROFILE/commands_bad` -> Bad Commands, should raise an error
		- `dynamic_cases/VERSION/PROFILE/responses_good` -> Good Responses, should not raise an error
		- `dynamic_cases/VERSION/PROFILE/responses_bad` -> Bad Responses, should raise an error
	 

### Adding Static Tests (Optional)
1. Add a function prefixed with `test_` with the desired command/response message
	
	- Ex) Test should pass without errors
	
	```python
	...
    def test_basic_query(self):
        """
        Basic query features, all schemas should support this command/response pair
        """
        cmd = {
            "action": "query",
            "target": {
                "features": []
            }
        }
        rsp = {
            "status": 200
        }

        self.validate_as(cmd, self.cmd_exp)
        self.validate_as(rsp, self.rsp_exp)
    ...
	```
	
	- Ex) Test should pass with errors
	
	```python
	...
    def test_basic_query(self):
        """
        Basic query features, all schemas should support this command/response pair
        """
        cmd = {
            "action": "query",
            "target": {
                "features": [
                    "OpenC2"
                ]
            }
        }
        rsp = {
            "status": 600
        }

		 with self.assertRaises(ValidationError):
            self.validate_as(cmd, self.cmd_exp)
        
        with self.assertRaises(ValidationError):
	        self.validate_as(rsp, self.rsp_exp)
    ...
	```


## Notes:
- Use cases
    - General - [Oasis](https://github.com/oasis-tcs/openc2-usecases)
        - Current version of tests in latest version folder in `use_cases/dynamic_tests` 
	    - Some cases updated for adherence to schema changes
- The code within this repository is not intended to be production ready 