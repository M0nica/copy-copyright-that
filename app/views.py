# views.py

from flask import Flask, render_template, request, redirect, url_for
import requests

from app import app

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/contribute')
def about():
    return render_template("contribute.html")

@app.route("/", methods=['POST'])
def calculate():
    business_name = str(request.form['business_name'])


    return redirect(url_for('results', business_name=business_name))


@app.route('/results/<business_name>')


def results(business_name):
    # searches https://domainsdb.info/apidomainsdb/ to determine if domain is available
    # cctld = country code top-level domain (ccTLD)
    response = requests.get('https://api.domainsdb.info/search?query=' + business_name +  '.com&tld=cctld')
    data = response.json()

    if data['total'] == 0:
        domain_availability = str(business_name + ".com") + " is available"
    # elif data['domains'][0] == str(business_name + ".com"):
    #     domain_availibility = business_name + ".com is not available"
    else:
        domain_availability =  str(data['domains'][0] + " not available")

    # print(data)
    business_name = business_name



    return render_template('results.html', business_name=business_name, domain_availability=domain_availability)
