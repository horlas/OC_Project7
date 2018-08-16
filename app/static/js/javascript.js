
//Load JSON-encoded data from the server using a GET HTTP request.
//call root /_add_datas
$(function() {
            $('#submit').bind('click', function() {
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

                                 $('<div class="message">').text(data.wikipedia).appendTo('#grandpy');
                                 var map = initMap();
                                 $("#map-container").val(map)
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
    map = new google.maps.Map(document.getElementById('map-container'), {
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

function getMes(){
var user_mes = $("#target").val();
$('<div class="message">').html(user_mes).appendTo('#user');
}




