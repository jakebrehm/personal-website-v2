$(document).ready(function(){

    let $buttons = $('.project-area .button-group button');

    $buttons.click(function(e){

        $('.project-area .button-group button').removeClass('active');
        e.target.classList.add('active');

        let selector = $(e.target).attr('data-filter');
        $('.project-area .grid').isotope({
            filter : selector
        })

        return false;

    });

    $('.project-area .button-group #btn1').trigger('click');


    // Sticky Navigation Menu

    let nav_offset_top = $('.header-area').height() + 50;

    function navbarFixed(){
        if($('.header-area').length){
            $(window).scroll(function(){
                let scroll = $(window).scrollTop();
                if(scroll >= nav_offset_top){
                    $('.header-area .main-menu .navbar').addClass('navbar-fixed');
                    $('.header-area .main-menu .navbar').removeClass('navbar-default');
                } else {
                    $('.header-area .main-menu .navbar').removeClass('navbar-fixed');
                    $('.header-area .main-menu .navbar').addClass('navbar-default');
                }
            })
        }
    }

    navbarFixed();

});