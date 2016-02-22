## cricinfo-slackbot

Slack bot that publishes cricinfo updates

### Usage

From slack channel type `/cricinfo`

### Integration

1. Go to your channel
2. Click on **Configure Integrations**.
3. Scroll all the way down to **DIY Integrations & Customizations section**.
4. Click on **Add** next to **Slash Commands**.
  - Command: `/cricinfo`
  - URL: `http://cricinfo-slack.herokuapp.com/cricinfo`
  - Method: `POST`
  - For the **Autocomplete help text**, check to show the command in autocomplete list.
    - Description: `Get live cricket updates from cricinfo on slack`
  - Descriptive Label: `Cricket Match Live Updates`

### Contributing

- Please use the [issue tracker](https://github.com/voidabhi/cricinfo-slackbot/issues) to report any bugs or file feature requests.
