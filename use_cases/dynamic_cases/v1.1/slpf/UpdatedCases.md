# Updated Use Cases

  - Changes made for Language Spec compliance

## SLPF Use Cases

### Bad Commands

| File                | Changes | Reason | Source                                                   | Note |
| ------------------- | ------- | ------ | -------------------------------------------------------- | ---- |
| poetry\_create.json |         |        | [Oasis](https://github.com/oasis-open/openc2-custom-aps) |      |

### Good Commands

| File                                      | Changes                                     | Reason              | Source                                                   | Note |
| ----------------------------------------- | ------------------------------------------- | ------------------- | -------------------------------------------------------- | ---- |
| ls\_example\_deny\_ipv4connection.json    |                                             |                     | [Oasis](https://github.com/oasis-open/openc2-custom-aps) |      |
| slpf\_example\_allow\_ipv6connection.json |                                             |                     | [Oasis](https://github.com/oasis-open/openc2-custom-aps) |      |
| slpf\_example\_delete\_rulenumber.json    | "slpf/rule\_number" -\> "slpf:rule\_number" | Language compliance | [Oasis](https://github.com/oasis-open/openc2-custom-aps) |      |
| slpf\_example\_deny\_ipv4connection.json  |                                             |                     | [Oasis](https://github.com/oasis-open/openc2-custom-aps) |      |
| slpf\_example\_deny\_ipv6connection.json  |                                             |                     | [Oasis](https://github.com/oasis-open/openc2-custom-aps) |      |
| slpf\_example\_deny\_ipv6net.json         |                                             |                     | [Oasis](https://github.com/oasis-open/openc2-custom-aps) |      |
| slpf\_example\_update\_file.json          |                                             |                     | [Oasis](https://github.com/oasis-open/openc2-custom-aps) |      |

### Bad Responses

| File                                 | Changes | Reason | Source                                                   | Note |
| ------------------------------------ | ------- | ------ | -------------------------------------------------------- | ---- |
| slpf\_query\_pairs\_bad\_action.json |         |        | [Oasis](https://github.com/oasis-open/openc2-custom-aps) |      |
| slpf\_query\_pairs\_bad\_pair.json   |         |        | [Oasis](https://github.com/oasis-open/openc2-custom-aps) |      |
| slpf\_query\_pairs\_bad\_target.json |         |        | [Oasis](https://github.com/oasis-open/openc2-custom-aps) |      |

### Good Responses

| File                                                | Changes                                     | Reason             | Source                                                   | Note |
| --------------------------------------------------- | ------------------------------------------- | ------------------ | -------------------------------------------------------- | ---- |
| results\_slpf\_empty.json                           |                                             |                    | [Oasis](https://github.com/oasis-open/openc2-custom-aps) |      |
| slpf\_example\_query\_features\_pairs\_example.json | "slpf/rule\_number" -\> "slpf:rule\_number" | Profile compliance | [Oasis](https://github.com/oasis-open/openc2-custom-aps) |      |
| slpf\_example\_rule\_number.json                    |                                             |                    | [Oasis](https://github.com/oasis-open/openc2-custom-aps) |      |
