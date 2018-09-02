//Load JSON-encoded data from the server using a GET HTTP request.
//call root /_add_datas
$(function() {
            $('#submit').on('click', function() {
                //display "GrandPy thinks"
                $("#monancre").hide();
                $(".progress").show();
                progressBar();
                //display user input
                getMes();
                setTimeout(function() {
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
                                //initialyse progress bar and show input area
                                progressBarnull();
                                $("#monancre").show();
                                $(".progress").hide();
                                //go to the bottom
                                $('html,body').animate({scrollTop: $('#monancre').offset().top}, "slow");
                            })
                    }, 3000);

                return false;}
                );
            });

//Initialize the dic whitch contains the map
function mapZone() {
    var $zone = $('<div  class="map-container d-flex justify-content-between mb-4" ></div>');
    $("#message").append($zone)
}

// Initialize and add the map
function initMap() {

  // The location of place
  var latElt = document.getElementById('lat');
  var lat = Number(latElt.textContent);
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

//add all html code to display user message
function addUserMes() {
    var $divheader = $('<div class="header"></div>').append('<strong class="primary-font">Gentil Visiteur</strong>');
    var $divchatbody = $('<div class="chat-body white p-3 z-depth-1"></div>').append(
                                                                                     $divheader,
                                                                                     '<hr class="w-100">',
                                                                                     '<p class="us_mess mb-0"></p>'
                                                                                    );
    // language=HTML
    var $zone = $('<li class="d-flex justify-content-between mb-4"></li>').append(
        $divchatbody,
        '<img src="../static/img/photoessaiuser.jpg" alt="avatar" class="avatar rounded-circle mr-0 ml-3 z-depth-1">'
    );

    $("#message").append($zone)
}
//catch user input onclick
function getMes(){
    var user_mes = $("#target").val();
    addUserMes();
    $('.us_mess').last().html(user_mes);
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
        '<img src="../static/img/photoessai2gp.jpg" alt="avatar" class="avatar rounded-circle mr-2 ml-lg-3 ml-0 z-depth-1">',
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

//to create the progress bar until 100%
function progressBar() {
    function timer(n) {
        $(".progress-bar").css("width", n + "%");
        if(n < 100) {
                setTimeout(function() {
                    timer(n + 10);
            }, 200);
        }
    }

    timer(0);
}

//to reinitialize the progress bar
function progressBarnull() {
      $('.progress-bar').css("width", "0%")
}

