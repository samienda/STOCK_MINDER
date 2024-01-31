$(document).ready(function() {
    $('.dropdown .submenu').hide();
      $('.dropdown').click(function() {
        $(this).find('.submenu').toggle();
      });
    });
  
    document.addEventListener('touchstart', function(event) {
      event.preventDefault(); 
      event.stopPropagation(); 
    }, { passive: false });