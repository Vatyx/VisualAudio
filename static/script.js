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
    console.log("In GetList");
    value = $(".inputfield");
    console.log(value);
}