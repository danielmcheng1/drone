$(document).ready(function () {
    var gallery_counter = {};
    for (var ymd in executions_by_ymd.length) {
        var this_dates_data = executions_by_ymd[ymd];
        this_dates_images = [];
        for (int i = 0; i < this_dates_data.length; i++) {
            var image_info = '../static/images/' + this_dates_data["image_short_dir"] + "/" + this_dates_data["image_final"];
            this_dates_images.push({small: image_info, large: image_info});
            load_gallery(this_dates_images);
        }
    }
    
    function show_image(ymd, currSpan){
        var currIndex = gallery_image_index[ymd];
        var image = images[currIndex];
        viewer.load(image.small, image.big);
        currSpan.html(currIndex + 1);
    }
 

    function move_right(ymd, total) {
        var nextIndex = gallery_image_index[ymd] + 1;
        if(nextIndex >= total) nextIndex = 0;
        show_image(ymd, currSpan);
    }
    function move_left(ymd, total) {
        var nextIndex = gallery_image_index[ymd] - 1;
        if (nextIndex < 0) gallery_image_index[ymd] = total - 1;
        show_image(ymd, currSpan);
    }
    
    function load_gallery(ymd, images) {   
        var gallery_image_index[ymd] = 0;
        var total = images.length;
        
        var wrapper = $('#image-gallery-' + ymd);
        var currSpan = wrapper.find('.current');
        var viewer = ImageViewer(wrapper.find('.image-container'));
     
        //display total count
        wrapper.find('.total').html(total);
     
        wrapper.find('.next').click(moveRight(ymd));
        wrapper.find('.prev').click(moveLeft(ymd));
        
        //initially show image
        show_image(ymd, currSpan);
        
        // playback / animation         
        var interval;
        $(".animateCommand").click(function do_slide() {
            if ($(this).text().trim() == "Animate") {
                $(this).text("Stop Animation");
                interval = setInterval(function() {
                    moveRight(ymd, total);
                }, 1000);
            } else {
                clearInterval(interval);
                $(this).text("Animate");
            }
        });
    }
});
    /*    $(function () {
            var viewer = ImageViewer();
            $('.gallery-items').click(function () {
                var imgSrc = this.src,
                    highResolutionImage = $(this).data('high-res-img');
         
                viewer.show(imgSrc, highResolutionImage);
            });
        });
        var viewer = ImageViewer();
        var playback = $('.gallery-items');
        var playbackInterval;
        for (var i = 0; i < playback.length; i++) {
            var imgSrc = playback[i].src,
                highResolutionImage = $(playback[i]).data('high-res-img');
            playbackInterval = setInterval(function() {
                viewer.show(imgSrc, highResolutionImage);
                clearInterval(playbackInterval)
            }, 1000 * i);
        }*/