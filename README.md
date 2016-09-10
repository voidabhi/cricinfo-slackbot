## cricinfo-slackbot

Slack bot that publishes cricinfo updates

![cricinfo.com](https://raw.githubusercontent.com/voidabhi/cricinfo-slackbot/master/espn-cricinfo-cribuzz.png)

### Usage

From slack channel type `/cricinfo`

### Integration

1. Go to your channel
2. Click on **Configure Integrations**.
3. Scroll all the way down to **DIY Integrations & Customizations section**.
4. Click on **Add** next to **Slash Commands**.
  - Command: `/cricinfo`
  - URL: `https://cricinfo-slack.herokuapp.com/cricinfo`
  - Method: `POST`
  - For the **Autocomplete help text**, check to show the command in autocomplete list.
    - Description: `Get live cricket updates from cricinfo on slack`
  - Descriptive Label: `Cricket Match Live Updates`

### Contributing

- Please use the [issue tracker](https://github.com/voidabhi/cricinfo-slackbot/issues) to report any bugs or file feature requests.

### LICENSE

```
Copyright 2016 Abhijeet Mohan - https://github.com/voidabhi/cricinfo-slackbot

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
