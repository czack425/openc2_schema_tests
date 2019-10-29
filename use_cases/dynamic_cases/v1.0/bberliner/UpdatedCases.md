# Updated Use Cases

  - Changes made for Language Spec compliance

## SLPF-Acme Use Cases

### Bad Commands

| File                                           | Changes | Reason | Source                                                            | Note                                                        |
| ---------------------------------------------- | ------- | ------ | ----------------------------------------------------------------- | ----------------------------------------------------------- |
| action\_notarget.json                          |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                                             |
| action\_notarget\_id.json                      |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                                             |
| action\_unknown.json                           |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                                             |
| allow\_ipv4net\_badcidr.json                   |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                                             |
| allow\_ipv4net\_badip.json                     |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                                             |
| allow\_ipv6net\_wikipedia3.json                |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                                             |
| args\_empty.json                               |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                                             |
| deny\_file\_hashes\_empty.json                 |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                                             |
| deny\_file\_hashes\_sha512.json                |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                                             |
| deny\_uri\_actuator\_empty.json                |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                                             |
| deny\_uri\_actuator\_multiple.json             |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) | Moved from good command, multiple actuators invalid in V1.0 |
| empty.json                                     |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                                             |
| empty\_array.json                              |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                                             |
| empty\_object.json                             |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                                             |
| number.json                                    |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                                             |
| number\_integer.json                           |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                                             |
| openc2\_response.json                          |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                                             |
| openc2\_response\_text.json                    |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                                             |
| query\_features\_ext\_args\_capX.json          |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                                             |
| query\_features\_ext\_args\_dots.json          |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                                             |
| query\_features\_ext\_args\_nox-.json          |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                                             |
| query\_features\_ext\_args\_specialchar.json   |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                                             |
| query\_features\_notunique.json                |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                                             |
| query\_features\_unknown.json                  |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                                             |
| query\_multiple\_target\_extensions.json       |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                                             |
| query\_multiple\_targets.json                  |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                                             |
| start\_container\_ext\_nocolon.json            |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                                             |
| start\_container\_ext\_noprofile.json          |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                                             |
| start\_container\_ext\_specialchar1.json       |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                                             |
| start\_container\_ext\_specialchar2.json       |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                                             |
| start\_container\_ext\_underscore\_first1.json |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                                             |
| start\_container\_ext\_underscore\_first2.json |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                                             |
| string.json                                    |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                                             |
| target\_multiple.json                          |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                                             |

### Good Commands

