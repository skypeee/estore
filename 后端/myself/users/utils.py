def jwt_response_payload_handler(token, user=None, request=None):
    """为返回的结果添加用户相关信息"""

    return {
        'token': token,
        'user_id': user.id,
        'username': user.username,
        'signature': user.user_signature,
        'last_name': user.last_name,
        'user_address': user.user_address
    }
