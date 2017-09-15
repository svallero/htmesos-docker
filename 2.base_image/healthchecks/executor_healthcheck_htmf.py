from flask import Flask, abort
import htcondor
import socket
import os

app = Flask(__name__)

@app.route("/health")
def health():
  try:
      #return 'OK', 200
      coll = htcondor.Collector() 
      proj = coll.query(htcondor.AdTypes.Startd, projection=['Name', 'State', 'Activity'])
      res = proj[0]
      if res['State'] == 'Claimed':
        return 'OK', 200
      elif res['Activity'] == 'Benchmarking':
        return 'OK', 200
      else:
        abort(401)
  except:
    abort(401)

if __name__ == '__main__':
    app.run(host= '0.0.0.0')
