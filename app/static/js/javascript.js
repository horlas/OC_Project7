
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
                    function (data) {
                                 $("#lat").text(data.lat);
                                 $("#lng").text(data.lng);
                                 $('<div class="gp_mess col-lg-6 col-lg-offset-1">').text(data.address).appendTo('#text_area');
                                 $('<div  class="gp_mess map-container col-lg-6 col-lg-offset-1" style="height:300px; border-radius:10px; margin: 5px; box-shadow: 5px 10px 10px 10px">').appendTo('#text_area');
                                 var map = initMap();
                                 $('text_area:last-child').val(map);
                                 $('<div class="gp_mess col-lg-6">').text(data.wikipedia).appendTo('#text_area');
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

  // The map, centered at right place
    map = new google.maps.Map(document.getElementById("text_area").lastChild, {
          zoom: 15,
          center: new google.maps.LatLng(lat, lon)});

    //add a marker
    var marker = new google.maps.Marker({
        position: {lat: lat, lng: lon},
        map: map
    });
    return map;

};

function getMes(){
var user_mes = $("#target").val();
$('<div class="us_mess col-lg-6 col-lg-offset-6">').html(user_mes).appendTo('#text_area');
};


//to activate Enter key
var input = document.getElementById("target");
input.addEventListener("keyup", function(event) {
    event.preventDefault();
    if (event.keyCode === 13) {
        document.getElementById("submit").click();
    }
});









////to get the footer at the end of the page ///
jQuery(document).ready(function($) {
    /**
     * Set footer always on the bottom of the page
     */
    function footerAlwayInBottom(footerSelector) {
        var docHeight = $(window).height();
        var footerTop = footerSelector.position().top + footerSelector.height();
        if (footerTop < docHeight) {
            footerSelector.css("margin-top", (docHeight - footerTop) + "px");
        }
    }
    // Apply when page is loading
    footerAlwayInBottom($("#footer"));
    // Apply when page is resizing
    $(window).resize(function() {
        footerAlwayInBottom($("#footer"));
    });
});







