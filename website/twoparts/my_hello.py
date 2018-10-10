from datetime import datetime

def hello_app(environ, start_response):
    status = '200 OK'  # HTTP Status
    headers = [('Content-type', 'text/html; charset=utf-8')]  # HTTP Headers
    start_response(status, headers)

    mydtetme = datetime.now().ctime()
    
    content='''<p>The time is now {} Surprise!'''.format(mydtetme)
    
    
    
    # The returned object is going to be printed
    # return [b"Hello World"]
    
    return[bytes(content, 'UTF-8')]
