
//Load JSON-encoded data from the server using a GET HTTP request.
//call root /_add_datas
$(function() {
            $('a#submit').bind('click', function() {
                //$.getJSON(--url, --data, --func)
                $.getJSON(
                    //url
                    $SCRIPT_ROOT + '/_add_datas',
                    //data
                    {place: $('input[name="place"]').val()},
                    //func
                    function (data) {$("#coord").text(data.coordinates);
                                 $("#lat").text(data.lat);
                                 $("#lng").text(data.lng);
                                 $("#address").text(data.address);
                                 $("#story").text(data.wikipedia);
                                 var map = initMap();
                                 $("#map").val(map)
                });
                return false;}
                );
            });

// Initialize and add the map


function initMap() {

  // The location of place
  var latElt = document.getElementById('lat');
  var lat = Number(latElt.textContent);
  console.log(lat);

  var lngElt = document.getElementById('lng');
  var lon = Number(lngElt.textContent);
  console.log(lng);

  // The map, centered at right place
    map = new google.maps.Map(document.getElementById('map'), {
          zoom: 15,
          center: new google.maps.LatLng(lat, lon)},
        )
    //add a marker
    var marker = new google.maps.Marker({
        position: {lat: lat, lng: lon},
        map: map
    });

    return map;

}








//window.onload = initMap();


