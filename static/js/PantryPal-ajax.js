// $(document).ready(function(){
	$("#user_form").submit(function(event) {
		$("#search_content").hide();
	    $.post('/PantryPal_app/search/', $(this).serialize() , function(data){
	    	$("#search_content").html(data);
	    });
	    $("#search_content").show();
	    $("#search_content").fadeIn();
	    event.preventDefault();
	});
// });


