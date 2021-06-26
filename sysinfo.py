import threading
import time
import sys
import random
import platform
import psutil
import webview


html = """
<!DOCTYPE html>
<html>
<head lang="en">
<meta charset="UTF-8">

<style>

    body {
        background-color: #282a36;
        color: white;
    }

    #response-container {
        display: none;
        padding: 3rem;
        margin: 3rem 5rem;
        font-size: 120%;
        border: 5px #282a36;
    }

    h1 { color: white; font-family: 'Helvetica Neue', sans-serif; font-size: 46px; font-weight: 100; line-height: 50px; letter-spacing: 1px; padding: 0 0 40px; border-bottom: double #555; text-align: center; }

    label {
        margin-left: 0.3rem;
        margin-right: 0.3rem;
    }

    .btn {
        border: none;
        font-family: 'Lato';
        font-size: inherit;
        color: inherit;
        cursor: pointer;
        padding: 25px 80px;
        display: inline-block;
        margin: 15px 30px;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-weight: 700;
        outline: none;
        position: relative;
        -webkit-transition: all 0.3s;
        -moz-transition: all 0.3s;
        transition: all 0.3s;
        background: #6272a4;
        color: #fff;
        border-radius: 50px;
    }

    .btn:hover {
        background: #44475a;
    }
</style>
</head>
<body>


<h1>System info</h1>
<button class="btn"  onClick="initialize()">Get info!</button><br/>
<div id="response-container"></div>
<script>
    window.addEventListener('pywebviewready', function() {
        var container = document.getElementById('pywebview-status')
        container.innerHTML = '<i>pywebview</i> is ready'
    })

    function showResponse(response) {
        var container = document.getElementById('response-container')

        container.innerText = response.message
        container.style.display = 'block'
    }

    function initialize() {
        pywebview.api.init().then(showResponse)
    }

</script>
</body>
</html>
"""


class Api:
    def __init__(self):
        self.cancel_heavy_stuff_flag = False

    def init(self):

        dist = platform.dist()
        dist = " ".join(x for x in dist)
        ram = str(round(psutil.virtual_memory().total / (1024.0 **3)))

        response = {
                'message': 'OS: ' + "GNU/"+platform.system() + "\n" + 'Arch: ' + platform.architecture()[0]+"/"+platform.machine()+ "\n" + "Distro: " + dist + "\n" + "Kernel: " + platform.release() + "\n"  + "Memory: " + ram + "GB"
        }
        return response

if __name__ == '__main__':
    api = Api()
    window = webview.create_window('System/Machine info', html=html, js_api=api)
    webview.start()
