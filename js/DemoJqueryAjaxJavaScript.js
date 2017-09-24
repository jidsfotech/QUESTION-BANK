// THIS IS MY JAVA SCRIPT TEST LAB 


//this js function get element with the given name and change change the text when a click action is take
function DemoFunction(){
	document.getElementById("demo").innerHTML = "My first working java scripts";
    }
    

// this function binds change event to a select element, it redirects to another page base on user selection
$(document).ready(function() {
  // bind change event to select
  $('#dynamic_select').on('change', function() {
    var url = $(this).val(); // get selected value
    if (url) { // require a URL
      window.location = url; // redirect
    }
    return false;
  });
});

$( "li" ).each(function( index ) {
  console.log( index + ": " + $( this ).text() );
});
 
 /*SCRIPT FOR TESTING AJAX REQUEST ERROR 
this script will test if the connection to the server through ajax was succesful connection was succesful
===============================================================================================================================
********************************
TO TEST CLICK ACTION EVENT OF <a href>
 $(document).ready(function() {
  $("#courses").click(function(event) {
    event.preventDefault();
    var target = $(this).attr("href");
    console.log(target);
    console.dir();
    $.ajax({
      type: "GET",
      url: target,
            success:function (data, status, jqXHR){
                $("#container").html(data);
                alert("Local success callback.");},
            error:function (jqXHR, status, error){
                    alert("Local error callback.");
                    console.debug(jqXHR); 
                    console.debug(error);},
            complete:function (jqXHR, status){
                    alert("Local completion callback.");}
});
       });
       

ANOTHER AJAX REQUEST STATUS CHECKER TO GET SPECIFIC ERRORS       
$.ajax({
            url: target,
            type: "GET",
            dataType: "json",
            error: function(jqXHR, exception) {
            if (jqXHR.status === 0) {
                alert('Not connect.\n Verify Network.');
            } else if (jqXHR.status == 404) {
                alert('Requested page not found. [404]');
            } else if (jqXHR.status == 500) {
                alert('Internal Server Error [500].');
            } else if (exception === 'parsererror') {
                alert('Requested JSON parse failed.');
            } else if (exception === 'timeout') {
                alert('Time out error.');
            } else if (exception === 'abort') {
                alert('Ajax request aborted.');
            } else {
                alert('Uncaught Error.\n' + jqXHR.responseText);
            }
        }
});


$(document).ready(function() {
  $('.courses').click(function(event) {
    event.preventDefault();
    var target = $(this).attr('rel');
    $.ajax({
      type: "GET",
      url: target,
      
      success: function(data){
           alert(JSON.stringify(data));
          


          
      }});
  });
});





// JAVA SCRIPTS FOR QUESTION BANK

//This will retrive question papers base on user selection
$(document).ready(function() {
      $('#QuestionPapers_id').hide();
      $('.courses').click(function(event) {
          $('#QuestionPapers_id').show();
          event.preventDefault();
          var Url = $(this).attr('rel');
          $.ajax({
              type: "GET",
              url: Url,
              'contentType': 'application/json'
              }).done(function(data) {
              //data = {"data":data};
              $('#QuestionPapers_id').DataTable({
                "data": data,
                "columns": [
                {"data": "QuestionPapers"},
                {"data":"Date"}
                ]
             })
          });

      });
      });
      
$(document).ready(function(){
    $("#CourseTable_id").dataTable({
        "paging":false,
        "searching":false,
        "info":false,
        "odering":false
        });
        });


      
        



$(document).ready(function() {
      jQuery.support.cors = true;
      $('#QuestionPapers_id').hide();
      $('.courses').click(function(event) {
          $('#QuestionPapers_id').show();
          event.preventDefault();
          var Url = $(this).attr('rel');
          $.ajax({
              type: "GET",
              url: Url,
              data: "{}",
              dataType: "json",
              cache: false,
              contentType: 'application/json',
              success: function (data) {
              var trHTML = '';
              $.each(data.Countries, function (i, item) {
                       trHTML += '<tr><td>' + data.[i] + '</td><td>' + data.[i] + '</td></tr>';
                       
                       });
                       
                       $('#QuestionPapers_id').append(trHTML);
        
              },
        
        error: function (msg) {
            
            alert(msg.responseText);};
    });
});
})
  






  

*/



