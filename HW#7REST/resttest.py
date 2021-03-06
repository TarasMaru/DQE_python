import time


def notfound_404(environ, start_response):
    start_response('404 Not Found', [('Content-type', 'text/plain')])
    return [b'Not Found']

_hello_resp = (
               '    <html>\n'
               '        <head>\n'
               '            <title>Hello {name}</title>\n'
               '        </head>\n'
               '        <body>\n'
               '            <h1>Hello {name}!</h1>\n'
               '        </body>\n'
               '    </html>')


def hello_world(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/html')])
    params = environ['params']
    resp = _hello_resp.format(name=params.getvalue('name'))
    yield resp.encode('utf-8')


_localtime_resp = ('<?xml version="1.0"?>\n'
                   '        <time>\n'
                   '            <year>{t.tm_year}</year>\n'
                   '            <month>{t.tm_mon}</month>\n'
                   '            <day>{t.tm_mday}</day>\n'
                   '            <hour>{t.tm_hour}</hour>\n'
                   '            <minute>{t.tm_min}</minute>\n'
                   '            <second>{t.tm_sec}</second>\n'
                   '        </time>')

#html code to display image in browser
_img_resp =('<html xmlns="http://www.w3.org/1999/xhtml">\n'
                   '        <head>\n'
                   '            <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\n'
                   '            <title>Image to server</title>\n'
                   '            </head>\n'
                   '            <body>\n'
                   '            <img src="{img_net}" alt="Image to server" />\n'
                   '       </body></html>')


pictures = {'"CrewDragon"': 'https://delo.ua/files/news/images/3635/38/picture2_spacex-provela-fi_363538_p0.jpg'}


def show_pic(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/html')])
    params = environ['params']
    url = pictures.get(params.getvalue('name'), 'https://bitsofco.de/content/images/2018/12/broken-1.png')
    resp = _img_resp.format(img_net=url)
    yield resp.encode('utf-8')


def localtime(environ, start_response):
    start_response('200 OK', [('Content-type', 'application/xml')])
    resp = _localtime_resp.format(t=time.localtime())
    yield resp.encode('utf-8')
