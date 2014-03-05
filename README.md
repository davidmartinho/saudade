# Saudade

Saudade is a project that aims to facilitate the web designer task of prototyping front-ends, and simultaneously ease the integration with the web developers code to make dynamic web pages.

## Requirements

You will need python and virtualenv.

## Setup

Then, clone the project to your local development environment, create a new virtual environment (NOTE: you only need to do this once):

	virtualenv ENV

The command above will generate a new folder that essentialy contains the Python environment where the project will run. However, to make it work, you need to activate such environment by running the following command:

	source ENV/bin/activate

After you run the command above, you can check your terminal line begins with ```(ENV)```. This means you have this virtual environment activated. To deactivate it, you can simply run ```deactivate```.

While you have the virtual environment active, you can install all the requirements that Saudade needs to run (NOTE: you should run this once):

	pip install -r requirements.txt

Then, you are able to run Saudade. All you need to do is:
	
	python saudade.py

And you can access the application in:
	
	http://localhost:8080/

## Configuration
The first thing you need to do is to edit the ```routes.json``` file and specify your application routes:

	{
		"/users": {
			"file": "list-users"
		}
	}

The example above tells Saudade that when you access ```http://localhost:8080/users``` then the file ```views/list-users.html``` will be loaded.

### Providing data to the template
If you want to provide data to a template, you can add the data field to the entry in the ```routes.json``` file:

        {
                "/users": {
                        "file": "list-users", "data": { "users": [{"name": "John Doe"}, {"name": "Jane Doe"}] }
                }
        }

This means that you can then iterate over the users array in ```view/list-users.html``` like in the following example:
	
	<ul>
	{% for user in users %}
		<li>{{user.name}}</li>
	{% endfor %}
	</ul>

