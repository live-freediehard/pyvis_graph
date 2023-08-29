from flask import Flask, render_template, send_file
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('agg')
from io import BytesIO
import networkx as nx


app = Flask(__name__)

@app.route('/<int:nodes>')
def ind(nodes):
    return render_template("image.html", nodes=nodes)

@app.route('/graph/<int:nodes>')
def graph(nodes):
    G = nx.complete_graph(nodes)
    nx.draw(G)

    img = BytesIO() # file-like object for the image
    plt.savefig(img) # save the image to the stream
    img.seek(0) # writing moved the cursor to the end of the file, reset
    plt.clf() # clear pyplot

    return send_file(img, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)