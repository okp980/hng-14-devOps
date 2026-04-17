# Stage 2 — FastAPI service

A minimal FastAPI application for HNG DevOps stage 2: a small HTTP API behind nginx in production, with a root check, a health probe, and a `/me` profile endpoint. Nginx (`nginx.conf`) reverse-proxies port 80 to the app on `localhost:8000`.

## Run locally

```bash
cd stage-2
source .venv/bin/activate   # optional, if using the bundled venv
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Install dependencies without the venv: `pip install fastapi uvicorn`.

API docs: `http://127.0.0.1:8000/docs`

## On a Linux server (FastAPI + nginx)

Install Python and the app dependencies, then run the API on port 8000 (what nginx proxies to):

```bash
sudo apt update && sudo apt install -y python3 python3-pip python3-venv
cd /path/to/stage-2
python3 -m venv .venv && source .venv/bin/activate
pip install fastapi uvicorn
uvicorn main:app --host 0.0.0.0 --port 8000
```

Install nginx, copy this repo’s `nginx.conf` into `/etc/nginx` (for example Ubuntu loads snippets under `conf.d`, so you can use `sudo cp nginx.conf /etc/nginx/conf.d/stage-2.conf`), check the config, then start or reload nginx:

```bash
sudo apt install -y nginx
sudo cp nginx.conf /etc/nginx/conf.d/stage-2.conf
sudo nginx -t && sudo systemctl reload nginx
```

If nginx is not running yet: `sudo systemctl start nginx` (and `sudo systemctl enable nginx` if you want it on boot). Visit `http://<server-ip>/` on port 80; `/`, `/healthy`, and `/me` are forwarded to FastAPI.

## Endpoints


| Method | Path       | Response                                |
| ------ | ---------- | --------------------------------------- |
| GET    | `/`        | `{"message": "API is running"}`         |
| GET    | `/healthy` | `{"message": "healthy"}`                |
| GET    | `/me`      | JSON with `name`, `email`, and `github` |


live url: hng-14.duckerdns.org