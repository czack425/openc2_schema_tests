# Updated Use Cases

  - Changes made for Language Spec compliance

## SLPF-Acme Use Cases

### Bad Commands

<table>
<thead>
<tr class="header">
<th>File</th>
<th>Changes</th>
<th>Reason</th>
<th>Source</th>
<th>Note</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>create_poetry.json</td>
<td></td>
<td></td>
<td><a href="https://github.com/oasis-open/openc2-custom-aps">Oasis</a></td>
<td></td>
</tr>
<tr class="even">
<td>deny_uri_actuator_multiple.json</td>
<td>"x_acme" -&gt; "x-acme"</td>
<td>extensions are '-' not '_'</td>
<td><a href="https://github.com/oasis-open/openc2-custom-aps">Oasis</a></td>
<td></td>
</tr>
<tr class="odd">
<td>long_name_80.json</td>
<td></td>
<td></td>
<td><a href="https://github.com/oasis-open/openc2-custom-aps">Oasis</a></td>
<td></td>
</tr>
<tr class="even">
<td>long_name_244.json</td>
<td></td>
<td></td>
<td><a href="https://github.com/oasis-open/openc2-custom-aps">Oasis</a></td>
<td></td>
</tr>
<tr class="odd">
<td>long_name_x80.json</td>
<td></td>
<td></td>
<td><a href="https://github.com/oasis-open/openc2-custom-aps">Oasis</a></td>
<td></td>
</tr>
<tr class="even">
<td>long_name_x244.json</td>
<td></td>
<td></td>
<td><a href="https://github.com/oasis-open/openc2-custom-aps">Oasis</a></td>
<td></td>
</tr>
<tr class="odd">
<td>query_features_ext_args_capX.json</td>
<td>"X_mycompany" -&gt; "X-mycompany"</td>
<td>extensions are '-' not '_'</td>
<td><a href="https://github.com/oasis-open/openc2-custom-aps">Oasis</a></td>
<td></td>
</tr>
<tr class="even">
<td>query_features_ext_args_dots.json</td>
<td>"x_mycompany.example.com" -&gt; "x-mycompany.example.com"</td>
<td>extensions are '-' not '_'</td>
<td><a href="https://github.com/oasis-open/openc2-custom-aps">Oasis</a></td>
<td></td>
</tr>
<tr class="odd">
<td>query_features_ext_args_nox-.json</td>
<td></td>
<td></td>
<td><a href="https://github.com/oasis-open/openc2-custom-aps">Oasis</a></td>
<td></td>
</tr>
<tr class="even">
<td>query_features_ext_args_specialchar.json</td>
<td>"x_mycompany/foo;bar" -&gt; "x-mycompany:foo;bar"</td>
<td><p>extensions are '-' not '_'</p>
<p>Language compliance</p></td>
<td><a href="https://github.com/oasis-open/openc2-custom-aps">Oasis</a></td>
<td></td>
</tr>
<tr class="odd">
<td>query_multiple_target_extensions.json</td>
<td><p>"x_acme:features" -&gt; "x-acme:features"</p>
<p>"x_mycompany:features" -&gt; "x-mycompany:features"</p></td>
<td>extensions are '-' not '_'</td>
<td><a href="https://github.com/oasis-open/openc2-custom-aps">Oasis</a></td>
<td></td>
</tr>
<tr class="even">
<td>start_container_ext_specialchar1.json</td>
<td>"x_acm&amp;e:container" -&gt; "x-acm&amp;e:container"</td>
<td>extensions are '-' not '_'</td>
<td><a href="https://github.com/oasis-open/openc2-custom-aps">Oasis</a></td>
<td></td>
</tr>
<tr class="odd">
<td>start_container_ext_specialchar2.json</td>
<td>"x_acme:conta$iner" -&gt; "x-acme:conta$iner"</td>
<td>extensions are '-' not '_'</td>
<td><a href="https://github.com/oasis-open/openc2-custom-aps">Oasis</a></td>
<td></td>
</tr>
<tr class="even">
<td>start_container_ext_underscore_first1.json</td>
<td>"x__acme:container" -&gt; "x-_acme:container"</td>
<td>extensions are '-' not '_'</td>
<td><a href="https://github.com/oasis-open/openc2-custom-aps">Oasis</a></td>
<td></td>
</tr>
<tr class="odd">
<td>start_container_ext_underscore_first2.json</td>
<td>"x_acme:_container" -&gt; "x-acme:_container"</td>
<td>extensions are '-' not '_'</td>
<td><a href="https://github.com/oasis-open/openc2-custom-aps">Oasis</a></td>
<td></td>
</tr>
</tbody>
</table>

### Good Commands

