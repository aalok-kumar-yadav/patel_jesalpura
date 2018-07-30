//Jquery For Hidden Team Carousel

      $(document).ready(function () {
        var carousel = $("#carousel").waterwheelCarousel({
          flankingItems: 3,
          movingToCenter: function ($item) {
            $('#callback-output').prepend('movingToCenter: ' + $item.attr('id') + '<br/>');
          },
          movedToCenter: function ($item) {
            $('#callback-output').prepend('movedToCenter: ' + $item.attr('id') + '<br/>');
          },
          movingFromCenter: function ($item) {
            $('#callback-output').prepend('movingFromCenter: ' + $item.attr('id') + '<br/>');
          },
          movedFromCenter: function ($item) {
            $('#callback-output').prepend('movedFromCenter: ' + $item.attr('id') + '<br/>');
          },
          clickedCenter: function ($item) {
            $('#callback-output').prepend('clickedCenter: ' + $item.attr('id') + '<br/>');
          }
        });

        $('#prev').bind('click', function () {
          carousel.prev();
          return false
        });

        $('#next').bind('click', function () {
          carousel.next();
          return false;
        });

        $('#reload').bind('click', function () {

          newOptions = eval("(" + $('#newoptions').val() + ")");
          carousel.reload(newOptions);
          return false;
        });

        $('#team_1').click(function(){
          carousel.show_member_image_function(0);

        });

        $('#team_2').click(function(){
          carousel.show_member_image_function(1);
        });

        $('#team_3').click(function(){
          carousel.show_member_image_function(2);
        });

        $('#team_4').click(function(){
          carousel.show_member_image_function(-2);
        });

        $('#team_5').click(function(){
          carousel.show_member_image_function(-1);
        });

      });


//Jquery For Team Slider

jssor_1_slider_init = function() {

            var jssor_1_options = {
              $AutoPlay: 0,
              $AutoPlaySteps: 5,
              $SlideDuration: 160,
              $SlideWidth: 200,
              $SlideSpacing: 3,
              $ArrowNavigatorOptions: {
                $Class: $JssorArrowNavigator$,
                $Steps: 5
              },
              $BulletNavigatorOptions: {
                $Class: $JssorBulletNavigator$
              }
            };

            var jssor_1_slider = new $JssorSlider$("jssor_1", jssor_1_options);

            /*#region responsive code begin*/

            var MAX_WIDTH = 1020;

            function ScaleSlider() {
                var containerElement = jssor_1_slider.$Elmt.parentNode;
                var containerWidth = containerElement.clientWidth;

                if (containerWidth) {

                    var expectedWidth = Math.min(MAX_WIDTH || containerWidth, containerWidth);

                    jssor_1_slider.$ScaleWidth(expectedWidth);
                }
                else {
                    window.setTimeout(ScaleSlider, 30);
                }
            }

            ScaleSlider();

            $Jssor$.$AddEvent(window, "load", ScaleSlider);
            $Jssor$.$AddEvent(window, "resize", ScaleSlider);
            $Jssor$.$AddEvent(window, "orientationchange", ScaleSlider);
            /*#endregion responsive code end*/
        };


// Function For HighLighting Navigation Bar

      $(function() {

        $('body').navHighlighter({
          underlineColour : '#F0C181',
          blur : '0px',
          height : '1px'
        });

      });


// Alert After Contact Form Submission

         $('#contact_button').click(function(){
          alert("Thanks for contacting us! We will get back to you soon!");
          location.reload();

        });


// Function For Opening Blog Description Page in New Tab

    function blog_description(blog_id)
    {
        url ="blog_description/"+blog_id;
        window.open(url);

    }


// Function For Opening Blog Home Page In New Tab

function open_blog_home_page()
{
    window.open("bloghome");

}


//Function For Opening Google Map in New Tab

function openmap()
{
    window.open("https://www.google.com/maps/place/Ashok+P+Patel+%26+Associates/@23.01942,72.5523803,17z/data=!4m8!1m2!2m1!1s803%2F804,+Samudra+Annexe,+C+G+Road,+Navrangpura+Ahmedabad,+Gujarat+380006!3m4!1s0x395e84f53fffffff:0xb7d9c67ff2e3313e!8m2!3d23.01942!4d72.554569");

}


// Function For Showing Member Details


function show_member_details(id){
   hide_member_details();
   var temp_id = '#mem_des_div_'+id.substring(5,6)
   $(temp_id).show();

}


// Function For Coming Back To Normal Front Service Division

function restore_service_division(){
    $("#hidden_fieldset_id").fadeOut(500);
    $("#fieldset_id").fadeIn(2300);

}


// Function For Coming Back To Normal Front Team Slider Division

function restore_team_division(){
    $("#carousel").fadeOut(500);
    $("#team_slider").fadeIn(2300);

}


// Function For Showing Team Division

function show_team_division(id){
    var str = id;
    var res = str.substring(0, 6);
    var num = str.substring(5, 6);
    var fin = parseInt(num);

    $("#team_slider").fadeOut(500);
    show_member_details(id);
    $("#carousel").fadeIn(2300);

}


// Function For Hiding Member Details

function hide_member_details(){
    var i;
    for (i=1;i<=5;i++){
    temp_mem_des = '#mem_des_div_'+i;
     $(temp_mem_des).hide();
    }

  }


// Function For Showing Front Service Division

function show_service_division(service_id){
    $("#fieldset_id").fadeOut(500);
    $("#hidden_fieldset_id").fadeIn(2300);

    var temp = service_id.substring(5, 6);
    show_service_content(temp);
}


// Function For Showing Service Content

function show_service_content(item_id){
		hide_service_content_division();
		temp =item_id
		if (item_id.length >1 ){
		    temp = item_id.substring(13, 14);
		}

        var temp_div = '#div_service_con_'+temp
        var temp_header = '#service_item_header_'+temp

		$(temp_div).fadeIn(1000);
        $(temp_header).css({'font-weight':'bolder'});

	}


// Function For Hiding Service Content

function hide_service_content_division(){
    var i ;
    for (i=1;i<=8;i++){
    temp_div_var = '#div_service_con_'+i
    temp_service_var = '#service_item_header_'+i
    $(temp_div_var).hide();
    $(temp_service_var).css({'font-weight':'normal'});
    }

}


// Document Ready Function for Home page

$(document).ready(function(){
    $('#cls').css({'height':window.screen.height});
    hide_service_content_division();
    $("#div1").show();

});

// Function for reloading Home page

function reload_home_page(){

alert("Thank You For Contacting Us!!!");
}