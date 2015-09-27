a = 1;

function myWoo()
{
    console.log("yeeeeeeeep");
}

function freesoundRedirect()
{
    var redirect_uri = encodeURIComponent('https://flasktest-vatyx.c9.io/woo');
    location.href="https://accounts.spotify.com/authorize/?client_id=9344d5a91349489488cc51637d912e21&response_type=code&redirect_uri="+redirect_uri;
}

function getList()
{
    console.log("In GetListaaayy");
    var value = $("#inputField").val();
    $.get( "/gettracks", {'trackname': 'this'}, function(data)
    {
        console.log(data);
    });
}

function populate() {
  var val = $('#search').val();
  var $list = $('#listItem');
  $list.html('');
  if (!val) return;
  $.get('/gettracks', {trackname: val}, function(data) {
    var items = data.items;
    console.log(items[5]);
    items.slice(0, 10).map(function(item) {
      var artist = item.artists.map(function(a) { return a.name; }).join(', ');
      var k = item.name.indexOf("(");
      var name = k > 0 ? item.name.substring(0, item.name.indexOf("(")) : item.name;
      var explicit = item.explicit ? "EXPLICIT" : "";

      $list.append($('<div class="items">' +
        '<a href="/previewtrack?id=' + item.id + '">' + 
        '<img src="' + item.album.images[0].url + '"/>' +
        '<div class="info">' +
          '<h2 class="title"> ' + name + ' - ' + artist + ' </h2>' +
          '<p class="explicit">' + explicit + '</p>' +
          '<p class="pop">Popularity:' + item.popularity + '</p>' +
        '</div>' +
        '</a>' +
        '</div>'
        ));
    });
  });
}

$('#search').on('input propertychange paste', function() {
  populate();
});