| File                                                                      | Changes | Reason | Source                                                            | Note |
| ------------------------------------------------------------------------- | ------- | ------ | ----------------------------------------------------------------- | ---- |
| allow\_device\_deviceid.json                                              |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| allow\_file\_hashes\_sha256.json                                          |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| allow\_ipv4net.json                                                       |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| allow\_ipv4net\_cidr.json                                                 |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| allow\_ipv6net.json                                                       |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| allow\_ipv6net\_ipv4mapped\_orig.json                                     |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| allow\_ipv6net\_ipv4mapped\_result.json                                   |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| allow\_ipv6net\_localhost.json                                            |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| allow\_ipv6net\_localhost\_reduced.json                                   |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| allow\_ipv6net\_prefix.json                                               |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| allow\_ipv6net\_unspecified.json                                          |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| allow\_ipv6net\_unspecified\_reduced.json                                 |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| allow\_ipv6net\_wikipedia1.json                                           |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| allow\_ipv6net\_wikipedia10\_eui64.json                                   |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| allow\_ipv6net\_wikipedia11\_derrick.json                                 |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| allow\_ipv6net\_wikipedia2.json                                           |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| allow\_ipv6net\_wikipedia3.json                                           |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| allow\_ipv6net\_wikipedia4.json                                           |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| allow\_ipv6net\_wikipedia4\_shortened.json                                |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| allow\_ipv6net\_wikipedia5.json                                           |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| allow\_ipv6net\_wikipedia5\_shortened.json                                |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| allow\_ipv6net\_wikipedia6.json                                           |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| allow\_ipv6net\_wikipedia6\_shortened.json                                |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| allow\_ipv6net\_wikipedia7.json                                           |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| allow\_ipv6net\_wikipedia7\_shortened.json                                |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| allow\_ipv6net\_wikipedia8\_prefix1.json                                  |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| allow\_ipv6net\_wikipedia8\_prefix10\_example.json                        |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| allow\_ipv6net\_wikipedia8\_prefix11\_6to4.json                           |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| allow\_ipv6net\_wikipedia8\_prefix12\_unique\_local.json                  |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| allow\_ipv6net\_wikipedia8\_prefix13\_link\_local.json                    |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| allow\_ipv6net\_wikipedia8\_prefix14\_multicast.json                      |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| allow\_ipv6net\_wikipedia8\_prefix1\_end.json                             |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| allow\_ipv6net\_wikipedia8\_prefix1\_start.json                           |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| allow\_ipv6net\_wikipedia8\_prefix2.json                                  |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| allow\_ipv6net\_wikipedia8\_prefix3\_default\_route.json                  |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| allow\_ipv6net\_wikipedia8\_prefix3\_unspecified\_address.json            |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| allow\_ipv6net\_wikipedia8\_prefix4\_loopback\_address.json               |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| allow\_ipv6net\_wikipedia8\_prefix5\_ipv4\_mapped.json                    |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| allow\_ipv6net\_wikipedia8\_prefix5\_ipv4\_translated.json                |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| allow\_ipv6net\_wikipedia8\_prefix6\_ipv4\_translation.json               |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| allow\_ipv6net\_wikipedia8\_prefix7\_discard.json                         |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| allow\_ipv6net\_wikipedia8\_prefix8\_teredo.json                          |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| allow\_ipv6net\_wikipedia8\_prefix9\_ORCHIDv2.json                        |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| allow\_ipv6net\_wikipedia9\_multicast10\_RPL.json                         |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| allow\_ipv6net\_wikipedia9\_multicast11\_mDNSv6.json                      |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| allow\_ipv6net\_wikipedia9\_multicast12\_NTP.json                         |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| allow\_ipv6net\_wikipedia9\_multicast13\_link\_name.json                  |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| allow\_ipv6net\_wikipedia9\_multicast14\_dhcp\_agents.json                |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| allow\_ipv6net\_wikipedia9\_multicast15\_multicast\_name\_resolution.json |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| allow\_ipv6net\_wikipedia9\_multicast16\_dhcp\_servers.json               |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| allow\_ipv6net\_wikipedia9\_multicast17\_solicited\_node.json             |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| allow\_ipv6net\_wikipedia9\_multicast18\_node\_info.json                  |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| allow\_ipv6net\_wikipedia9\_multicast1\_nodes\_interface\_local.json      |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| allow\_ipv6net\_wikipedia9\_multicast2\_nodes\_link\_local.json           |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| allow\_ipv6net\_wikipedia9\_multicast3\_routers\_interface\_local.json    |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| allow\_ipv6net\_wikipedia9\_multicast3\_routers\_link\_local.json         |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| allow\_ipv6net\_wikipedia9\_multicast4\_routers\_site\_local.json         |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| allow\_ipv6net\_wikipedia9\_multicast5\_OSPFIGP.json                      |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| allow\_ipv6net\_wikipedia9\_multicast6\_OSPFIGP\_routers.json             |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| allow\_ipv6net\_wikipedia9\_multicast7\_RIP.json                          |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| allow\_ipv6net\_wikipedia9\_multicast8\_EIGRP.json                        |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| allow\_ipv6net\_wikipedia9\_multicast9\_PIM.json                          |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| contain\_device\_deviceid.json                                            |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| deny\_file\_hashes\_md5.json                                              |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| deny\_file\_hashes\_md5\_sha1.json                                        |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| deny\_file\_hashes\_md5\_sha1\_sha256.json                                |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| deny\_file\_hashes\_md5\_sha256.json                                      |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| deny\_file\_hashes\_sha1.json                                             |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| deny\_file\_hashes\_sha1\_sha256.json                                     |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| deny\_file\_hashes\_sha256.json                                           |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| deny\_macaddr.json                                                        |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| https\_example\_deny\_file\_hashes.json                                   |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| ls\_example\_contain\_device.json                                         |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| ls\_example\_deny\_ipv4connection.json                                    |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| ls\_example\_query\_features.json                                         |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| ls\_example\_query\_properties\_battery.json                              |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| query\_features\_all.json                                                 |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| query\_features\_all\_id.json                                             |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| query\_features\_empty.json                                               |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| query\_features\_empty\_id.json                                           |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| query\_features\_ext\_args.json                                           |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| query\_features\_ext\_args\_all.json                                      |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| query\_features\_ext\_args\_underscore.json                               |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| query\_features\_ext\_target.json                                         |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| query\_features\_extension\_args\_number.json                             |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| query\_features\_profiles.json                                            |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| query\_features\_profiles\_id.json                                        |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| query\_properties\_firewall\_status.json                                  |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| remediate\_file\_hashes\_sha256.json                                      |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| set\_properties\_firewall\_status.json                                    |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| slpf\_example\_allow\_ipv6connection.json                                 |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| slpf\_example\_delete\_rulenumber.json                                    |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| slpf\_example\_deny\_ipv4connection.json                                  |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| slpf\_example\_deny\_ipv6connection.json                                  |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| slpf\_example\_deny\_ipv6net.json                                         |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| slpf\_example\_update\_file.json                                          |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| start\_container\_ext\_target.json                                        |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| start\_container\_ext\_target\_ext\_actuator.json                         |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| start\_container\_ext\_target\_ext\_actuator\_ext\_args.json              |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| start\_container\_ext\_target\_ext\_actuator\_mult\_ext\_args.json        |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |
| stop\_container\_ext\_target.json                                         |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |      |

