var $header = $('#header');

function debounce(func, wait, immediate) {
	var timeout;
	return function() {
		var context = this, args = arguments;
		var later = function() {
			timeout = null;
			if (!immediate) func.apply(context, args);
		};
		var callNow = immediate && !timeout;
		clearTimeout(timeout);
		timeout = setTimeout(later, wait);
		if (callNow) func.apply(context, args);
	};
};


/*
$(window).bind('scroll', 'touchmove', function () {
    // $('#header-content').toggleClass('tiny', $(document).scrollTop() > 300);
    // $('#navbar-wrapper').toggleClass('fixed-top', $(document).scrollTop() > 100);
    // console.log($(document).scrollTop());
    var scrollDistance = $(this).scrollTop();
    $header.css('height', 'calc(100vh - ' + scrollDistance + 'px)');
    var newHeaderBackground = Math.min(60, 37 + scrollDistance/10);
    $header.css('background-color', 'hsl(191, 12%, ' + newHeaderBackground + '%)');

    $('#header-splash').stop();
    $('#header-nav').stop();

    if ($header.height() < 200) {
            $('#header-splash').fadeOut(500, function() {
            $('#header-nav').fadeIn(500);
        });
    } else {
            $('#header-nav').fadeOut(500, function() {
            $('#header-splash').fadeIn(500);
        });
    }
});

*/

var checkScrollFn = function() {
	var scrollDistance = $(window).scrollTop();
		if (scrollDistance > 0) {
			$(window).unbind();
			$('#header-splash').fadeOut(500, function() {
				$('#header-nav').fadeIn(500);
				$('#header').css('height', '70px');	
				$('body').css('padding-top', '70px');
				$('html').animate({scrollTop:0},500);
				$('html').promise().done(function() {$('html').stop()});
		});
	}
};

$(window).on('scroll', checkScrollFn);
$(document).ready(checkScrollFn);

