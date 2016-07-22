# mattermost-pagerduty
Webhook middleware to accept pagerduty events and posting them into a channel.


#### Installing
Run `pip install -r requirements.txt`

#### Configuring
At a minimum you need to define your mattermost hook url.

#### Running
This application will by default listen on port `8000`. To start it run `python run.py` or alternatively run it in supervisord or similar.
