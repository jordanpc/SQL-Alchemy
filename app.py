import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify


engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)


app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the home page!"

@app.route("/api/v1.0/stations")
def stations_route():
    stations = session.query(Station.station).all()
    station_list = []
    for item in stations:
        station_list.append(item[0])
    return jsonify(station_list)


@app.route("/api/v1.0/tobs")
def tobs_route():
    prev_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    tobs = session.query(Measurement.tobs).filter(Measurement.date > prev_date).all()
    temp_list = []
    for item in tobs:
        temp_list.append(item[0])
    return jsonify(temp_list)


@app.route("/api/v1.0/precipitation")
def precipitation():
    prev_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date > prev_date).all()
    prec_list = []
    for item in precipitation:
        prec_list.append(item[0])
    return jsonify(prec_list)


if __name__ == '__main__':
    app.run()
