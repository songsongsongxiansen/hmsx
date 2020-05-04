from flask import Blueprint,render_template,request,jsonify,make_response
from common.models.User import User
from common.libs.user.UserService import UserService

import json    

    router_user = Blueprint('user_page',__name__)
    
        resp['code'] = -1
        resp['msg'] = "请输入正确的密码"
        return jsonify(resp)
    
    # 从数据库中取出user
    user_info = User.query.filter_by(login_name=login_name).first()
    if not user_info:
        resp['code'] = -1
        resp['msg'] = "用户不存在"
        return jsonify(resp)
    # 判断密码
    if user_info.login_pwd != UserService.generatePwd(login_pwd,user_info.login_salt):
        resp['code'] = -1
        resp['msg'] = "密码输入错误"
        return jsonify(resp)

    # 判断用户状态
    if user_info.status != 1:
        resp['code'] = -1
        resp['msg'] = "用户已经被禁用，请联系管理员处理"
        return jsonify(resp)

    response = make_response(json.dumps({'code':200,'msg':'登录成功~~~'}))
    # Cookie中存入的信息是user_info.uid,user_info
    response.set_cookie("hmsc_1901C","%s@%s"%(UserService.generateAuthCode(user_info),user_info.uid),60*60*24*15)
    return response

@router_user.route("/logout")
def logout():
    return "登出"

@router_user.route("/edit")
def edit():
    return "编辑"

@router_user.route("/reset-pwd")
def resetPwd():
    return "重置密码" 