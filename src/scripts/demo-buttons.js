$(function(){
    $('#sample-1-button').click(function(){
        if(!$('#iframe-1').length) {
            $('#iframeHolder-1').html('<iframe allowfullscreen webkitallowfullscreen width="640" height="480" frameborder="0" seamless src="https://p3d.in/e/ZLbp9"></iframe>');
        }
    });

    $('#sample-2-button').click(function(){
        if(!$('#iframe-2').length) {
            $('#iframeHolder-2').html('<iframe allowfullscreen webkitallowfullscreen width="640" height="480" frameborder="0" seamless src="https://p3d.in/e/fd0hx"></iframe>');
        }
    });

    $('#sample-3-button').click(function(){
        if(!$('#iframe-3').length) {
            $('#iframeHolder-3').html('<iframe allowfullscreen webkitallowfullscreen width="640" height="480" frameborder="0" seamless src="https://p3d.in/e/5vhhQ"></iframe>');
        }
    });
});