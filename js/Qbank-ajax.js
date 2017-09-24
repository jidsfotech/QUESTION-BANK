$(document).ready(function() {
      jQuery.support.cors = true;
      $('#QuestionPapers').hide();
      $('.courses').on('click', function(event) {
          $('#QuestionPapers_id').DataTable();
          event.preventDefault();
          $("#Qlist").empty();
          var Url = $(this).attr('rel');
          $.ajax({
              type: "GET",
              url: Url,
              dataType:"json",
              contentType: 'application/json',
              success: function (data) {
                  
                  var header = document.getElementById("QpapersHeader");
                  var trHTML = '';
                  for (var i=0; i < data.length; i++)
                  {
                      
                  trHTML += '<tr><td>'+'<a class="disp" href=/media/'+data[i][0]+'>'+data[i][0]+'</td><td>' + data[i][1]+ '</td><td>' + data[i][2]+ '</td><td>' + data[i][3]+ '</td></tr>';
          
                  header.innerHTML = "LIST OF AVAILABLE QUESTION PAPERS FOR"+ " " +data[i][4];
                  }
                  
                  $('#QuestionPapers_id').append(trHTML);
                   
                   $('#QuestionPapers').show();
                 
                  },
                  
    });
});
});


$(document).ready(function() {
    $('.disp').on('click', function(event) {
        event.preventDefault();
        var dis = $(this).attr('href'); 
        window.open(dis, '_blank')
    })
})
    

$(document).ready(function(){
    $("#CourseTable_id").dataTable({
        "paging":false,
        "searching":false,
        "info":false,
        "odering":false
        });
        });
        
$(document).ready(function(){
    $("#LevelTable_id").dataTable({
        "paging":false,
        "searching":false,
        "info":false,
        "odering":false
        });
        });
                

$(document).ready(function() {
    $('#id_level').on('change', function() {
    var pk = $(this).val();
    var pri_key = pk.replace(/\s/g, "_");
    
    $.ajax({
        type: "GET",
        url:"/Qbank/getCourseCodeAndTitle/"+pri_key,
        dataType:"json",
        contentType:'application/json',
        success: function (data) { 
            
            var course_title = '';
            var course_code = '';
            for (var i=0; i < data.length; i++)
            {
                course_title+='<option value='+'"'+data[i][0]+'"'+'>'+data[i][0]+'</option>';
                
                course_code+='<option value='+'"'+data[i][1]+'"'+'>'+data[i][1]+'</option>';
                } 
                
                $("#id_CourseTitle").append(course_title);
                $("#id_CourseCode").append(course_code);
              }, 
              
              });
        
        });
});
$('#bs-carousel').carousel({
    	pause: 'none'
	})


