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
    items.slice(0, 10).map(function(item) {
      var artist = item.artists.map(function(a) { return a.name; }).join(', ');
      $list.append($('<li><a href="/previewtrack?id=' + item.id + '">' + item.name + ' - ' + artist + '</a></li>'));
    });
  });
}

$('#search').on('input propertychange paste', function() {
  populate();
});
