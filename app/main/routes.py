from flask import render_template, flash, redirect, url_for, request
from app.main import bp


@bp.route("/location")
def geo_loc():
    center_x = request.args.get("center_x")
    center_y = request.args.get("center_y")
    zoom = request.args.get("zoom")

    # http://127.0.0.1:5000/geo/location?center_x=40.44062&center_y=-79.99589&zoom=11
    return render_template(
        "index.html", center_x=center_x, center_y=center_y, zoom=zoom
    )
