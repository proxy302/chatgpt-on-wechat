#-*- coding:utf-8 -*-
import time
import db


def get_robot_mapping_by_feishu_token(token):
    return db.mysql.get("SELECT * FROM t_robot_mapping WHERE feishu_verification_token = %s and deleted_on = 0", token)
