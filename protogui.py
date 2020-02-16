# What should we do with our user interface??

from flask import Flask, render_template
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map

app = Flask(__name__, template_folder="templates")
app.config['GOOGLEMAPS_KEY'] = "AIzaSyBYhkmFKfz745tUYWf5CskwslxKan6M_-E"
GoogleMaps(app)

# TODO: GET THE MARKERS: THEIR
merkers = []

@app.route("/")
def mapview():
    # creating a map in the view
    mymap = Map(
        identifier="view-side",
        lat=43.782421,
        lng=-79.186651,
        markers=[(43.782421, -79.186651), (43.774823, -79.258845)
                 ]
    )
    sndmap = Map(
        identifier="sndmap",
        lat=43.782421,
        lng=-79.186651,
        markers=[
            {
                'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
                'lat': 43.774823,
                'lng': -79.258845,
                'infobox': "<b>Scarborough Town Center</b>"
            },
            {
                'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
                'lat': 43.782421,
                'lng': -79.186651,
                'infobox': "<b>UTSC</b>"
            }
        ]
    )
    return render_template('template.html', mymap=mymap, sndmap=sndmap)

if __name__ == "__main__":
    app.run(debug=True)
