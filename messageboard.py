from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from datetime import datetime

messages = []
class MessageBoardHandler(BaseHTTPRequestHandler):

  def do_GET(self):
    if self.path == '/':
      self.send_response(200)
      self.send_header('Content-type', 'text/html')
      self.end_headers()
      with open('messageboard.html', 'rb') as html:
        self.wfile.write(html.read())

      self.wfile.write(bytes('<ul>', 'utf-8'))

      for message in reversed(messages):
        self.wfile.write(bytes('<li>{}</li>'.format(message), 'utf-8'))

      self.wfile.write(bytes('</ul></body></html>', 'utf-8'))

    else:
      self.send_response(404)
      self.end_headers()
      self.wfile.write(bytes('Not Found', 'utf-8'))

  def do_POST(self):
    if self.path == '/post':
      content_length = int(self.headers['Content-Length'])
      post_data = self.rfile.read(content_length).decode('utf-8')
      params = parse_qs(post_data)
      message = params['message'][0]

      if not message or len(message) > 128:
        self.send_response(400)
        self.end_headers()
        return

      timestamp = datetime.now().strftime("%I:%M:%S %p")
      messages.append('{} <br> {}'.format(message, timestamp))

      self.send_response(303)
      self.send_header('Location', '/')
      self.end_headers()
    else:
      self.send_response(404)
      self.end_headers()
      self.wfile.write(bytes('Not Found', 'utf-8'))

if __name__ == '__main__':
  server_address = ('', 8000)
  httpd = HTTPServer(server_address, MessageBoardHandler)
  httpd.serve_forever()