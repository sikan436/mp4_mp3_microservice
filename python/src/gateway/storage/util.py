import pika,json

import pika.spec


def upload(f,fs,channel,access):
    try:
        fid=fs.put(f)
    except Exception as err:
        return "internal server error ",500
    
    message={
        "video_fid":str(fid),
        "mp3_fid":None,
        "username":access["username"],
    }
    

    try:
        channel.basic_publish(
            exchange='',
            routing_key="video",
            message=json.dumps(message),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ),

            )
    except:
        fs.delete(fid)
        return "internal server errror",500