NotificationManager = function(parent) {
    this.parent = parent;
    this.div = $(document.createElement('div')).addClass('lightbox');
    
    
    this.parent.append(this.div);
}

NotificationManager.prototype.show = function(content) {
    var self = this;
    this.div.text(content);
    self.div.animate({opacity: 1}, 'slow');
    this.div.queue(function() {
        setTimeout(function() {
            self.div.animate({opacity: 0}, 'slow');
            self.div.dequeue();
        }, 1000);
    });
}

NotificationManager.prototype.hide = function() {
    this.div.css('visibility', 'hidden');
}