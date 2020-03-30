$(document).ready(function(){

    let $buttons = $('.project-area .button-group button');

    $buttons.click(function(e){

        $('.project-area .button-group buttons').removeClass('active');
        e.target.classList.add('active');

        let selector = $(e.target).attr('data-filter');
        $('.project-area .grid').isotope({
            filter : selector
        })

        return false;

    });

    $('.project-area .button-group #btn1').trigger('click');

});