<table>
<thead>
<tr class="header">
<th>File</th>
<th>Changes</th>
<th>Reason</th>
<th>Source</th>
<th>Note</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ls_example_deny_ipv4connection.json</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>ls_example_query_properties_battery.json</td>
<td></td>
<td></td>
<td><a href="https://github.com/oasis-open/openc2-custom-aps">Oasis</a></td>
<td></td>
</tr>
<tr class="odd">
<td>query_features_ext_args.json</td>
<td>"x_mycompany" -&gt; "x-mycompany"</td>
<td>extensions are '-' not '_'</td>
<td><a href="https://github.com/oasis-open/openc2-custom-aps">Oasis</a></td>
<td></td>
</tr>
<tr class="even">
<td>query_features_ext_args_all.json</td>
<td>"x\_0123456789\_ABCDEFG_abcdefg\__\_" -&gt; "x-0123456789\_ABCDEFG_abcdefg\__\_"</td>
<td>extensions are '-' not '_'</td>
<td><a href="https://github.com/oasis-open/openc2-custom-aps">Oasis</a></td>
<td></td>
</tr>
<tr class="odd">
<td>query_features_ext_args_underscore.json</td>
<td>"x_mycompany_with_underscore" -&gt; "x-mycompany_with_underscore"</td>
<td>extensions are '-' not '_'</td>
<td><a href="https://github.com/oasis-open/openc2-custom-aps">Oasis</a></td>
<td></td>
</tr>
<tr class="even">
<td>query_features_ext_target.json</td>
<td>"x_acme:features" -&gt; "x-acme:features"</td>
<td>extensions are '-' not '_'</td>
<td><a href="https://github.com/oasis-open/openc2-custom-aps">Oasis</a></td>
<td></td>
</tr>
<tr class="odd">
<td>query_features_extension_args_number.json</td>
<td>"x_395" -&gt; "x-395"</td>
<td>extensions are '-' not '_'</td>
<td><a href="https://github.com/oasis-open/openc2-custom-aps">Oasis</a></td>
<td></td>
</tr>
<tr class="even">
<td>slpf_example_allow_ipv6connection.json</td>
<td></td>
<td></td>
<td><a href="https://github.com/oasis-open/openc2-custom-aps">Oasis</a></td>
<td></td>
</tr>
<tr class="odd">
<td>slpf_example_delete_rulenumber.json</td>
<td></td>
<td></td>
<td><a href="https://github.com/oasis-open/openc2-custom-aps">Oasis</a></td>
<td></td>
</tr>
<tr class="even">
<td>slpf_example_deny_ipv4connection.json</td>
<td></td>
<td></td>
<td><a href="https://github.com/oasis-open/openc2-custom-aps">Oasis</a></td>
<td></td>
</tr>
<tr class="odd">
<td>slpf_example_deny_ipv6connection.json</td>
<td></td>
<td></td>
<td><a href="https://github.com/oasis-open/openc2-custom-aps">Oasis</a></td>
<td></td>
</tr>
<tr class="even">
<td>slpf_example_deny_ipv6net.json</td>
<td></td>
<td></td>
<td><a href="https://github.com/oasis-open/openc2-custom-aps">Oasis</a></td>
<td></td>
</tr>
<tr class="odd">
<td>slpf_example_update_file.json</td>
<td></td>
<td></td>
<td><a href="https://github.com/oasis-open/openc2-custom-aps">Oasis</a></td>
<td></td>
</tr>
<tr class="even">
<td>set_properties_firewall_status.json</td>
<td>"x_acme" -&gt; "x-acme"</td>
<td>extensions are '-' not '_'</td>
<td><a href="https://github.com/oasis-open/openc2-custom-aps">Oasis</a></td>
<td></td>
</tr>
<tr class="odd">
<td>start_container_ext_target.json</td>
<td>"x_acme:containers" -&gt; "x-acme:containers"</td>
<td>extensions are '-' not '_'</td>
<td><a href="https://github.com/oasis-open/openc2-custom-aps">Oasis</a></td>
<td></td>
</tr>
<tr class="even">
<td>start_container_ext_target_ext_actuator.json</td>
<td><p>"x_acme:containers" -&gt; "x-acme:containers"</p>
<p>"x_mycompany" -&gt; "x-mycompany"</p></td>
<td>extensions are '-' not '_'</td>
<td><a href="https://github.com/oasis-open/openc2-custom-aps">Oasis</a></td>
<td></td>
</tr>
<tr class="odd">
<td>start_container_ext_target_ext_actuator_ext_args.json</td>
<td><p>"x_acme:containers" -&gt; "x-acme:containers"</p>
<p>“x_mycompany" -&gt; "x-mycompany"</p>
<p>"x_example" -&gt; "x-example"</p></td>
<td>extensions are '-' not '_'</td>
<td><a href="https://github.com/oasis-open/openc2-custom-aps">Oasis</a></td>
<td></td>
</tr>
<tr class="even">
<td>start_container_ext_target_ext_actuator_mult_ext_args.json</td>
<td><p>"x_acme:containers" -&gt; "x-acme:containers"</p>
<p>"x_mycompany" -&gt; "x-mycompany"</p>
<p>“x_example" -&gt; "x-example"</p></td>
<td>extensions are '-' not '_'</td>
<td><a href="https://github.com/oasis-open/openc2-custom-aps">Oasis</a></td>
<td></td>
</tr>
<tr class="odd">
<td>stop_container_ext_target.json</td>
<td>"x_acme:containers" -&gt; "x-acme:containers"</td>
<td>extensions are '-' not '_'</td>
<td><a href="https://github.com/oasis-open/openc2-custom-aps">Oasis</a></td>
<td></td>
</tr>
</tbody>
</table>

