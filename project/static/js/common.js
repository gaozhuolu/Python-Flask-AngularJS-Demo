function contHeight(){
	var winHeight = $(window).height() - $('.main-header').height();
	$('#contentHeight').css('min-height', winHeight +'px' );

}

function rightFormHeight(){
	var height = $(window).height() - $('.top-new-section').height() - $('.main-header').height() ;
	$('.right-form').css('min-height', height +'px');
}

function dashboardChartSize() {
	//if( $('#div-new-contacts') ) {
	//	console.log($('#div-new-contacts').height());
	//	$('#div-autoresponse-summary').css('height', $('#div-new-contacts').height() + 'px');
	//	$('#div-autoresponse-summary').css('min-height', $('#div-new-contacts').height() + 'px');
	//}
}

function svgbarFunction() {
	$('.svg-bar').on('click', function(){
		$('body').toggleClass('menuOpen');
		$('.svg-bar').toggleClass('close-toggle');
	});
}

function dropdownCompanylist(e){
	console.log('dropbtn - clicked');
	e.stopPropagation();
	if ($('#myDropdown').is(":visible")) {
		$('#myDropdown').hide();
	}
	else {
		$('#myDropdown').show();
	}
}

function initFunctions() {
	contHeight();
	rightFormHeight();
	dashboardChartSize();

	$('body').removeClass('menuOpen');

	$(window).click(function() {
		$('#myDropdown').hide();
	});
}

jQuery(document).ready(function(){
	initFunctions();
	$(window).resize(function(){
		initFunctions();
	});
});