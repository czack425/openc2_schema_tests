# Updated SLPF-Acme UseCases
- Changes made for Language Spec compliance

## Bad Commands
| File | Change | Reason | Note |
|------|--------|--------|------|
| query_features_ext_args_capX.json | "X_mycompany" -> "X-mycompany" | extentions are '-' not '_' |
| query_features_ext_args_dots.json | "x_mycompany.example.com" -> "x-mycompany.example.com" | extentions are '-' not '_' |
| query_features_ext_args_nox-.json | ... | ... |
| query_features_ext_args_specialchar.json | "x_mycompany/foo;bar" -> "x-mycompany/foo;bar" | extentions are '-' not '_' |
| query_multiple_target_extensions.json | "x_acme:features" -> "x-acme:features"<br />"x_mycompany:features" -> "x-mycompany:features" | extentions are '-' not '_' |
| start_container_ext_specialchar1.json | "x_acm&e:container" -> "x-acm&e:container" | extentions are '-' not '_' |
| start_container_ext_specialchar2.json | "x_acme:conta$iner" -> "x-acme:conta$iner" | extentions are '-' not '_' |
| start_container_ext_underscore_first1.json | "x__acme:container" -> "x-_acme:container" | extentions are '-' not '_' |
| start_container_ext_underscore_first2.json| "x_acme:_container" -> "x-acme:_container" | extentions are '-' not '_' |

## Good Commands
| File | Change | Reason | Note |
|------|--------|--------|------|
| deny_uri_actuator_multiple.json | "x_acme" -> "x-acme" | extentions are '-' not '_' |
| ls_example_query_properties_battery.json | "x_esm" -> "x-esm" | extentions are '-' not '_' |
| query_features_all_badprofile.json | version:<br/>"1.0-draft-2019-02" -> "1.0" | version string not compliant to the language spec description | Is this supposed to be in responses-good? |
| query_features_ext_args.json | "x_mycompany" -> "x-mycompany" | extentions are '-' not '_' |
| query_features_ext_args_all.json | "x\_0123456789\_ABCDEFG_abcdefg\__\_" -> "x-0123456789\_ABCDEFG_abcdefg\__\_" | extentions are '-' not '_' |
| query_features_ext_args_underscore.json | "x_mycompany_with_underscore" -> "x-mycompany_with_underscore" | extentions are '-' not '_' |
| query_features_ext_target.json | "x_acme:features" -> "x-acme:features" | extentions are '-' not '_' |
| query_features_extension_args_number.json | "x_395" -> "x-395" | extentions are '-' not '_' |
| results_unknown_profile.json | None | | Is this supposed to be in responses-good? |
| set_properties_firewall_status.json | "x_acme" -> "x-acme" | extentions are '-' not '_' |
| start_container_ext_target.json | "x_acme:containers" -> "x-acme:containers" | extentions are '-' not '_' |
| start_container_ext_target_ext_actuator.json | "x_acme:containers" -> "x-acme:containers"<br />"x_mycompany" -> "x-mycompany" | extentions are '-' not '_' |
| start_container_ext_target_ext_actuator_ext_args.json | "x_acme:containers" -> "x-acme:containers"<br />"x_mycompany" -> "x-mycompany"<br />"x_example" -> "x-example" | extentions are '-' not '_' |
| start_container_ext_target_ext_actuator_mult_ext_args.json | "x_acme:containers" -> "x-acme:containers"<br />"x_mycompany" -> "x-mycompany"<br />"x_example" -> "x-example" | extentions are '-' not '_' |
| stop_container_ext_target.json | "x_acme:containers" -> "x-acme:containers" | extentions are '-' not '_' |

## Bad Responses
| File | Change | Reason | Note |
|------|--------|--------|------|
| results_ext_empty.json | "x_acme" -> "x-acme" | extentions are '-' not '_' |

## Good Responses
| File | Change | Reason | Note |
|------|--------|--------|------|
| ls_example_query_properties_battery.json | "x_esm" -> "x-esm" | extentions are '-' not '_' |
| results_ext_multiple.json | "x_mycompany" -> "x-mycompany"<br />"x_acme" -> "x-acme" | extentions are '-' not '_' | 201 is not a valid OpenC2 Status-Code, move to responses-bad |
| results_ext_single.json | "x_mycompany" -> "x-mycompany" | extentions are '-' not '_' | 201 is not a valid OpenC2 Status-Code, move to responses-bad |
