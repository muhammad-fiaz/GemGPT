import sys
from webui import app

if "--share" in sys.argv:
    app.launch(share=True)
else:
    app.launch()
