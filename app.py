from flask import Flask, jsonify

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

@app.route("/api/v1.0/stations")
def stations():
    active_stations = session.query(Station.station, Station.name).all()
    return jsonify(active_stations)

@app.route("/api/v1.0/tobs")
def tobs():
    temp_data = session.query(Measurement.date, Measurement.station, Measurement.tobs).filter(Measurement.date >= twelve_months).all()
    return jsonify(temp_data)

@app.route("/api/v1.0/<start>")
def startDateOnly(date):
    day_results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= date).all()
    return jsonify(day_results)

@app.route("/api/v1.0/<start>/<end>")
def startDateEndDate(start,end):
    multiple_days = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    return jsonify(multiple_days)

if __name__ == "__main__":
    app.run(debug=True)
