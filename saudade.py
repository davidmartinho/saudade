import bottle
import jinja2
import json

class StripPathMiddleware(object):
	def __init__(self, app):
		self.app = app
	def __call__(self, e, h):
		e['PATH_INFO'] = e['PATH_INFO'].rstrip('/')
		return self.app(e,h)

app = bottle.Bottle()
app.jinja2_env = jinja2.Environment(loader=jinja2.FileSystemLoader("views/"))

def renderTemplate(name, jsonPayload):
	return app.jinja2_env.get_template(name + '.html').render(jsonPayload)

@app.route('/static/<path:path>')
def callback(path):
    return bottle.static_file(path, root='static')

@app.route('<url:re:.+>')
def index(url):
	try:
		json_data = open("routes.json")
		data = json.load(json_data)
		if(url in data):
			if("file" in data[url]):
				template = data[url]["file"]
				if("data" in data[url]):
					payload = data[url]["data"]
				else:
					payload = iter(())
				return renderTemplate(template, payload)
			else:
				raise bottle.HTTPError(404, "Template file for %s not specified in routes.json" % url)
		else:
			raise bottle.HTTPError(404, "Url %s was not found on routes.json" % url)
	except IOError:
		raise bottle.HTTPError(404, "The file routes.json could not be found")


myapp = StripPathMiddleware(app)
bottle.run(host='localhost', port=8080, app=myapp)