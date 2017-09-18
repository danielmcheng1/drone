$(document).ready(function () {
    var gallery_counter = {};
    for (var ymd in executions_by_ymd.length) {
        var this_dates_data = executions_by_ymd[ymd];
        this_dates_images = [];
        for (int i = 0; i < this_dates_data.length; i++) {
            var image_info = '../static/images/' + this_dates_data["image_short_dir"] + "/" + this_dates_data["image_final"];
            this_dates_images.push({small: image_info, large: image_info, timestamp: this_dates_data["hms"]});
            load_gallery(this_dates_images);
        }
    }
    
    function show_image(images, ymd){
        var wrapper = $('#image-gallery-' + ymd);
        var currSpan = wrapper.find('.current');
        var viewer = ImageViewer(wrapper.find('.image-container'));
        var image = images[gallery_image_index[ymd]];
        
        viewer.load(image.small, image.big);
        $("#timestamp-for-" + ymd).text(image.timestamp);
        currSpan.html(gallery_image_index[ymd]);   
    }
 

    function move_right(images, ymd) {
        var newIndex = gallery_image_index[ymd] + 1;
        if (newIndex >= images.length) gallery_image_index[ymd] = 0;
        else gallery_image_index[ymd] = newIndex;
        
        show_image(images, ymd);        
    }
    function move_left(images, ymd) {
        var nextIndex = gallery_image_index[ymd] - 1;
        if (nextIndex < 0) gallery_image_index[ymd] = images.length - 1;
        
        show_image(images, ymd);        
    }
    
    function load_gallery(images, ymd) {   
        var gallery_image_index[ymd] = 0;
        
        var wrapper = $('#image-gallery-' + ymd);
        
        //display total count
        wrapper.find('.total').html(images.length);     
        wrapper.find('.next').click(moveRight(images, ymd));
        wrapper.find('.prev').click(moveLeft(images, ymd));
        
        //initially show image
        show_image(images, ymd);
        
        // playback / animation         
        var interval;
        $(".animateCommand").click(function do_slide() {
            if ($(this).text().trim() == "Animate") {
                $(this).text("Stop Animation");
                interval = setInterval(function() {
                    moveRight(images, ymd);
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