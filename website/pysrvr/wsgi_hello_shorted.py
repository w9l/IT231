from wsgiref.simple_server import make_server

from ? import hello_world_app

with make_server('', 3000, hello_world_app) as httpd:
    print("Serving on port 3000...")
    httpd.serve_forever()