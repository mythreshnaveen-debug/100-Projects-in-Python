#Project 54 - About Me Page (using Flask)
# Small project i made to learn the ins and outs of flask
from flask import Flask
app = Flask(__name__)

#this page was made by AI, since I actually did not have an about me page to use.
basicAboutMePage =  """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>About Me</title>
</head>

<body>
  <h1>About Me</h1>

  <p>
    Hi! My name is Mk, and I enjoy learning how to code and build cool projects.
    I like experimenting with technology, problem-solving, and creating things
    that people can interact with.
  </p>

  <h2>My Interests</h2>
  <ul>
    <li>Coding & Programming</li>
    <li>Game Development</li>
    <li>Learning New Technologies</li>
    <li>Creative Projects</li>
  </ul>

  <h2>What I'm Working On</h2>
  <p>
    Right now, I’m focusing on improving my coding skills and working on personal
    projects to better understand how websites and games are built.
  </p>

  <h2>Fun Fact</h2>
  <p>
    I enjoy challenging myself with new ideas and figuring out how things work
    behind the scenes.
  </p>

  <hr>

  <p>
    Thanks for visiting my page!
  </p>
</body>
</html>
"""

@app.route('/')
def hello_world():
    return "<h2>Welcome world!</h2>"

@app.route('/about')
def about():
    return basicAboutMePage


if __name__ == "__main__":
    app.run()
