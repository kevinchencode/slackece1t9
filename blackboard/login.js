var Horseman = require('node-horseman');
var horseman = new Horseman();


horseman
	.userAgent("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36")
	//.viewport(3200, 1800)
	.open("https://portal.utoronto.ca")
	.click("a[title='Login']")
	.waitForNextPage()
	.type('input[name="user"]', 'chenka24')
	.type('input[name="pass"]', 'R7362L58')
	.click("button[name='login']")
	.waitForNextPage()
	.url()
	.log()
	.close();