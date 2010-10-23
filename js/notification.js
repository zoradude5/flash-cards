NotificationManager = function(parent) {
    this.parent = parent;
    this.content = $(document.createElement('div'));
    this.div = $(document.createElement('div')).addClass('lightbox').append(this.content);
    
    this.parent.append(this.div);
}

NotificationManager.prototype.show = function(content) {
    var self = this;
    this.content.text(content);
    self.div.animate({opacity: 1}, 'slow');
    self.div.css('zIndex','10');
    this.div.queue(function() {
        setTimeout(function() {
            self.div.animate({opacity: 0}, 'slow', function() {
                self.div.css('zIndex','-1')
            });
            self.div.dequeue();
        }, 1000);
    });
}

NotificationManager.prototype.hide = function() {
    this.div.css('visibility', 'hidden');
}