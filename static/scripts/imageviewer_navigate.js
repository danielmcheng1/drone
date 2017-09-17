$(document).ready(function () {
    var images = [{
        small : '../static/images/half.jpeg',
        big : '../static/images/half.jpeg'
    },{
        small : '../static/images/full_jagged.jpeg',
        big : '../static/images/full_jagged.jpeg'
    },{
        small : '../static/images/single.jpeg',
        big : '../static/images/single.jpeg'
    }];
 
    var curImageIdx = 1,
        total = images.length;
    var wrapper = $('#image-gallery'),
        curSpan = wrapper.find('.current');
    var viewer = ImageViewer(wrapper.find('.image-container'));
 
    //display total count
    wrapper.find('.total').html(total);
 
    function showImage(){
        var imgObj = images[curImageIdx - 1];
        viewer.load(imgObj.small, imgObj.big);
        curSpan.html(curImageIdx);
    }
 
    wrapper.find('.next').click(function(){
         curImageIdx++;
        if(curImageIdx > total) curImageIdx = 1;
        showImage();
    });
 
    wrapper.find('.prev').click(function(){
         curImageIdx--;
        if(curImageIdx < 0) curImageIdx = total;
        showImage();
    });
 
    //initially show image
    showImage();
    function moveRight() {
        curImageIdx++;
        if(curImageIdx > total) curImageIdx = 1;
        showImage();
    }
    $(".footer-info").click(function do_slide() {
        var interval;
        alert($(this) + " text: " + $(this).text());
        if ($(this).text() == "Animate") {
            $(this).text("Stop Animation");
            interval = setInterval(function() {
                moveRight();
            }, 1000);
        } else {
            clearInterval(interval);
        }
    });
});