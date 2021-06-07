def collision(object1, object2):
    result = object1.map.overlap(object2.map, (int(object2.x - object1.x), int(object2.y - object1.y)))
    if result:
        result = True
    else:
        result = False
    return result
