// Document Ready Function

            $(document).ready(function() {
			$("#txtEditor").Editor();

			});


// Function For getting Text Editor For Blog Writing

function function_editor(){

	        var text = $("#txtEditor").Editor("getText");

	        document.getElementById('blogDescription').value = text;

        }


// Function For changing Blog Status

function change_blog_view_status()
        {
        $.ajax({url: "redirect_admin/", success: function(result){
        }});

        }


//Function For showing Add Post Division

function show_addpost_division(){

      $(".addpost_class").show();

    }


        $("#addpost_id").click(function(){
              /*$(".addpost_class").hide(); */
          });



             // Function For displaying Blog Description

 function function_display_des(description)
 {
    link = "get_blog_description/"+description.substring(4,5)
    $.ajax({url: link, success: function(result){
    modal.style.display = "block";
    document.getElementById("display_blog_des").innerHTML = result;
                }});

    }


