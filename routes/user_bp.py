from flask import Blueprint

from controllers.UserController import *

user_bp = Blueprint('user_bp', __name__)

user_bp.route('/', methods=['GET'])(index)
user_bp.route('/create', methods=['GET'])(create)
user_bp.route('/create', methods=['POST'])(store)
user_bp.route('/viewAll', methods=['GET'])(userList)
user_bp.route('/viewSeceltion', methods=['GET', 'POST'])(viewSeceltion)
user_bp.route('/view/<int:user_id>', methods=['GET'])(show)
user_bp.route('/updateSelection', methods=['GET', 'POST'])(updateSelection)
user_bp.route('/update/<int:user_id>', methods=['GET'])(edit)
user_bp.route('/update/<int:user_id>', methods=['POST'])(update)
user_bp.route('/deleteSelection', methods=['GET', 'POST'])(deleteSelection)
user_bp.route('/delete/<int:user_id>', methods=['GET', 'POST'])(delete)
