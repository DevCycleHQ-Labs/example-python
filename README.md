# DevCycle Python Server SDK Example App
An example app built using the [DevCycle Python Server SDK](https://docs.devcycle.com/sdk/server-side-sdks/python/)

## Requirements.

Python 3.7+ and Django 4.2+

## Creating a Demo Feature
This example app requires that your project has a feature with the expected variables, as well as some simple targeting rules. 

#### ⇨ [Click here](https://app.devcycle.com/r/create?resource=feature&key=hello-togglebot) to automatically create the feature in your project ⇦

When you run the example app and switch your identity between users, you'll be able to see the feature's different variations.

## Running the Example
### Setup

* Create a `.env` file and set `DEVCYCLE_SERVER_SDK_KEY` to your Environment's SDK Key.\
You can find this under [Settings > Environments](https://app.devcycle.com/r/environments) on the DevCycle dashboard.
[Learn more about environments](https://docs.devcycle.com/essentials/environments).
* Run `python3 -m pip install -r requirements.txt` in the project directory to install dependencies. You may need to run `pip` with root permission: `sudo pip install -r requirements.txt`
* Run `python3 manage.py migrate` to apply migrations

### Development

`python3 manage.py runserver`

The server will start on port 8000. You can access the example app at http://localhost:8000.

## Documentation
For more information about using the DevCycle Python Server SDK, see [the documentation](https://docs.devcycle.com/sdk/server-side-sdks/python/)

