## Project requirements

### General requirements
- Check registered AedanStream streams to see if anyone has started broadcasting. Then send notifications to desired endpoints according to the configurations and user preferences.
- Include a title and a description and optionally some links for the end users to quickly join the stream.
- If the offline gap of a stream is less than about 10 minutes, do not send new notifications.
- Notification endpoints:
  - Telegram Bot
  - Discord (Webhooks)
  - SMS
- Streamers and viewers should be able to manage their settings and preferences about sending and recieving notifications using a Telegram bot.
- The Telegram bot may be added to groups and channels to send notification. Respective configurations for those groups and channels are done directly inside their chats.
- The app is expected to be as light as possible and to handle at least 20 streams without much effort and lag.

### Telegram Bot
- Each user needs a one-time token to authorize himself. The bot only serves the authorized users.
- This one-time token is provided by the system admin. Once the token is consumed by the bot, the user's telegram account is authorized forever unless the admin revokes the user permissions.
- Streamer can choose one of his streams to manage.
- Stream details including title (category) and a short description can be set permanently or temporarily.
- Sending notifications for a stream can be turned on or off and also it is possible to temporarily disable notifications.
- Each notification endpoint can be separately enabled or disabled.
- Streamer may add his own dedicated Discord webhooks to his stream's notifications endpoints.
- There should be an option to enable one-time SMS notification for a specific stream. It also is temporary and the period can be set by the streamer before this setting expires.
- Number of sent SMS notifications should be limited in a week or month per streamer.
- Users can decide if they like to recieve direct notifications from the bot or from SMS, and if they do like to get direct notifications, they can choose which stream's notifications they want to get.
- Each user can only register 1 phone number for recieving SMS notifications.
- Adding the bot to a group or channel requires a new one-time token. After activating the bot in the group or channel, only the person who activated the bot can manage it using the chat and inline comamnds.
- The bot can send a message to the group or channel when one of the chosen streams goes live.

### Management panel
- The system admin can manage some basic settings and permissions by utilizing a simple command-line script on the server.
- Some of the available options for the admin are:
  - Manage default notification endpoints. (eg. Discord webhooks, ...)
  - Register streamers and their stream ids.
  - Create one-time toekns for specific users and for specific uses.
  - Manage user permissions and limitations. (eg. SMS limits)
  - Monitor the system and query the stats. (Usage reports and more...)

### Technical requirements
- Application's state should be stored on disk and the application is expected to restore its previous state after a restart.
- Logs should be stored locally.
- main app configurations are preferred be stored in a `YAML` or `JSON` file.
- It is suggested to use `sqlite` database for storing application's state and data.