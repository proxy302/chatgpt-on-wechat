# -*- coding:utf-8 -*-
import time
import db

def get_model_by_id(id):
    return db.mysql.get("SELECT * FROM t_models WHERE id = %s", id)