### Bad Responses

| File                                       | Changes | Reason | Source                                                            | Note                                                                  |
| ------------------------------------------ | ------- | ------ | ----------------------------------------------------------------- | --------------------------------------------------------------------- |
| empty.json                                 |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                                                       |
| empty\_array.json                          |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                                                       |
| empty\_object.json                         |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                                                       |
| openc2\_command\_query\_features\_all.json |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                                                       |
| query\_features\_all\_badprofile.json      |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                                                       |
| results\_empty.json                        |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) | Moved from good response, response requires a minimum of one property |
| results\_unknown\_profile.json             |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                                                       |
| status\_asbool.json                        |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                                                       |
| status\_asdouble.json                      |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                                                       |
| status\_asstring.json                      |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                                                       |
| status\_negative.json                      |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                                                       |
| status\_too\_high.json                     |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                                                       |
| status\_too\_low.json                      |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                                                       |
| statustext\_nostatus.json                  |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                                                       |
| unknown\_field.json                        |         |        | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                                                       |

### Good Responses

| File                                                | Changes                                | Reason              | Source                                                            | Note                                     |
| --------------------------------------------------- | -------------------------------------- | ------------------- | ----------------------------------------------------------------- | ---------------------------------------- |
| ls\_example\_query\_features.json                   |                                        |                     | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                          |
| ls\_example\_query\_properties\_battery.json        |                                        |                     | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                          |
| query\_features\_all.json                           | Version: “1.0-draft-2019-02” -\> “1.0” | Language compliance | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                          |
| results\_ext\_empty.json                            |                                        |                     | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                          |
| results\_ext\_multiple.json                         |                                        |                     | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) | 201 is not a valid response for language |
| results\_ext\_single.json                           |                                        |                     | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) | 201 is not a valid response for language |
| results\_slpf\_empty.json                           |                                        |                     | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                          |
| slpf\_example\_query\_features\_pairs\_example.json |                                        |                     | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                          |
| slpf\_example\_rule\_number.json                    |                                        |                     | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                          |
| status\_102.json                                    |                                        |                     | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                          |
| status\_200.json                                    |                                        |                     | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                          |
| status\_400.json                                    |                                        |                     | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                          |
| status\_401.json                                    |                                        |                     | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                          |
| status\_403.json                                    |                                        |                     | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                          |
| status\_404.json                                    |                                        |                     | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                          |
| status\_500.json                                    |                                        |                     | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                          |
| status\_501.json                                    |                                        |                     | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                          |
| status\_503.json                                    |                                        |                     | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                          |
| status\_and\_status\_text.json                      |                                        |                     | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                          |
| status\_only\_not\_implemented.json                 |                                        |                     | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                          |
| status\_only\_success.json                          |                                        |                     | [Brian Berliner](https://github.com/bberliner/openc2-json-schema) |                                          |
