
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
                                 addGPyMess(data.address);

                                 mapZone();
                                 initMap();
                                 addGPyMess(data.wikipedia);
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
    map = new google.maps.Map(document.getElementById("message").lastChild, {
          zoom: 15,
          center: new google.maps.LatLng(lat, lon)});

    //add a marker
    var marker = new google.maps.Marker({
        position: {lat: lat, lng: lon},
        map: map
    })

}

function mapZone() {
    console.log("yes");
    // var $divchatbody = $('<div id="MAP" class="map-container">Coucou</div>');
    // var $zone = $('<li class="d-flex justify-content-between mb-4"></li>').append($divchatbody);
    var $zone = $('<div  class="map-container d-flex justify-content-between mb-4" ></div>');
    $("#message").append($zone)
}







//catch user input onclick
function getMes(){
    var user_mes = $("#target").val();
    console.log(user_mes);
    addUserMes();
    $('.us_mess').html(user_mes);
}



//add all html code to display user message
function addUserMes() {
    var $divheader = $('<div class="header"></div>').append('<strong class="primary-font">Gentil Visiteur</strong>');
    var $divchatbody = $('<div class="chat-body white p-3 z-depth-1"></div>').append(
                                                                                     $divheader,
                                                                                     '<hr class="w-100">',
                                                                                     '<p class="us_mess mb-0"></p>'
                                                                                    );
    var $zone = $('<li class="d-flex justify-content-between mb-4"></li>').append(
        $divchatbody,
        '<img src="https://mdbootstrap.com/img/Photos/Avatars/avatar-5" alt="avatar" class="avatar rounded-circle mr-0 ml-3 z-depth-1">'
    );

    $("#message").append($zone)
}
//add all html code to display GdPy message, and take in argument data.adress from Ajax call
function addGPyMess(message){
    var $divheader = $('<div class="header"></div>').append('<strong class="primary-font">Grand Py</strong>');
    var $gpyMess = $('<p class="gp_mess mb-0">message</p>').text(message);
    var $divchatbody = $('<div class="chat-body white p-3 z-depth-1"></div>').append(
                                                                                     $divheader,
                                                                                     '<hr class="w-100">',
                                                                                     $gpyMess
);
    var $zone = $('<li class="d-flex justify-content-between mb-4"></li>').append(
        '<img src="https://mdbootstrap.com/img/Photos/Avatars/avatar-6" alt="avatar" class="avatar rounded-circle mr-2 ml-lg-3 ml-0 z-depth-1">',
        $divchatbody
    );

    $("#message").append($zone)
}


//to activate Enter key on input form
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







