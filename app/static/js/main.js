var center_x = document.getElementById('map').getAttribute('data-center-x');
var center_y = document.getElementById('map').getAttribute('data-center-y');
var zoom = document.getElementById('map').getAttribute('data-zoom');

let mapOptions = {
    center: [center_x, center_y],
    zoom: zoom
}

let map = new L.map('map', mapOptions);

let layer = new L.TileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png');
map.addLayer(layer);

let marker = new L.Marker([center_x, center_y]);
marker.addTo(map);

//https://leafletjs.com/index.html