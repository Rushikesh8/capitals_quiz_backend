def update_db_object(db_object,update_data):
    for attribute,value in update_data.items():
        setattr(db_object,attribute,value)
    db_object.save()
    return db_object