var main = function() {
  $('.filter').click(function() {
    $('.filter').removeClass("active");
    $(this).addClass("active");

  	// var selected = null;
  	var $selected = $(this).attr('data-filter')

  	var $category = $('#portfolio [data-category]');

  	$('.mix').addClass("hide");

  	if ($selected == 'all') {
  		$('.mix').removeClass('hide');
  	} else {
  		$category.filter('[data-category = "' + $selected + '"]')
          .removeClass('hide')
  	}
  });


};

$(document).ready(main);