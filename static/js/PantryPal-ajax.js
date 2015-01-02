$(document).ready(function(){
	$("#user_form").submit(function(event) {
		// $("#spinner").css("display", "inline-block");
	    $.post('/PantryPal_app/search/', $(this).serialize() , function(data){
	    	$("#search_content").html(data);
	    });
	    $("#search_content").show();
	    $("#search_content").fadeIn();
	    // $('#spinner').css('display', 'none');
	    event.preventDefault();
	});
});

$(document).ajaxStart(function() {
	$('#spinner').css("display", "inline-block");
	$('#container-folio').css("display", "none");
}).ajaxStop(function() {
	$('#spinner').css("display", "none");

});