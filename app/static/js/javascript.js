// Initialize and add the map
function initMap() {
  // The location of place
  var latElt = document.getElementById('lat');
  var lat = Number(latElt.textContent);

  var lngElt = document.getElementById('lng');
  var lng = Number(lngElt.textContent);
 // var coordElt = document.getElementById('coord');
 // var coord = Object.freeze(coordElt.textContent);
  var place  = {lat, lng};

  // The map, centered at right place
  var map = new google.maps.Map(
      document.getElementById('map'), {center: place, zoom: 12});
    // The marker, positioned at the right place
  var marker = new google.maps.Marker({position: coord, map: map});
}
