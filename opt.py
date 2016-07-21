from tornado.options import define, options


define('mattermost_url', default="https://your.mattermost.url/hooks/id")
define('port', default=8000)
