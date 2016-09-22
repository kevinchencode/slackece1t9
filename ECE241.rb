message = ARGV[0]
hello = `curl -X POST --data-urlencode 'payload={"channel": "#developers", "username": "digitalsystemsbot", "text": "#{ARGV[0]}", "icon_url": "https://avatars.slack-edge.com/2016-09-20/81985374709_3d122dfc770e342ead21_48.jpg"}' https://hooks.slack.com/services/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`
puts hello
