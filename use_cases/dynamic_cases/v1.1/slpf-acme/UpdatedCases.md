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
<td>extensions are '-' not '_'</td>
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
<td>deny_uri_actuator_multiple.json</td>
<td>"x_acme" -&gt; "x-acme"</td>
<td>extensions are '-' not '_'</td>
<td><a href="https://github.com/oasis-open/openc2-custom-aps">Oasis</a></td>
<td></td>
</tr>
<tr class="even">
<td>ls_example_query_properties_battery.json</td>
<td>"x_esm" -&gt; "x-esm"</td>
<td>extensions are '-' not '_'</td>
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
<td>"x_0123456789_ABCDEFG_abcdefg___" -&gt; "x-0123456789_ABCDEFG_abcdefg___"</td>
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
<td>results_unknown_profile.json</td>
<td></td>
<td></td>
<td><a href="https://github.com/oasis-open/openc2-custom-aps">Oasis</a></td>
<td></td>
</tr>
<tr class="odd">
<td>set_properties_firewall_status.json</td>
<td>"x_acme" -&gt; "x-acme"</td>
<td>extensions are '-' not '_'</td>
<td><a href="https://github.com/oasis-open/openc2-custom-aps">Oasis</a></td>
<td></td>
</tr>
<tr class="even">
<td>start_container_ext_target.json</td>
<td>"x_acme:containers" -&gt; "x-acme:containers"</td>
<td>extensions are '-' not '_'</td>
<td><a href="https://github.com/oasis-open/openc2-custom-aps">Oasis</a></td>
<td></td>
</tr>
<tr class="odd">
<td>start_container_ext_target_ext_actuator.json</td>
<td><p>"x_acme:containers" -&gt; "x-acme:containers"</p>
<p>"x_mycompany" -&gt; "x-mycompany"</p></td>
<td>extensions are '-' not '_'</td>
<td><a href="https://github.com/oasis-open/openc2-custom-aps">Oasis</a></td>
<td></td>
</tr>
<tr class="even">
<td>start_container_ext_target_ext_actuator_ext_args.json</td>
<td><p>"x_acme:containers" -&gt; "x-acme:containers"</p>
<p>“x_mycompany" -&gt; "x-mycompany"</p>
<p>"x_example" -&gt; "x-example"</p></td>
<td>extensions are '-' not '_'</td>
<td><a href="https://github.com/oasis-open/openc2-custom-aps">Oasis</a></td>
<td></td>
</tr>
<tr class="odd">
<td>start_container_ext_target_ext_actuator_mult_ext_args.json</td>
<td><p>"x_acme:containers" -&gt; "x-acme:containers"</p>
<p>"x_mycompany" -&gt; "x-mycompany"</p>
<p>“x_example" -&gt; "x-example"</p></td>
<td>extensions are '-' not '_'</td>
<td><a href="https://github.com/oasis-open/openc2-custom-aps">Oasis</a></td>
<td></td>
</tr>
<tr class="even">
<td>stop_container_ext_target.json</td>
<td>"x_acme:containers" -&gt; "x-acme:containers"</td>
<td>extensions are '-' not '_'</td>
<td><a href="https://github.com/oasis-open/openc2-custom-aps">Oasis</a></td>
<td></td>
</tr>
</tbody>
</table>

### Bad Responses

| File                                       | Changes                                | Reason                      | Source                                                   | Note |
| ------------------------------------------ | -------------------------------------- | --------------------------- | -------------------------------------------------------- | ---- |
| poetry\_results.json                       |                                        |                             | [Oasis](https://github.com/oasis-open/openc2-custom-aps) |      |
| query\_features\_all\_badprofile-v1.0.json | Version: “1.0-draft-2019-02" -\> “1.0” | Language compliance         | [Oasis](https://github.com/oasis-open/openc2-custom-aps) |      |
| results\_ext\_empty.json                   | "x\_acme" -\> "x-acme"                 | extensions are '-' not '\_' | [Oasis](https://github.com/oasis-open/openc2-custom-aps) |      |

### Good Responses

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
<td>ls_example_query_properties_battery.json</td>
<td>"x_esm" -&gt; "x-esm"</td>
<td>extensions are '-' not '_'</td>
<td><a href="https://github.com/oasis-open/openc2-custom-aps">Oasis</a></td>
<td></td>
</tr>
<tr class="even">
<td>query_features_all_badprofile.json</td>
<td>Version: “1.0-draft-2019-02" -&gt; “1.0”</td>
<td>Language compliance</td>
<td><a href="https://github.com/oasis-open/openc2-custom-aps">Oasis</a></td>
<td></td>
</tr>
<tr class="odd">
<td>results_ext_multiple.json</td>
<td>"x_acme" -&gt; "x-acme"<br />
"x_mycompany" -&gt; "x-mycompany"</td>
<td>extensions are '-' not '_'</td>
<td><a href="https://github.com/oasis-open/openc2-custom-aps">Oasis</a></td>
<td></td>
</tr>
<tr class="even">
<td>results_ext_single.json</td>
<td>"x_mycompany" -&gt; "x-mycompany"</td>
<td>extensions are '-' not '_'</td>
<td><a href="https://github.com/oasis-open/openc2-custom-aps">Oasis</a></td>
<td></td>
</tr>
</tbody>
</table>
