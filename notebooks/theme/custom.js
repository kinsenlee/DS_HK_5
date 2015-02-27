/*

%%javascript

window.load_remote_theme = false
var theme_url = "https://drostehk.github.io/ipynb-theme/";
var asset_url = 'https://raw.githubusercontent.com/tijptjik/DS_assets/master/';

window.load_local_theme = function(){
    var hostname = document.location.hostname
    return ((hostname == "localhost" || hostname == '127.0.0.1') && !load_remote_theme)
}

var url = load_local_theme() ? document.location.origin + "/files/theme/custom.js" : theme_url + 'custom.js'

$.getScript(url)


*/

// Theme and Asset base URLs, change these to your fork.

if (typeof theme_url !== 'undefined'){
    var theme_url   = 'http://drostehk.github.io/ipynb-theme/'
}
if (typeof asset_url !== 'undefined'){
    var asset_url   = 'https://drostehk.github.io/notebook-assets/'
}


// Hide the theme Cell

$('.cell:first').hide()

// Load the styles

if (load_local_theme()){
    theme_url = document.location.origin + '/files/theme/'
}

$('<link>')
  .appendTo($('head'))
  .attr({type : 'text/css', rel : 'stylesheet'})
  .attr('href', theme_url + 'custom.css');

// Insert stylised elements

$('<img>')
  .prependTo($('h1'))
  .attr({src : 'assets/nodes.png', alt : 'break', class : 'lead'});

// Load the assets

if (load_local_theme()){
    asset_url = document.location.origin + '/files/assets/'
}

$('img[src^="assets/"]').each(
    function(){
        var $this = $(this);
        var img = $this.attr('src').split('/')[1];
        $this.attr('src', asset_url + img)
    }
)

// Create events for jQuery show and hide methods

$.each(['show', 'hide'], function (i, ev) {
    var el = $.fn[ev];
    $.fn[ev] = function () {
        this.trigger(ev);
        return el.apply(this, arguments);
    };
});

// Render Resource Blocks - see for example http://prologue.datascience.hk

$('.rendered_html').on('show', function() {
    var resource_img = $('[alt="resource"]').map(function(i,e){return $(e).attr('src')})
    var resource_text = $('[alt="resource"]').siblings('a').map(function(i,e){return $(e).text()})
    var resource_links = $('[alt="resource"]').siblings('a').map(function(i,e){return $(e).attr('href')})

    $('[alt="resource"]').each(function(i,e){
        $p = $(e).parent('p');
        $p.empty()
            .addClass('resource-container')
            .append('<a>')
            .find('a')
            .attr('href', resource_links[i])
            .append('<div>')
            .find('div')
            .css('background-image','url(' + resource_img[i]+')')
            .parent()
            .append('<p>')
            .find('p')
            .text(resource_text[i])
    })
})

$('.rendered_html').trigger('show')
