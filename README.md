# README

This is the [Flask](http://flask.pocoo.org/) [quick start](http://flask.pocoo.org/docs/1.0/quickstart/#a-minimal-application) example for [Render](https://render.com).

The app in this repo is deployed at [https://flask.onrender.com](https://flask.onrender.com).

## Deployment

Follow the guide at https://render.com/docs/deploy-flask.

# 中文
执行
gunicorn app:app


# 问题
- render No open HTTP ports detected
https://community.render.com/t/no-open-http-ports-detected/14511/2
Ensure the server is listening on 0.0.0.0, and not 127.0.0.1.