### Bad Responses

<table>
<thead>
<tr class="header">
<th>File</th>
<th>Changes</th>
<th>Reason</th>
<th>Source</th>
<th>Note</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>results_ext_empty.json</td>
<td>"x_acme" -&gt; "x-acme"</td>
<td>extensions are '-' not '_'</td>
<td><a href="https://github.com/oasis-open/openc2-custom-aps">Oasis</a></td>
<td></td>
</tr>
<tr class="even">
<td>results_ext_multiple.json</td>
<td><p>"x_mycompany" -&gt; "x-mycompany</p>
<p>“x_acme" -&gt; "x-acme"</p></td>
<td>extensions are '-' not '_'</td>
<td><a href="https://github.com/oasis-open/openc2-custom-aps">Oasis</a></td>
<td>Moved from good-responses</td>
</tr>
<tr class="odd">
<td>results_ext_single.json</td>
<td>"x_mycompany" -&gt; "x-mycompany"</td>
<td>extensions are '-' not '_'</td>
<td><a href="https://github.com/oasis-open/openc2-custom-aps">Oasis</a></td>
<td>Moved from good-responses</td>
</tr>
<tr class="even">
<td>results_poetry.json</td>
<td></td>
<td></td>
<td><a href="https://github.com/oasis-open/openc2-custom-aps">Oasis</a></td>
<td></td>
</tr>
<tr class="odd">
<td>results_unknown_profile.json</td>
<td></td>
<td></td>
<td><a href="https://github.com/oasis-open/openc2-custom-aps">Oasis</a></td>
<td>Moved from commands-good</td>
</tr>
<tr class="even">
<td>slpf_query_pairs_bad_action.json</td>
<td></td>
<td></td>
<td><a href="https://github.com/oasis-open/openc2-custom-aps">Oasis</a></td>
<td></td>
</tr>
<tr class="odd">
<td>slpf_query_pairs_bad_pair.json</td>
<td></td>
<td></td>
<td><a href="https://github.com/oasis-open/openc2-custom-aps">Oasis</a></td>
<td></td>
</tr>
<tr class="even">
<td>slpf_query_pairs_bad_target.json</td>
<td></td>
<td></td>
<td><a href="https://github.com/oasis-open/openc2-custom-aps">Oasis</a></td>
<td></td>
</tr>
</tbody>
</table>

### Good Responses

| File                                                | Changes              | Reason                      | Source                                                   | Note                                        |
| --------------------------------------------------- | -------------------- | --------------------------- | -------------------------------------------------------- | ------------------------------------------- |
| ls\_example\_query\_properties\_battery.json        | "x\_esm" -\> "x-esm" | extensions are '-' not '\_' | [Oasis](https://github.com/oasis-open/openc2-custom-aps) |                                             |
| query\_features\_all\_badprofile.json               |                      |                             | [Oasis](https://github.com/oasis-open/openc2-custom-aps) |                                             |
| results\_ext\_empty.json                            |                      |                             | [Oasis](https://github.com/oasis-open/openc2-custom-aps) |                                             |
| results\_ext\_multiple.json                         |                      |                             | [Oasis](https://github.com/oasis-open/openc2-custom-aps) | Status 201 is not valid under V1.0 language |
| results\_ext\_single.json                           |                      |                             | [Oasis](https://github.com/oasis-open/openc2-custom-aps) | Status 201 is not valid under V1.0 language |
| results\_slpf\_empty.json                           |                      |                             | [Oasis](https://github.com/oasis-open/openc2-custom-aps) |                                             |
| slpf\_example\_query\_features\_pairs\_example.json |                      |                             | [Oasis](https://github.com/oasis-open/openc2-custom-aps) |                                             |
| slpf\_example\_rule\_number.json                    |                      |                             | [Oasis](https://github.com/oasis-open/openc2-custom-aps) |                                             |
