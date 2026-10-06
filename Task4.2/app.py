from flask import Flask
import socket
import platform

app = Flask(__name__)

# Student Details
STUDENT_NAME = "Hoo Ying Kit"
STUDENT_ID = "105190469"

@app.route("/")
def deployment_dashboard():
    container_host = socket.gethostname()
    py_version = platform.python_version()

    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>SWE40006 - Task 4.2 Deployment Audit</title>
        <style>
            :root {{
                --bg: #0f172a;
                --card-bg: #1e293b;
                --text-main: #f8fafc;
                --text-muted: #94a3b8;
                --accent-blue: #38bdf8;
                --border-color: #334155;
            }}
            * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }}
            body {{
                background-color: var(--bg);
                color: var(--text-main);
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                padding: 20px;
            }}
            .container {{
                background-color: var(--card-bg);
                border: 1px solid var(--border-color);
                border-radius: 12px;
                max-width: 650px;
                width: 100%;
                padding: 32px;
                box-shadow: 0 10px 25px rgba(0,0,0,0.4);
            }}
            .header {{
                border-bottom: 1px solid var(--border-color);
                padding-bottom: 16px;
                margin-bottom: 24px;
            }}
            h1 {{ font-size: 22px; font-weight: 700; color: var(--text-main); margin-bottom: 6px; }}
            p.sub {{ color: var(--text-muted); font-size: 14px; line-height: 1.5; }}
            .grid {{
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 14px;
            }}
            .metric-box {{
                background-color: #0f172a;
                border: 1px solid var(--border-color);
                padding: 14px 16px;
                border-radius: 8px;
            }}
            .metric-label {{ font-size: 12px; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.5px; }}
            .metric-value {{ font-size: 15px; font-weight: 600; color: var(--accent-blue); margin-top: 4px; font-family: monospace; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>Deployment Portfolio Activity 4</h1>
                <p class="sub">SWE40006 Software Deployment and Evolution &mdash; Sub-task 4.2 (Credit Level)</p>
            </div>

            <div class="grid">
                <div class="metric-box">
                    <div class="metric-label">Student Name</div>
                    <div class="metric-value">{STUDENT_NAME}</div>
                </div>
                <div class="metric-box">
                    <div class="metric-label">Student ID</div>
                    <div class="metric-value">{STUDENT_ID}</div>
                </div>
                <div class="metric-box">
                    <div class="metric-label">Container ID (Hostname)</div>
                    <div class="metric-value">{container_host}</div>
                </div>
                <div class="metric-box">
                    <div class="metric-label">Python Runtime</div>
                    <div class="metric-value">v{py_version}</div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)