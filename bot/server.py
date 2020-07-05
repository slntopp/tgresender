from flask import Flask, request, render_template, jsonify
from bot.scripts.generate_session import *
import bot.conf as conf
import os

app = Flask(__name__, template_folder='/app/public',
            static_folder='/app/public/static')

conf = conf.load()
api_id, api_hash = conf['api_id'], conf['api_hash']
tg_app = {
    "app": gen_client(api_id, api_hash)
}
tg_app["app"].connect()


@app.route('/send_code', methods=['POST'])
def handle_send_code():
    tg_app["phone_number"] = request.form.get('phone_number', False)
    if tg_app["phone_number"]:
        tg_app["phone_code_hash"] = send_code(
            tg_app["app"], tg_app["phone_number"])
    return '', 200


@app.route('/enter_code', methods=['POST'])
def handle_enter_code():
    code = request.form.get('code', False)
    if not code:
        return '', 400

    tg_app["user"] = enter_code(
        tg_app["app"], tg_app["phone_number"], tg_app["phone_code_hash"], code)
    if not tg_app["user"]:
        return jsonify({
            "success": False,
            "password_required": True,
            "hint": tg_app["app"].get_password_hint()
        })
    return jsonify({
        "success": True,
        "name": tg_app["user"].first_name if not tg_app["user"].is_bot else tg_app["user"].username
    })


@app.route('/enter_pass', methods=['POST'])
def handle_enter_pass():
    passwd = request.form.get('passwd', False)
    if not passwd:
        return '', 400
    tg_app["user"] = tg_app["app"].check_password(passwd)
    return jsonify({
        "success": True,
        "name": tg_app["user"].first_name
    })


@app.route('/state', methods=['GET'])
def get_state():
    return 'Running...'

# Dashboard section


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
