var prevScrollpos = window.pageYOffset;

window.onscroll = function() {

    var currentScrollPos = window.pageYOffset;

    if (prevScrollpos > currentScrollPos) {

        showHeader();

    } else {
        
        hideHeader();

    }

    prevScrollpos = currentScrollPos;

};

function hideHeader() {

    $(".toggle").removeClass("is-visible").addClass("is-hidden");

}

function showHeader() {

    $(".toggle").removeClass("is-hidden").addClass("is-visible").addClass("scrolling");

}


$('.toast').toast('show');
