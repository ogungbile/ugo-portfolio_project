from flask import Flask, render_template, request, flash, redirect
from netmiko import ConnectHandler

app = Flask(__name__)

@app.route("/login")
def index():
	return render_template("index.html")

@app.route("/cpanel", methods=["POST", "GET"])
def cpanel():
	if request.method == 'POST':
		request.form['name_input']
		if str(request.form['name_input']):
			return redirect('cpanel')

	return render_template("cpanel.html")

@app.route("/rboard", methods=["POST", "GET"])
def rboard():
	if request.method == 'POST':
		passkey=str(request.form['name_input'])
		if passkey:
			router_mikrotik = {
    				'device_type': 'mikrotik_routeros',
    				'host':   '102.135.221.206',
    				'username': 'admin',
    				'password': '3ndUzerP@ass',
    
				}
			passkey=str(request.form['name_input'])
			passkey2='/interface wireless security-profiles set 1 wpa2-pre-shared-key=' + '"' + passkey + '"'
			net_connect = ConnectHandler(**router_mikrotik)
			output = net_connect.send_command(passkey2)
			output2 = net_connect.send_command('/interface wireless set 0 ssid="Virus"')
			print(output)
			print(passkey2)
	return render_template("cpanel.html")
					
		