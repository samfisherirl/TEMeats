(function($){"use strict";$.fn.layer_slider_height_helper=function(options){return this.each(function(){var container=$(this),first_div=container.find('>div').first(),timeout=!1,counter=0,reset_size=function(){if(first_div.height()>0||counter>5){container.height('auto')}else{timeout=setTimeout(reset_size,500);counter++}};if(!first_div.length){return}
timeout=setTimeout(reset_size,0)})}}(jQuery))