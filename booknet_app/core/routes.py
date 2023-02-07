from flask import render_template, Blueprint, request, redirect
from booknet_app.core.forms import NewsletterForm
import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError
from config import mailchimp_audienceid, mailchimp_apikey, mailchimp_serverprefix

core = Blueprint('core', __name__)

def mailchimp_newsletter(email):
    try:
        client = MailchimpMarketing.Client()
        client.set_config({
            "api_key": mailchimp_apikey,
            "server": mailchimp_serverprefix
        })

        response = client.lists.add_list_member(mailchimp_audienceid, {"email_address": email, "status": "subscribed"})
        print(response)
        return response
    
    except ApiClientError as error:
        print(error.status_code)
        return error.status_code

@core.route('/', methods=["GET","POST"])
@core.route('/home', methods=["GET","POST"])
def index():
    form = NewsletterForm()
    status = mailchimp_newsletter(form.email.data)
    return render_template('index.html', form=form, status=status)

@core.route('/newsletter', methods=["GET","POST"])
def newsletter():
    form = NewsletterForm()
    status = mailchimp_newsletter(form.email.data)
    return redirect(request.referrer)
