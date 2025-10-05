from   flask import Blueprint, request, jsonify

logout = Blueprint('logout', __name__)
@logout.route('/logout', methods=['POST'])
def logout_user(): #función
    print("Headers:", request.headers)
    print("Body:", request.json)