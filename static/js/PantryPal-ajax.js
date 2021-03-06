$(document).ready(function(){
	$("#user_form").submit(function(event) {
		$('.next').data('search_terms', $("#query").val());
		$('.next').data('max_time', $("#time").val());

	    $.post('/PantryPal_app/search/', $(this).serialize() , function(data){
	    	$("#search_content").hide().html(data).fadeIn(1500);
	    });
	    $("#search_content").show();
	    $("#search_content").fadeIn();
	    //allow for smooth scroll
	    $('#go_up').localScroll();

	    event.preventDefault();
	});
});

$(document).ajaxStart(function() {
	$("#search_content").html("");
	$('#spinner').css("display", "inline-block");
	$('#container-folio').css("display", "none");
}).ajaxStop(function() {
	$('#spinner').css("display", "none");
	$('#search_content').css("display", "inherit");
	if ($('.needed').length == 16)	{
		$('.next').css('display', 'inline-block');
	}	
});