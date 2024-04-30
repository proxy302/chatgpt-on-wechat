#-*- coding:utf-8 -*-
import time
import db


def get_token_mapping_by_id(id):
    return db.mysql.get("SELECT * FROM t_token_mapping WHERE id = %s", id)
