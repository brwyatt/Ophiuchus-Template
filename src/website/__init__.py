from ophiuchus.framework import route
from ophiuchus.framework import Handler


@route("/")
class Placeholder(Handler):
    def GET(self, event, context):
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "text/html"},
            "body": "\n".join(
                [
                    "<html>",
                    "<head>",
                    "<title>Ophiuchus - Hello World</title>",
                    "</head>",
                    "<body>",
                    "<h1>Hello World</h1>",
                    "<p>Example Ophiuchus handler.</p>",
                    "<p>Please edit the setup.py file to include your own",
                    "entry_points for your site's group and handlers.</p>",
                    "</body>",
                    "</html>",
                ],
            ),
        }
