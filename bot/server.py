from flask import Flask, request, render_template, jsonify
from bot.scripts.generate_session import *
import bot.conf as conf_gateway
import os

app = Flask(__name__, template_folder='/app/public',
            static_folder='/app/public/static')

conf = conf_gateway.load()
tg_app = {}


@app.route('/init_client', methods=['POST'])
def handle_init_client():
    global conf
    global tg_app

    form = request.form
    api_id, api_hash = form.get(
        'api_id', ''), form.get('api_hash', '')
    conf_gateway.set_api(api_id, api_hash)

    conf = conf_gateway.load()
    tg_app["app"] = gen_client(api_id, api_hash)
    tg_app["app"].connect()

    return jsonify({
        "result": "success"
    }), 200


@app.route('/get_conf', methods=['GET'])
def get_conf():
    global conf
    try:
        return jsonify(conf)
    except:
        return jsonify({})


@app.route('/send_code', methods=['POST'])
def handle_send_code():
    global tg_app
    tg_app["phone_number"] = request.form.get('phone_number', False)
    if tg_app["phone_number"]:
        tg_app["phone_code_hash"] = send_code(
            tg_app["app"], tg_app["phone_number"])
    return jsonify({
        "result": "success"
    }), 200


@app.route('/enter_code', methods=['POST'])
def handle_enter_code():
    global tg_app

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
        "name": "%s %s" % (tg_app["user"].first_name, tg_app["user"].last_name) if not tg_app["user"].is_bot else tg_app["user"].username
    })


@app.route('/enter_pass', methods=['POST'])
def handle_enter_pass():
    global tg_app

    passwd = request.form.get('passwd', False)
    if not passwd:
        return '', 400
    tg_app["user"] = tg_app["app"].check_password(passwd)
    return jsonify({
        "success": True,
        "name": "%s %s" % (tg_app["user"].first_name, tg_app["user"].last_name)
    })


@app.route('/state', methods=['GET'])
def get_state():
    return 'Running...'

# Panel section


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/login/', methods=['POST'])
def handle_login():
    return jsonify({"result": request.args.get('passwd', '') == open('/app/bot/scripts/token.txt').read()[:-1]})
