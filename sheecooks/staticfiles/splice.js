
// Include jQuery from CDN
$(document).ready(function() {
    var owl = $('.owl-carousel');
    owl.owlCarousel({
    items:2,
    loop:true,
    margin:2,
    autoplay:true,
    autoplayTimeout:5000,
    autoplayHoverPause:false,
    responsiveClass:true,
    responsive:{
        0:{
            items:1,
            nav:true
        },
        600:{
            items:1,
            nav:false
        },
        1000:{
            items:2,
            nav:true,
            loop:true
        }
    },
   
});
})

