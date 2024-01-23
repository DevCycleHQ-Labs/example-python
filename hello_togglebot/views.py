from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def home_page(request):
    step = request.devcycle.variable_value(request.user, "example-text", "default")

    header = ""
    body = ""
    if step == "step-1":
        header = "Welcome to DevCycle's example app."
        body = "If you got here through the onboarding flow, just follow the instructions to change and create new Variations and see how the app reacts to new Variable values."
    elif step == "step-2":
        header = "Great! You've taken the first step in exploring DevCycle."
        body = "You've successfully toggled your very first Variation. You are now serving a different value to your users and you can see how the example app has reacted to this change. Next, go ahead and create a whole new Variation to see what else is possible in this app."
    elif step == "step-3":
        header = "You're getting the hang of things."
        body = "By creating a new Variation with new Variable values and toggling it on for all users, you've already explored the fundamental concepts within DevCycle. There's still so much more to the platform, so go ahead and complete the onboarding flow and play around with the feature that controls this example in your dashboard."
    else:
        header = "Welcome to DevCycle's example app."
        body = "If you got to the example app on your own, follow our README guide to create the Feature and Variables you need to control this app in DevCycle."
    
    response = '<h2>{header}</h2><p>{body}</p><p><a href="/variables">All Variables</a></p>'.format(header=header, body=body)
    return HttpResponse(response)

def get_variables(request):
    variables = request.devcycle.all_variables(request.user)
    response = ''
    for key, variable in variables.items():
        response += '<li><strong>{key}</strong>: {value}</li>'.format(key=key, value=variable.value)
    return HttpResponse('<h2>Variables</h2><ul>' + response + '</ul><p><a href="/">Home</a></p>')
