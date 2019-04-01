
def jwt_response_payload_handler(token, user=None, request=None):
    """
    自定义jwt认证成功返回数据
    """
    return {
        'token': token,
        'user_id': user.id,  # 自定义字段1
        'username': user.username,  # 自定义字段2
        'last_name': user.last_name,
    }
