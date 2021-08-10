from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return(
        f"Welcome to the Surf's Up API!<br/>"
        f"Usage:<br/>"
        f"/api/v1.0/precipitation Returns a JSON list of precipitation from 8/23/2016 to 8/23/2017<br/>"
        f"/api/v1.0/stations Returns a JSON list of stations in Hawaii<br/>"
        f"/api/v1.0/tobs Returns a JSON list of temperature observations during the timeframe<br/>"
        f"/api/v1.0/<start> and /api/v1.0/<start>/<end> Return a JSON of min, max, avg temps for the range<br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    precip_data = session.query(Measurement.date, func.avg(Measurement.prcp)).filter(Measurement.date >= twelve_months).group_by(Measurement.date).all()
    return jsonify(precip_data)